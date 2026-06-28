# Wiki Plugins DAP Pymodaq

Technical wiki documenting the **PyMoDAQ** plugins developed as part of the
**DAP** project (BTS CIEL, Lycée Edouard Branly, in partnership with **CETHIL**): the
**Arduino** plugin and the **Raspberry** plugin (which unifies the former Raspberry Pi 3
and Pi Zero setups).

A **Sphinx documentation** site using the **`sphinx_rtd_theme`** theme — the same one
used by the official PyMoDAQ documentation (<https://pymodaq.cnrs.fr>) — written in
**English** and deployed on **GitHub Pages**.

## Overview

Documentation split into two sections, one per plugin:

- **Arduino plugin** — instruments built around an Arduino / ESP32 board (Telemetrix-ESP32):
  multicolor LED, fan/heater, analog and PT100 / ADS1115 acquisition, Dashboard
  extension.
- **Raspberry plugin** — control of an experimental setup via a Raspberry Pi: a
  PyMoDAQ actuator and detector communicating with a server embedded on the Pi via
  ZeroMQ.

## AI Disclosure

This wiki was designed and developed with the help of artificial intelligence tools,
used as genuine **productivity tools**. This is a deliberate choice: AI is now an
integral part of the developer profession and today's job market, and we choose to
**adapt to it and master it** rather than ignore it.

What makes the difference is the **usage**. We **research these tools in depth** in
order to use them with discernment, as a genuine productivity lever. AI speeds up
implementation — it replaces neither the design, nor the technical decisions, nor the
understanding of the code. The **vast majority of the features** and the **technical
stack** used here are familiar to us: we know what was built, why, and how to evolve
and maintain it.

Concretely, a project of this scope normally represents **3 to 5 weeks of full-time
work** (i.e. several months alongside our studies). By leveraging AI, we completed it
in a fraction of that time, focusing our energy on **architecture**, **quality**, and
**details** rather than repetitive tasks — exactly the productivity gain sought in a
modern work environment.

## Project Structure

```
wiki-plugins-dap-pymodaq/
├── docs/
│   ├── requirements.txt          # Sphinx dependencies (sphinx, rtd-theme, design)
│   └── source/
│       ├── conf.py               # Sphinx configuration (theme, version, language)
│       ├── index.rst             # Home page (cards linking to the 2 plugins)
│       ├── _static/css/          # Supplementary CSS
│       ├── arduino/              # Arduino plugin documentation
│       └── raspberry/            # Raspberry plugin documentation
├── .github/workflows/deploy.yml  # CI: Sphinx build + GitHub Pages deployment
├── ARCHITECTURE.md               # Technical choices and organization
├── CHANGELOG.md                  # Version history
├── SPRINTS.md                    # Backlog and progress by sprint
└── README.md
```

See [ARCHITECTURE.md](ARCHITECTURE.md) for details on technical choices.

## Building the Wiki Locally

Requirement: **Python 3**.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux / macOS:
# source .venv/bin/activate

pip install -r docs/requirements.txt
sphinx-build -b html docs/source docs/_build/html

# Preview:
python -m http.server 8000 --directory docs/_build/html
# → http://localhost:8000
```

## Deployment

Deployment is **automatic**: every push to `main` triggers the GitHub Actions workflow
([.github/workflows/deploy.yml](.github/workflows/deploy.yml)), which **builds the
Sphinx site** and then publishes it to GitHub Pages.

> ℹ️ Prerequisite (one-time setup): in the repository's **Settings → Pages**, select
> **"GitHub Actions"** as the source.

## Workflow and Versioning

- The project progresses in **sprints** (1 sprint = 1 feature), tracked in
  [SPRINTS.md](SPRINTS.md).
- We **commit directly to `main`**; a **Git tag** (`vX.Y.Z`) is set for each published
  version.
- Semantic versioning `MAJOR.MINOR.PATCH`. The current version is defined in
  [docs/source/conf.py](docs/source/conf.py) (`version` / `release`) and tracked in
  [CHANGELOG.md](CHANGELOG.md).
- Root-level documentation files are updated **at every sprint**.
