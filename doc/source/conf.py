#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PHATE documentation build configuration file, created by
# sphinx-quickstart on Thu Mar 30 19:50:14 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import glob
import shutil

root_dir = os.path.abspath(os.path.join(os.path.dirname(
    __file__), '..', '..'))
sys.path.insert(0, root_dir)
# print(sys.path)

# Copy ipython notebooks
dest_dir = "examples"
for file in glob.glob(os.path.join(root_dir, 'examples', '*.ipynb')):
    print("Copy {} to {}".format(file, dest_dir))
    shutil.copy(file, dest_dir)

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.napoleon',
              'sphinx.ext.doctest',
              'sphinx.ext.coverage',
              'sphinx.ext.viewcode',
              'nbsphinx',
              'sphinx.ext.mathjax',
              'autodocsumm',
              'IPython.sphinxext.ipython_console_highlighting']

autodoc_mock_imports = ["h5py", "tables", "rpy2", "fcsparser"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['ytemplates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst', '.ipynb']

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'scprep'
copyright = '2018 Krishnaswamy Lab, Yale University'
author = 'Scott Gigante, Jay Stanley, Daniel Burkhardt'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
version_py = os.path.join(root_dir, 'scprep', 'version.py')
# The full version, including alpha/beta/rc tags.
release = open(version_py).read().strip().split(
    '=')[-1].replace('"', '').strip()
# The short X.Y version.
version = release.split('-')[0]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['ystatic']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'scprepdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'scprep.tex', 'scprep Documentation',
     'Scott Gigante, Jay Stanley, Daniel Burkhardt', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'scprep', 'scprep Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'scprep', 'scprep Documentation',
     author, 'scprep', 'One line description of project.',
     'Miscellaneous'),
]

nbsphinx_execute = "always"
nbsphinx_timeout = 180

nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        | This page was generated from `{{ docname }}`__ by nbsphinx_.
        | Interactive version:
          :raw-html:`<a href="https://mybinder.org/v2/gh/KrishnaswamyLab/scprep/{{ env.config.release }}?filepath={{ docname }}"><img alt="Run in Binder" src="https://mybinder.org/badge.svg" style="vertical-align:text-bottom"></a>`
          :raw-html:`<a href="https://colab.research.google.com/github/KrishnaswamyLab/scprep/blob/{{ env.config.release }}/{{ docname }}"><img alt="Run in Colab" src="https://colab.research.google.com/assets/colab-badge.svg" style="vertical-align:text-bottom"></a>`

    __ https://github.com/KrishnaswamyLab/scprep/blob/
        {{ env.config.release }}/{{ docname }}

      .. _nbsphinx: http://nbsphinx.readthedocs.io/.

.. raw:: latex

    \vfil\penalty-1\vfilneg
    \vspace{\baselineskip}
    \textcolor{gray}{The following section was generated from
    \texttt{\strut{}{{ docname }}}\\[-0.5\baselineskip]
    \noindent\rule{\textwidth}{0.4pt}}
    \vspace{-2\baselineskip}
"""
