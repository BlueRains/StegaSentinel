import sys
from pathlib import Path

# Go to the upper level
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "StegaSentinel"
copyright = "%Y, Lu Schoevaars"
author = "Lu Schoevaars"
release = "0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.apidoc",
    "sphinx.ext.duration",
    "sphinx.ext.intersphinx"
]

templates_path = ["_templates"]
exclude_patterns = []

apidoc_modules = [
    {
        "path": "../../analyser",
        "destination": "analyser",
        "module_first": True,
        "implicit_namespaces": True,
        "automodule_options": {
            "synopsis analyse incoming attachments",
            "members",
            "show-inheritance",
            "undoc-members",
            "member-order",
        },
    },
    {
        "path": "../../connector",
        "destination": "connector",
        "module_first": True,
        "automodule_options": {
            "synopsis connect email and analyser",
            "members",
            "show-inheritance",
            "undoc-members",
        },
    },
]
nitpicky = True

# -- Options for markup

default_role = "py:obj" # Make `filter` refer to python function filter

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]
