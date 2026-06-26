# Sprints — Wiki Plugins DAP Pymodaq

Chaque sprint livre **une fonctionnalité** complète et vérifiée. Le backlog est aligné
sur les habitudes de programmation du portfolio de référence (séparation `public/`,
outillage lint/format, CI/CD, coquille partagée DRY, SEO/accessibilité).

Légende : ✅ terminé · 🚧 en cours · ⬜ à faire

---

## 🔄 Refonte « v2.0 » — Re-plateformage Sphinx (terminée — v2.0.0)

Direction validée le 2026-06-11 : le wiki passe d'un site **vanilla** à un projet
**Sphinx** au thème officiel PyMoDAQ (`sphinx_rtd_theme`), rédigé en **anglais** (`.rst`),
avec **2 plugins** (Arduino + Raspberry unifié).

- ✅ **Sprint 7 — Scaffold Sphinx (v1.4.0)** : projet `docs/` (thème RTD + `sphinx_design`),
  accueil à 2 cartes, nouvelle CI build/deploy, retrait du site vanilla. Vérifié en
  navigateur (rendu identique à l'officiel).
- ✅ **Sprint 8 — Doc Raspberry (v1.5.0)** : contenu complet depuis les sources (instruments
  MoveRasp / ViewRasp / PiCamera, protocole ZMQ/JSON, serveur côté Pi, adaptation banc).
  5 pages `.rst`, build sans warning, rendu vérifié en navigateur.
- ✅ **Sprint 9 — Doc Arduino (v1.6.0)** : pages du coéquipier préservées, traduites EN et
  corrigées depuis les sources (instruments, setup, firmware, installation, usage).
  6 pages `.rst` + 14 images récupérées, build sans warning, rendu vérifié.
- ✅ **Sprint 10 — Polish (v1.7.0)** : logo + favicon, SEO (canonical via `html_baseurl`,
  `sitemap.xml` via `sphinx-sitemap`, `robots.txt`). Redirections des anciennes URLs
  retirées (collision de casse `Arduino/` vs `arduino/`). Build sans warning, vérifié.
- ✅ **Sprint 11 — Finalisation (v2.0.0)** : relecture/cohérence, docs racine à jour,
  build sans warning (12 pages), tag **production v2.0.0**.
- ✅ **Sprint 12 — Téléchargements (v2.1.0)** : page « Downloads » + carte accueil
  (presets, configs en exemples, env conda, outil H5→CSV). Build sans warning, vérifié.
- ✅ **Sprint 13 — Package d'installation clé-en-main (v2.2.0)** : `install-dap-pymodaq.zip`
  (Install.bat double-clic autonome `%~dp0\files`, plugin Raspberry **unifié** + Arduino,
  configs + presets + sources plugins, README). Section sur la page Downloads. ⚠️ Installeur
  et preset Raspberry adapté **non testés** (pas de conda/PyMoDAQ ici) — à valider.

Reste à merger `dev` → `main` et pousser (manuel, par l'utilisateur).

> L'historique ci-dessous documente la version **vanilla** (v0.0.1 → v1.3.0), conservée
> pour mémoire.

---

## ✅ v0.0.1 — Hotfixes navigation & branding
Trois correctifs livrés en commits séparés :
- **FIX-1** — lien Arduino cassé sur l'accueil (`RPI0/presentation.html` →
  `Arduino/presentation.html`).
- **FIX-2** — unification du logo et des titres en « Wiki Plugins DAP Pymodaq » (7 pages),
  correction du `<title>` Arduino erroné et du `&` non échappé.
- **FIX-3** — sous-lien Arduino manquant ajouté dans les sidebars RPi 3 / RPi Zero.

## ✅ Sprint 0 — Fondations & outillage (v0.1.0)
Restructuration en `public/`, configuration des linters (ESLint/Stylelint/Prettier),
`package.json`, `.gitignore`, `.nojekyll`, `version.json`, et documentation racine
(README, ARCHITECTURE, CHANGELOG, SPRINTS).

## ✅ Sprint 1 — CI/CD GitHub Actions (v0.2.0)
Workflow `.github/workflows/deploy.yml` : job `lint` (ESLint + Stylelint, informatif)
puis job `deploy` publiant `public/` sur GitHub Pages (Source : « GitHub Actions »).
Ajout de `.gitattributes` (normalisation LF).

## ✅ Sprint 2 — Coquille partagée / DRY (v0.3.0)
Sidebar (+ bouton menu mobile et overlay) injectée depuis une **source unique**
(`NAV_GROUPS` dans `script.js`), suppression de la duplication dans chaque page.
Chemins relatifs paramétrés (`data-base`) et lien actif via `data-page`. Contrôles
câblés en `addEventListener`. Résorbe durablement les incohérences de navigation
(cause des hotfixes v0.0.1). Vérifié en navigateur (accueil + sous-page).

## ✅ Sprint 3 — Qualité du code & accessibilité (v0.4.0)
Externalisation des ~93 styles inline → classes CSS (`kebab-case`), remplacement des
handlers `onclick` inline par une délégation d'événements, remplacement de `alert()` par
un toast accessible, version affichée en pied de sidebar (`version.json`), skip-link,
`aria-label`/`aria-current`/`aria-expanded`, `prefers-reduced-motion`. Vérifié en
navigateur. *Note : la validation `npm run lint` (ESLint/Stylelint) nécessite Node et
s'exécute en CI ; le CSS pré-existant peut encore générer des avertissements Stylelint à
traiter quand Node sera disponible.*

## ✅ Sprint 4 — SEO & performance (v1.0.0)
Par page : `description`, Open Graph, `canonical`, `theme-color` ; `favicon.svg`,
`sitemap.xml`, `robots.txt` ; `loading="lazy"` sur toutes les images. Première version
« production », tag Git `v1.0.0`.

## ✅ Sprint 5 — Barre latérale rétractable (v1.1.0)
La barre se replie en mode « rail » étroit (~72 px) qui reste visible (icônes de groupe
cliquables vers chaque plugin). État par défaut selon la page (accueil ouverte, autres
réduites), choix mémorisé en `localStorage`, anti-clignotement par script inline.
Comportement desktop ; mobile inchangé (tiroir off-canvas). Vérifié en navigateur.

## ✅ Sprint 6 — Refonte de l'accueil + liens plugins (v1.2.0)
Réécriture de `index.html` : retrait de la pastille « E6 », nouveau hero clair (H1
« Wiki Plugins DAP Pymodaq », mention du nom court « DAP Pymodaq »), 3 cartes plugins
cliquables avec liens directs vers les docs, contexte simplifié et sections denses
(tableau, équipe) repliées dans des `<details>`. Vérifié en navigateur.

---

### Récapitulatif par version

| Version | Livrable                                   | Statut |
| ------- | ------------------------------------------ | ------ |
| v0.0.1  | Hotfixes navigation & branding             | ✅     |
| v0.1.0  | Sprint 0 — Fondations & outillage          | ✅     |
| v0.2.0  | Sprint 1 — CI/CD GitHub Actions            | ✅     |
| v0.3.0  | Sprint 2 — Coquille partagée (DRY)         | ✅     |
| v0.4.0  | Sprint 3 — Qualité code & accessibilité    | ✅     |
| v1.0.0  | Sprint 4 — SEO, performance, production    | ✅     |
| v1.1.0  | Sprint 5 — Barre latérale rétractable      | ✅     |
| v1.2.0  | Sprint 6 — Refonte de l'accueil            | ✅     |
