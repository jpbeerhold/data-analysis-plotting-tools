# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
sys.path.insert(0, os.path.abspath(".."))

project = 'data-analysis-plotting-tools'
copyright = '2024, Ananya Pal, Jannis Philipp Beerhold'
author = 'Ananya Pal, Jannis Philipp Beerhold'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",
    "autoapi.extension",      # Support automatic documentation
    "sphinx.ext.coverage",    # Automatically check if functions are documented
    "sphinx.ext.mathjax",     # Allow support for algebra
    "sphinx.ext.viewcode",    # Include the source code in documentation
    "sphinx.ext.githubpages", # Build for GitHub pages
    "numpydoc",               # Support NumPy style docstrings
    "myst_nb",                # For compiling Jupyter Notebooks into high quality documentation formats  
]

autoapi_dirs = ['../../data_analysis_plotting_tools']

autoapi_ignore = ["*/example.ipynb", "*/usage_example.py"]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_title = 'Data Analysis Plotting Tools'


# do not execute jupyter notebooks when building docs
nb_execution_mode = "off"

# download notebooks as .ipynb and not as .ipynb.txt
html_sourcelink_suffix = ""

suppress_warnings = [
    f"autosectionlabel._examples/{filename.split('.')[0]}"
    for filename in os.listdir("notebooks/")
    if os.path.isfile(os.path.join("notebooks/", filename))
]  # Avoid duplicate label warnings for Jupyter notebooks.

remove_from_toctrees = ["_autosummary/*"]