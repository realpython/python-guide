.. _install3-windows:

Installing Python 3 on Windows
==============================

.. image:: https://farm5.staticflickr.com/4276/34435689480_2e6f358510_k_d.jpg

First, follow the installation instructions for `Chocolatey <https://chocolatey.org/install>`_.
It's a community system packager manager for Windows 7+. (It's very much like Homebrew on OSX.)

Once done, installing Python 3 is very simple, because Chocolatey pushes Python 3 as the default.

.. code-block:: console

    choco install python

Once you've run this command, you should be able to launch Python directly from to the console.
(Chocolatey is fantastic and automatically adds Python to your path.)

Setuptools + Pip
----------------

The two most crucial third-party Python packages are `setuptools <https://pypi.python.org/pypi/setuptools>`_ and `pip <https://pip.pypa.io/en/stable/>`_,
which let you download, install and uninstall any compliant Python software
product with a single command. It also enables you to add this network installation
capability to your own Python software with very little work.

All supported versions of Python 3 include pip, so just make sure it's up to date::

    python -m pip install -U pip


Pipenv & Virtual Environments
-----------------------------

The next step is to install Pipenv, so you can install dependencies and manage virtual environments.

A Virtual Environment is a tool to keep the dependencies required by different projects
in separate places, by creating virtual Python environments for them. It solves the
"Project X depends on version 1.x but, Project Y needs 4.x" dilemma, and keeps
your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 2.0 while also
maintaining a project which requires Django 1.8.

So, onward! To the :ref:`Pipenv & Virtual Environments <virtualenvironments-ref>` docs!

--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.
