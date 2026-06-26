# Configuration file for the Sphinx documentation builder.
# Wiki of the DAP PyMoDAQ plugins (Arduino, Raspberry).
# Same theme as the official PyMoDAQ documentation: sphinx_rtd_theme.

# -- Project information -----------------------------------------------------
project = 'DAP Pymodaq Plugins'
author = 'BTS CIEL - Lycee Edouard Branly'
copyright = '2026, BTS CIEL - Lycee Edouard Branly'

version = '2.1.1'
release = '2.1.1'

language = 'en'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx_design',          # cards / grids / tabs (used by the official docs)
    'sphinx_sitemap',          # generates sitemap.xml
    'sphinx.ext.githubpages',  # writes .nojekyll for GitHub Pages
]

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output (identical theme to https://pymodaq.cnrs.fr) ----------------
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
}
html_logo = '_static/logo.svg'
html_favicon = '_static/favicon.svg'
html_static_path = ['_static']
html_css_files = ['css/custom.css']
html_extra_path = ['_extra']

# -- SEO ---------------------------------------------------------------------
# Canonical URLs (added by the theme from html_baseurl) and sitemap generation.
html_baseurl = 'https://wiki-plugins-dap-pymodaq.github.io/'
sitemap_url_scheme = '{link}'
