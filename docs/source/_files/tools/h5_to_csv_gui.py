#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
h5_to_csv_gui.py — Convertisseur graphique HDF5 (Pymodaq « Log Data ») -> CSV.

Interface PyQt6 :
  1. Bouton « Importer un fichier .h5 ».
  2. À l'import, les colonnes et leurs 5 premières valeurs s'affichent (aperçu).
  3. Bouton « Convertir en CSV… » : demande où sauvegarder, puis écrit le CSV.

Le CSV est pensé pour être tracé dans un tableur (Excel, LibreOffice) :
  - UNE seule colonne « temps », axe commun à tous les signaux ;
  - timestamp converti en date + heure lisible : JJ/MM/AAAA HH:MM:SS,cc ;
  - pas de colonne « index » ;
  - trous comblés : valeur précédente recopiée (ou suivante si rien avant) ;
  - virgule décimale (Excel FR), séparateur de colonnes « ; ».

Le nom de chaque colonne de données est l'attribut « label » du signal ; Pymodaq le
stocke en dictionnaire typé ({"...", "data": "'t_resistance'"}) dont on extrait « data ».

Dépendances :  pip install PyQt6 h5py numpy
Lancement :    python h5_to_csv_gui.py
Remarque : l'heure est convertie en heure LOCALE de la machine.
"""

import os
import re
import csv
import json
import sys
from collections import OrderedDict
from datetime import datetime

try:
    import h5py
    import numpy as np
except ImportError:
    print("ERREUR : modules manquants. Installez :  pip install PyQt6 h5py numpy")
    raise

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTableWidget, QTableWidgetItem, QFileDialog, QMessageBox, QHeaderView,
)

APERCU_LIGNES = 5          # nombre de lignes affichées en aperçu
SEPARATEUR_CSV = ";"       # séparateur de colonnes du CSV (compatible Excel FR)
DECIMAL_CSV = ","          # séparateur décimal (virgule pour Excel FR)


# ----------------------------------------------------------------------------
# Logique de lecture HDF5 (identique au script en ligne de commande)
# ----------------------------------------------------------------------------
def extraire_data(valeur):
    """Extrait la valeur utile d'un attribut Pymodaq (clé 'data', guillemets retirés)."""
    if isinstance(valeur, bytes):
        valeur = valeur.decode("utf-8", "replace")
    if isinstance(valeur, dict):
        texte = str(valeur.get("data", ""))
    else:
        texte = str(valeur).strip()
        if texte.startswith("{") and '"data"' in texte:
            try:
                obj = json.loads(texte)
                if isinstance(obj, dict) and "data" in obj:
                    texte = str(obj["data"])
            except Exception:
                m = re.search(r'"data"\s*:\s*"(.*?)"\s*}', texte)
                if m:
                    texte = m.group(1)
    texte = texte.strip()
    while len(texte) >= 2 and texte[0] in "'\"" and texte[-1] == texte[0]:
        texte = texte[1:-1].strip()
    return texte


def lire_label(dataset):
    """Renvoie le 'label' utile du dataset (ou d'un parent proche), sinon None."""
    noeud = dataset
    for _ in range(3):
        if noeud is None:
            break
        attrs = getattr(noeud, "attrs", {})
        if "label" in attrs:
            valeur = extraire_data(attrs["label"])
            if valeur:
                return valeur
        noeud = getattr(noeud, "parent", None)
    return None


MARQUEURS = r'/(?:NavAxes|Axes|Data0D|Data1D|Data2D|DataND)(?:/|$)'


def groupe_de(path):
    return re.split(MARQUEURS, path, maxsplit=1)[0]


def est_axe(path):
    return ("/NavAxes/" in path) or ("/Axes/" in path)


def periode(temps):
    if temps is None or temps.size < 2:
        return float("nan")
    d = np.diff(np.asarray(temps, dtype=float))
    d = d[d > 0]
    return float(np.median(d)) if d.size else float("nan")


def decimales_pour(per):
    if per != per or per <= 0:
        return 3
    if per >= 1:
        return 0
    if per >= 0.1:
        return 1
    if per >= 0.01:
        return 2
    return 3


def cle_temps(ts, quantum):
    return int(round(float(ts) * 1e6 / quantum)) * quantum


def temps_lisible(micro_us, decimals, decimal=DECIMAL_CSV):
    """Microsecondes depuis l'époque -> 'JJ/MM/AAAA HH:MM:SS[,cc]' (heure locale)."""
    sec, micro = micro_us // 1_000_000, micro_us % 1_000_000
    base = datetime.fromtimestamp(sec).strftime("%d/%m/%Y %H:%M:%S")
    if decimals > 0:
        return base + decimal + "{:06d}".format(micro)[:decimals]
    return base


def remplir(tableau):
    """Comble les trous : recopie de la valeur précédente, puis de la suivante."""
    a = np.asarray(tableau, dtype=float)
    derniere = np.nan
    for i in range(a.size):
        if np.isnan(a[i]):
            a[i] = derniere
        else:
            derniere = a[i]
    suivante = np.nan
    for i in range(a.size - 1, -1, -1):
        if np.isnan(a[i]):
            a[i] = suivante
        else:
            suivante = a[i]
    return a


def noms_colonnes_uniques(labels):
    bruts = [(lab if lab else "Data") for lab in labels]
    compteur, colonnes = {}, []
    for nom in bruts:
        if nom in compteur:
            compteur[nom] += 1
            colonnes.append("{}_{}".format(nom, compteur[nom]))
        else:
            compteur[nom] = 0
            colonnes.append(nom)
    return colonnes


def charger_groupes(chemin):
    """Renvoie une liste de groupes : {'temps': array|None, 'canaux': [(label, array)]}."""
    axes = {}
    data = OrderedDict()

    with h5py.File(chemin, "r") as f:
        def visiteur(nom, objet):
            if not isinstance(objet, h5py.Dataset):
                return
            try:
                arr = np.atleast_1d(np.asarray(objet[()]).squeeze())
            except Exception:
                return
            if arr.ndim != 1 or arr.size == 0 or not np.issubdtype(arr.dtype, np.number):
                return
            g = groupe_de(nom)
            if est_axe(nom):
                if g not in axes:
                    axes[g] = arr
            else:
                data.setdefault(g, []).append((lire_label(objet) or "Data", arr))

        f.visititems(visiteur)

    return [{"temps": axes.get(g), "canaux": canaux} for g, canaux in data.items()]


def construire_table(groupes, decimal=DECIMAL_CSV):
    """Construit (entetes, lignes) avec UNE colonne temps commune et trous comblés."""
    noms = iter(noms_colonnes_uniques([lab for g in groupes for lab, _ in g["canaux"]]))
    signaux = []
    for g in groupes:
        t = g["temps"]
        for _lab, arr in g["canaux"]:
            tt = t[:arr.size] if (t is not None and t.size >= arr.size) else t
            signaux.append((next(noms), tt, arr))

    if not signaux:
        return ["temps"], []

    periodes = [periode(t) for _, t, _ in signaux if t is not None]
    periodes = [p for p in periodes if p == p]
    fine = min(periodes) if periodes else 1.0
    dec = decimales_pour(fine)
    quantum = int(round(10 ** (6 - dec)))

    grille = sorted({cle_temps(x, quantum) for _, t, _ in signaux if t is not None for x in t})
    if not grille:
        grille = list(range(max((v.size for _, _, v in signaux), default=1)))
        pos = None
    else:
        pos = {g: i for i, g in enumerate(grille)}
    n = len(grille)

    entetes = ["temps"] + [lab for lab, _, _ in signaux]
    colonnes = []
    for _lab, t, v in signaux:
        a = np.full(n, np.nan)
        if t is not None and pos is not None:
            for ts, val in zip(t, v):
                a[pos[cle_temps(ts, quantum)]] = float(val)
        else:
            a[:min(n, v.size)] = np.asarray(v, dtype=float)[:min(n, v.size)]
        colonnes.append(remplir(a))

    lignes = []
    for i in range(n):
        row = [temps_lisible(grille[i], dec, decimal)] if pos is not None else [str(i)]
        for col in colonnes:
            val = col[i]
            row.append("" if val != val else float(val))
        lignes.append(row)
    return entetes, lignes


def formater_cellule(valeur, decimal=DECIMAL_CSV):
    """Float -> chaîne à virgule ; chaîne (temps) ou vide -> inchangée."""
    if isinstance(valeur, (float, np.floating)):
        return str(float(valeur)).replace(".", decimal)
    return str(valeur)


def ecrire_csv(chemin_csv, entetes, lignes, sep=SEPARATEUR_CSV, decimal=DECIMAL_CSV):
    with open(chemin_csv, "w", newline="", encoding="utf-8-sig") as fp:
        writer = csv.writer(fp, delimiter=sep)
        writer.writerow(entetes)
        for row in lignes:
            writer.writerow([formater_cellule(c, decimal) for c in row])
    return len(lignes)


# ----------------------------------------------------------------------------
# Interface graphique
# ----------------------------------------------------------------------------
class Convertisseur(QWidget):
    def __init__(self):
        super().__init__()
        self.chemin_h5 = None
        self.entetes = []
        self.lignes = []
        self._construire_ui()

    def _construire_ui(self):
        self.setWindowTitle("Convertisseur HDF5 → CSV — Pymodaq")
        self.resize(900, 480)
        layout = QVBoxLayout(self)

        titre = QLabel("Convertisseur HDF5 → CSV")
        titre.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(titre)

        sous_titre = QLabel("Axe de temps unique (date + heure lisible) · trous comblés · "
                            "virgule décimale · à tracer ensuite dans Excel.")
        sous_titre.setStyleSheet("color: #555;")
        layout.addWidget(sous_titre)

        ligne_haut = QHBoxLayout()
        self.btn_import = QPushButton("Importer un fichier .h5")
        self.btn_import.clicked.connect(self.importer)
        ligne_haut.addWidget(self.btn_import)
        self.lbl_fichier = QLabel("Aucun fichier importé.")
        self.lbl_fichier.setStyleSheet("color: #555;")
        ligne_haut.addWidget(self.lbl_fichier, stretch=1)
        layout.addLayout(ligne_haut)

        layout.addWidget(QLabel("Aperçu ({} premières lignes) :".format(APERCU_LIGNES)))
        self.table = QTableWidget(0, 0)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table, stretch=1)

        ligne_bas = QHBoxLayout()
        self.lbl_statut = QLabel("")
        self.lbl_statut.setStyleSheet("color: #2E7D46;")
        ligne_bas.addWidget(self.lbl_statut, stretch=1)
        self.btn_convertir = QPushButton("Convertir en CSV…")
        self.btn_convertir.setEnabled(False)
        self.btn_convertir.clicked.connect(self.convertir)
        ligne_bas.addWidget(self.btn_convertir)
        layout.addLayout(ligne_bas)

    # ----- actions -----
    def importer(self):
        chemin, _ = QFileDialog.getOpenFileName(
            self, "Choisir un fichier HDF5", "",
            "Fichiers HDF5 (*.h5 *.hdf5);;Tous les fichiers (*)")
        if chemin:
            self.charger(chemin)

    def charger(self, chemin):
        """Charge un fichier et remplit l'aperçu (méthode testable sans dialogue)."""
        try:
            groupes = charger_groupes(chemin)
            if not groupes:
                raise ValueError("Aucun signal numérique trouvé dans ce fichier.")
            entetes, lignes = construire_table(groupes, decimal=DECIMAL_CSV)
        except Exception as exc:
            QMessageBox.critical(self, "Erreur d'importation", str(exc))
            self.lbl_statut.setText("")
            return
        self.chemin_h5 = chemin
        self.entetes = entetes
        self.lignes = lignes
        self.lbl_fichier.setText(os.path.basename(chemin))
        self._remplir_apercu()
        self.btn_convertir.setEnabled(True)
        self.lbl_statut.setText("{} colonne(s), {} ligne(s).".format(len(entetes), len(lignes)))

    def _remplir_apercu(self):
        nb_lignes = min(APERCU_LIGNES, len(self.lignes))
        self.table.clear()
        self.table.setColumnCount(len(self.entetes))
        self.table.setRowCount(nb_lignes)
        self.table.setHorizontalHeaderLabels(self.entetes)
        for i in range(nb_lignes):
            for c, valeur in enumerate(self.lignes[i]):
                item = QTableWidgetItem(formater_cellule(valeur))
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
                self.table.setItem(i, c, item)

    def convertir(self):
        if not self.lignes:
            return
        defaut = os.path.splitext(self.chemin_h5)[0] + ".csv"
        chemin_csv, _ = QFileDialog.getSaveFileName(
            self, "Enregistrer le CSV", defaut, "Fichiers CSV (*.csv)")
        if not chemin_csv:
            return
        try:
            n = ecrire_csv(chemin_csv, self.entetes, self.lignes)
        except Exception as exc:
            QMessageBox.critical(self, "Erreur d'écriture", str(exc))
            return
        QMessageBox.information(
            self, "Conversion réussie",
            "{} colonne(s), {} ligne(s) enregistrées dans :\n{}".format(
                len(self.entetes), n, chemin_csv))


def main():
    app = QApplication(sys.argv)
    fenetre = Convertisseur()
    fenetre.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
