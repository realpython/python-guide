.. _install3-linux:

Installing Python 3 on Linux
============================

.. image:: https://farm5.staticflickr.com/4276/34435689480_2e6f358510_k_d.jpg

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

If you are using other Linux distribution, chances are you already have Python 3
pre-installed as well. If not, use your distribution's package manager.
For example on Fedora, you would use `dnf`:

.. code-block:: console

    $ sudo dnf install python3

Note that if the version of the ``python3`` package is not recent enough
for you, there may be ways of installing more recent versions as well,
depending on you distribution. For example installing the ``python36`` package
on Fedora 25 to get Python 3.6. If you are a Fedora user, you might want
to read about `multiple Python versions available in Fedora`_.

.. _multiple Python versions available in Fedora: https://developer.fedoraproject.org/tech/languages/python/multiple-pythons.html


Working with Python 3
---------------------

At this point, you may have system Python 2.7 available as well.

.. code-block:: console

    $ python

This will launch the Python 2 interpreter.

.. code-block:: console

    $ python3

This will launch the Python 3 interpreter.

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

Note that on some Linux distributions including Ubuntu and Fedora the ``pip``
command is meant for Python 2, while the ``pip3`` command is meant for Python 3.

.. code-block:: console

    $ command -v pip3

However, when using virtual environments (described bellow), you don't need to
care about that.


Pipenv & Virtual Environments
-----------------------------

The next step it to install Pipenv, so you can install dependencies and manage virtual environments. 

A Virtual Environment is a tool to keep the dependencies required by different projects
in separate places, by creating virtual Python environments for them. It solves the
"Project X depends on version 1.x but, Project Y needs 4.x" dilemma, and keeps
your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.10 while also
maintaining a project which requires Django 1.8.

So, onward! To the :ref:`Pipenv & Virtual Environments <virtualenvironments-ref>` docs!

--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.

