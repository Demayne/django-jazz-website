# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import django

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

def setup_django():
    """
    Set up the Django environment for the Sphinx documentation builder.
    This function modifies the system path and sets the environment variable
    for Django settings module, then initializes Django.
    """
    # Get the directory of the current file (conf.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Get the parent directory of 'docs', which should be the root of your project
    project_root = os.path.abspath(os.path.join(current_dir, '..'))

    # Add the project root to the Python path
    sys.path.insert(0, project_root)

    # Add the mySite directory to the Python path
    mySite_dir = os.path.join(project_root, 'mySite')
    sys.path.insert(0, mySite_dir)

    # Set the Django settings module
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mySite.settings'

    # Set up Django
    django.setup()

# Initialize Django setup
setup_django()

project = 'Django Consolidation Capstone'
copyright = '2024, Demayne'
author = 'Demayne'
release = '00.00.01'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Extensions to include in the Sphinx build process
extensions = []

# Paths that contain templates, relative to this directory
templates_path = ['_templates']

# Patterns to exclude from the build process
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Theme to use for HTML and HTML Help pages
html_theme = 'alabaster'

# Paths that contain custom static files, relative to this directory
html_static_path = ['_static']
