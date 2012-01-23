Installing Python on Linux
==========================

The latest version of Ubuntu, **comes with Python 2.7 out of the box**.

Distribute & Pip
----------------

The most crucial third-party Python software of all is Distribute, which extends the packaging and installation facilities provided by the distutils in the standard library. Once you add Distribute to your Python system you can download and install any compliant Python software product with a single command. It also enables you to add this network installation capability to your own Python software with very little work.

To obtain the latest version of Distribute for Linux, run the python script available here:
    http://python-distribute.org/distribute_setup.py

The new``easy_install`` command you have available is considered by many to be deprecated, so we will install its replacement: **pip**. Pip allows for uninstallation of packages, and is actively maintained, unlike easy_install.

To install pip, simply open a command prompt and run::

    $ easy_install pip


Virtualenv
----------

After Distribute & Pip, the next development tool that you should install is `virtualenv <http://pypi.python.org/pypi/virtualenv/>`_. Use pip::

    $ pip install virtualenv

The virtualenv kit provides the ability to create virtual Python environments that do not interfere with either each other, or the main Python installation. If you install virtualenv before you begin coding then you can get into the habit of using it to create completely clean Python environments for each project. This is particularly important for Web development, where each framework and application will have many dependencies.

To set up a new Python environment, change the working directory to where ever you want to store the environment, and run the virtualenv utility in your project's directory::

    $ virtualenv --distribute venv

To use an environment, run ``source venv/bin/activate``. Your command prompt will change to show the active environment. Once you have finished working in the current virtual environment, run ``deactivate`` to restore your settings to normal.

Each new environment automatically includes a copy of ``pip``, so that you can setup the third-party libraries and tools that you want to use in that environment. Put your own code within a subdirectory of the environment, however you wish. When you no longer need a particular environment, simply copy your code out of it, and then delete the main directory for the environment.


--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_, which is available under the same license.

