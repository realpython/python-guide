.. _install3-linux:

Installing Python 3 on Linux
============================

This document describes how to install Python 3.6 on Ubuntu Linux machines.

To see which version of Python 3 you have installed, open a command prompt and run

.. code-block:: console

    $ python3 --version

If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands::

    $ sudo apt-get update
    $ sudo apt-get install python3.6

If you're using another version of Ubuntu (e.g. the latest LTS release), we recommend using the `deadsnakes PPA <https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes>`_ to install Python 3.6::

    $ sudo add-apt-repository ppa:fkrull/deadsnakes
    $ sudo apt-get update
    $ sudo apt-get install python3.6

Working with Python 3
---------------------

At this point, you have the system Python 2.7 available, potentially the
:ref:`Homebrew version of Python 2 <install-osx>` installed, and the Homebrew
version of Python 3 as well.

.. code-block:: console

    $ python

will launch the Python 2 interpreter.

.. code-block:: console

    $ python3


Setuptools & Pip
----------------

The two most crucial third-party Python packages are `setuptools <https://pypi.python.org/pypi/setuptools>`_ and `pip <https://pip.pypa.io/en/stable/>`_.

Once installed, you can download, install and uninstall any compliant Python software
product with a single command. It also enables you to add this network installation
capability to your own Python software with very little work.

Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include
pip by default.

To see if pip is installed, open a command prompt and run

.. code-block:: console

    $ command -v pip

To install pip, `follow the official pip installation guide <https://pip.pypa.io/en/latest/installing/>`_ - this will automatically install the latest version of setuptools.

Virtual Environments
--------------------

A Virtual Environment is a tool to keep the dependencies required by different projects
in separate places, by creating virtual Python environments for them. It solves the
"Project X depends on version 1.x but, Project Y needs 4.x" dilemma, and keeps
your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.10 while also
maintaining a project which requires Django 1.8.

To start using this and see more information: :ref:`Virtual Environments <virtualenvironments-ref>` docs.

You can also use :ref:`virtualenvwrapper <virtualenvwrapper-ref>` to make it easier to
manage your virtual environments.


--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.

