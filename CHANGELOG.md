# Changelog

Toutes les modifications notables de ce projet sont documentées ici.

Le format suit [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/)
et le projet respecte le [versionnage sémantique](https://semver.org/lang/fr/) (`MAJEUR.MINEUR.CORRECTIF`).

## [2.1.1] - 2026-06-11

### Modifié
- **Downloads** : presets retirés du site (conservés pour le package d'installation) ;
  en-tête des configs reformulé (« An example configuration for a <appareil>, … ») ;
  outil **H5 → CSV rendu portable** (`%~dp0`, plus de dépendance au Bureau) et lançable
  par **double-clic** sur le `.bat`.

## [2.1.0] - 2026-06-11

### Ajouté
- **Page « Downloads »** + carte d'accès sur l'accueil. Fichiers prêts à l'emploi :
  - **Presets** PyMoDAQ (Arduino, RPi 3, RPi Zero) téléchargeables.
  - **Configs en exemples** (`.toml`) affichées en bloc de code *et* téléchargeables,
    avec adresses IP générisées.
  - **Environnement conda** (`Py26env.yml`).
  - **Outil autonome HDF5 → CSV** (`h5_to_csv_gui.py` + `H5_To_CSV.bat`) avec mode d'emploi.

## [2.0.0] - 2026-06-11

Première version **« production »** du wiki Sphinx (refonte complète, développée sur la
branche `dev`).

### Résumé de la refonte v2.0
- Wiki entièrement **re-plateformé en Sphinx** (thème `sphinx_rtd_theme`, identique à la
  documentation officielle PyMoDAQ), rédigé en **anglais**.
- **Deux plugins** documentés depuis les sources : **Raspberry** (unifie les anciens
  Raspberry Pi 3 et Pi Zero) et **Arduino**.
- Identité visuelle (logo, favicon), SEO (canonical, `sitemap.xml`, `robots.txt`) et CI
  GitHub Actions (build Sphinx → GitHub Pages).
- Relecture finale et cohérence vérifiées : build **sans warning**, 12 pages.

## [1.7.0] - 2026-06-11

### Ajouté
- **Identité visuelle** : logo (`logo.svg`) dans la barre latérale et favicon
  (`favicon.svg`), aux couleurs du thème.
- **SEO** : liens **canonical** (via `html_baseurl`), **`sitemap.xml`** (extension
  `sphinx-sitemap`) et **`robots.txt`**.

### Note
- Des redirections des anciennes URLs vanilla (`/Arduino/…`, `/RPI3B/…`, `/RPI0/…`) ont
  été envisagées puis retirées : le préfixe `Arduino/` (majuscule) entre en collision avec
  le nouveau `arduino/` (minuscule) sur les systèmes insensibles à la casse, rendant le
  build **local** non fiable. À réintroduire via une méthode sûre si besoin.

## [1.6.0] - 2026-06-11

### Ajouté
- **Documentation complète du plugin Arduino** (en anglais), combinant les sources du
  plugin et le travail du coéquipier (préservé, traduit et corrigé) — 6 pages `.rst` :
  - *Instruments* : actionneurs FanHeater / LED / LEDwithLCD / Servo, viewers
    PT100 / ADS1115 / Analog, extension ColorSynthesizer.
  - *Experimental setup* : banc thermique Arduino Nano ESP32 (composants, architecture
    client/serveur WiFi, brochage MAX31865 / XY-MOS).
  - *Flashing the Telemetrix firmware* : Arduino IDE, core ESP32 3.3.7, firmware
    Telemetrix4ESP32WIFI, identifiants WiFi, port 31336.
  - *Installing PyMoDAQ and the plugin* : installation utilisateur (Miniforge) et
    développeur.
  - *Using the plugin* : Dashboard, preset (FanHeater Master + viewer Slave, même IP /
    Controller ID), pilotage ventilateur / chauffage, acquisition température.
- **14 images** du montage Arduino récupérées depuis `v1.3.0` (renommées en kebab-case ASCII).

## [1.5.0] - 2026-06-11

### Ajouté
- **Documentation complète du plugin Raspberry** (rédigée depuis les sources, en anglais) :
  - *Instruments* : MoveRasp (actionneur), ViewRasp (viewer 0D), PiCamera (viewer 2D).
  - *Communication* : transport ZeroMQ (DEALER/ROUTER, port 5555) et protocole JSON
    (`scan` / `AQ` / `PI` / `AQ-MULTI` / `PI-MULTI`, enveloppe `ACK`/`ERROR`).
  - *Serveur côté Pi* : architecture en couches (transport → handler → backend),
    installation (I2C + `pigpio`), lancement, mode simulation.
  - *Adaptation à un banc* : `config.py` (actionneurs PWM/DIGITAL, registre de capteurs),
    bancs prêts à l'emploi (défaut + Pi Zero), ajout de pilotes.

## [1.4.0] - 2026-06-11

### Changé (refonte majeure — re-plateformage Sphinx)
- **Le wiki devient un projet Sphinx** utilisant le thème **`sphinx_rtd_theme`**,
  identique à la documentation officielle PyMoDAQ. Le contenu passe en
  **reStructuredText** et en **anglais**.
- Scaffold `docs/source/` : `conf.py`, accueil avec cartes `sphinx_design`, sections
  `arduino/` et `raspberry/`, plus `docs/requirements.txt`.
- **Nouvelle CI** : build `sphinx-build` puis déploiement du HTML généré sur GitHub Pages.

### Retiré
- L'ancien site **vanilla** (`public/` HTML/CSS/JS) et l'outillage Node
  (ESLint/Stylelint/Prettier, `package.json`). Conservé dans l'historique (tag `v1.3.0`).

### À venir
- Fusion des plugins Raspberry Pi 3 + Pi Zero en un plugin **Raspberry** unique et mise à
  jour du plugin **Arduino**, documentés depuis les sources (sprints suivants).

## [1.3.0] - 2026-06-09

### Ajouté
- **Documentation Arduino étoffée** (contribution équipe) : nouvelles pages *Firmware &
  Configuration*, *Installation PyMoDAQ* et *État d'avancement*, refonte de la page de
  présentation Arduino, le tout intégré à la navigation partagée (`NAV_GROUPS`).
- **Lightbox** : clic sur une figure (`.figure-img`) pour l'agrandir en superposition
  (overlay, bouton de fermeture, fermeture au clic extérieur et à Échap).

### Corrigé / Amélioré
- **Lightbox accessible au clavier** : figures focusables (`tabindex`/`role`), ouverture
  par Entrée/Espace, focus déplacé sur le bouton de fermeture puis **restauré** à la
  fermeture.
- Correction d'une **fuite d'écouteur `keydown`** (désormais retiré quel que soit le mode
  de fermeture de la lightbox).
- **`sitemap.xml`** complété avec les trois nouvelles pages Arduino.

## [1.2.5] - 2026-06-04

### Corrigé
- **Lint CI au vert** : 41 erreurs Stylelint corrigées dans `style.css` — notation de
  couleur moderne (`rgb(r g b / X%)`), alpha en pourcentage, `font-family` sans
  guillemets superflus (`Inter`), shorthands non redondants, propriété `inset`, et
  suppression d'une ligne vide avant déclaration. Plus 2 avertissements ESLint réglés
  (`catch` sans liaison `e` inutilisée dans `script.js`).

## [1.2.4] - 2026-06-04

### Ajouté
- **Bouton « Retour accueil » en mode rail** : quand il est présent (sur les sous-pages),
  il s'affiche désormais sous forme d'**icône maison** centrée lorsque la barre est
  réduite, au lieu d'être masqué. En mode ouvert, il garde son libellé « ← Retour Accueil ».

## [1.2.3] - 2026-06-04

### Corrigé
- **État de la barre latérale incohérent en navigation** : la barre s'ouvrait/se fermait
  selon la page faute de préférence mémorisée (défaut « accueil ouvert / autres réduites »).
  Le défaut par page est supprimé : l'état n'est désormais piloté **que par la mémoire**
  (`localStorage`). Seule exception : à la **toute première visite** (aucune préférence),
  la barre est **ouverte**. Ensuite l'état est identique sur toutes les pages et ne change
  qu'au clic de l'utilisateur. Logique alignée entre le script inline (anti-clignotement)
  et `script.js`.

## [1.2.2] - 2026-06-04

### Ajouté
- **Barre réduite (rail)** : deux séparateurs (`.rail-divider`) ajoutés pour structurer
  l'affichage — sous le bouton d'ouverture et sous le nom du projet. Organisation finale
  de haut en bas : bouton → séparateur → nom → séparateur → boutons des 3 plugins →
  grand espace → séparateur + version. Séparateurs visibles uniquement en mode rail.

## [1.2.1] - 2026-06-04

### Modifié
- **Barre latérale réduite (rail)** : le pied de barre est conservé pour **garder la
  version courante affichée en bas** même en mode réduit ; seul le texte
  « Lycée Edouard Branly / Session 2026 » est masqué dans ce mode, pour une organisation
  proche de la barre ouverte.

## [1.2.0] - 2026-06-04

### Modifié
- **Refonte complète de l'accueil** (`index.html`), plus simple et orienté utilisateur :
  - Retrait de la pastille « E6 IR ».
  - Nouveau hero : H1 **« Wiki Plugins DAP Pymodaq »** + mention du nom de code court
    **« DAP Pymodaq »** (celui affiché dans la barre de gauche) et de l'objectif
    (migration LabVIEW → PyMODAQ). Trois informations clés en pastilles.
  - **3 cartes plugins cliquables** (Arduino, RPi 3, RPi Zero) avec liens directs vers
    leur documentation — l'utilisateur n'a plus besoin de la barre de gauche.
  - Contexte « Le projet en bref » condensé ; sections denses (tableau technique,
    organisation de l'équipe) déplacées dans des blocs **repliables** (`<details>`).

## [1.1.0] - 2026-06-04

### Ajouté
- **Barre latérale rétractable** (mode « rail ») : un bouton replie la barre en une
  version étroite (~72 px) qui reste visible, avec des icônes de groupe (ARD / RP3 / RP0)
  cliquables menant directement à chaque plugin. Le contenu s'élargit en conséquence.
- État par défaut selon la page (`data-page`) : **accueil ouverte**, autres pages
  **réduites**. Le choix de l'utilisateur est **mémorisé** (`localStorage`) et surcharge
  le défaut. Script inline anti-clignotement appliquant l'état avant le premier rendu.

### Notes
- Le mode rail est un comportement **desktop** (≥ 769 px) ; en mobile, la barre conserve
  son tiroir off-canvas et le bouton hamburger. Transitions désactivées si
  `prefers-reduced-motion`.

## [1.0.0] - 2026-06-04

Première version « production ».

### Ajouté
- **SEO** par page : `meta description`, balises **Open Graph** (`og:*`), lien
  **canonical** (URL absolue) et `theme-color`.
- **`favicon.svg`** (motif de signal d'acquisition, aux couleurs du thème).
- **`sitemap.xml`** et **`robots.txt`** (base `https://wiki-plugins-dap-pymodaq.github.io`).

### Modifié
- **Performance** : `loading="lazy"` ajouté sur toutes les images de contenu.
- Documentation racine actualisée (déploiement « production », section SEO).

## [0.4.1] - 2026-06-04

### Corrigé
- La note de version ne s'affichait pas à l'ouverture en `file://` (double-clic), car
  `fetch('version.json')` est bloqué par le navigateur pour les fichiers locaux. Ajout
  d'une **version de repli** (`FALLBACK_VERSION`) affichée immédiatement, puis remplacée
  par la valeur canonique de `version.json` dès que le site est servi en HTTP (serveur
  local ou GitHub Pages).

## [0.4.0] - 2026-06-04

### Ajouté
- **Version courante affichée** en pied de barre latérale, lue dynamiquement depuis
  `public/version.json` (`loadVersion`).
- **Notifications (toasts)** accessibles (`role="status"`, `aria-live`) en remplacement
  de `alert()` pour le retour de copie.
- **Accessibilité** : lien d'évitement (« skip-link ») vers le contenu (`#contenu`),
  `aria-label` sur la navigation, `aria-current="page"` sur le lien actif,
  `aria-expanded` sur les groupes du menu, prise en compte de `prefers-reduced-motion`.

### Modifié
- **Suppression de tous les styles inline** (~93 occurrences) : externalisés en classes
  CSS réutilisables (utilitaires d'espacement, `figure-img`/`figure-caption`,
  `sub-list`, `cmd-text`, variantes d'info-box, etc.).
- **Boutons « Copier »** : handlers `onclick` inline remplacés par une délégation
  d'événements dans `script.js` (plus aucun handler inline dans le HTML).
- `<main>` doté d'un `id="contenu"` (cible du skip-link).

## [0.3.0] - 2026-06-04

### Ajouté
- **Coquille partagée (DRY)** : la barre latérale (sidebar), le bouton de menu mobile et
  l'overlay sont désormais injectés depuis une **source unique** (`NAV_GROUPS` dans
  `script.js`) au lieu d'être dupliqués dans chaque page HTML.
- Attributs `data-base` (chemin relatif vers la racine) et `data-page` (clé de la page
  active) portés par `<html>` : les liens et le lien actif sont calculés automatiquement,
  ce qui supprime durablement la classe de bugs des hotfixes v0.0.1.
- Logo cliquable (retour à l'accueil) et règles CSS associées (`a.logo`, `.sidebar-back`).

### Modifié
- Les contrôles de la coquille (menu, overlay, menu arborescent) utilisent
  `addEventListener` au lieu de handlers `onclick` inline.
- `script.js` restructuré autour de l'injection de la coquille (`injectShell`,
  `buildSidebar`) ; `buildTOC` conservé (table des matières + scroll-spy).

## [0.2.0] - 2026-06-04

### Ajouté
- **CI/CD** : workflow GitHub Actions (`.github/workflows/deploy.yml`) qui lint le code
  (ESLint + Stylelint, informatif) puis publie `public/` sur GitHub Pages à chaque push
  sur `main` (Source : « GitHub Actions »).
- `.gitattributes` (normalisation des fins de ligne en LF).

## [0.1.0] - 2026-06-04

### Ajouté
- Séparation `public/` (web) et racine (outillage/docs) : `index.html`, `style.css`,
  `script.js` et les dossiers `Arduino/`, `RPI3B/`, `RPI0/` déplacés sous `public/`.
- Configuration des linters : ESLint (`eslint.config.js`), Stylelint
  (`.stylelintrc.json`) et Prettier (`.prettierrc.json`, `.prettierignore`).
- `package.json` (scripts de lint/format, dépendances de développement).
- `.gitignore` (dépendances, secrets, OS, IDE).
- `public/.nojekyll` (désactive le traitement Jekyll de GitHub Pages).
- `public/version.json` (version courante).
- Documentation racine : `README.md` complet, `ARCHITECTURE.md`, `SPRINTS.md` et ce
  `CHANGELOG.md`.

## [0.0.1] - 2026-06-04

### Corrigé
- **Navigation** : le lien « Plugins Arduino » de la page d'accueil pointait vers
  `RPI0/presentation.html` (inexistant) au lieu de `Arduino/presentation.html`.
- **Navigation** : le groupe « Plugins Arduino » était vide dans plusieurs pages
  (RPi 3 et RPi Zero) ; ajout du sous-lien manquant.
- **Branding** : le `<title>` de la page Arduino indiquait « RPi 3 » par erreur ; le
  `<title>` de `rpi3_install.html` contenait un `&` non échappé.

### Modifié
- **Branding** unifié sur les 7 pages : logo harmonisé (`PyMoDAQ`/`PyDAP` →
  `DAP Pymodaq` + sous-titre « Wiki Plugins · BTS CIEL 2026 ») et titres normalisés en
  « … — Wiki Plugins DAP Pymodaq ».
