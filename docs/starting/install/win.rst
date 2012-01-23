Windows
=======

First, download the `latest version <>`_ of Python 2 from the official Website.

The Windows version is provided as an MSI package. To install it manually, just double-click the file. The MSI package format allows Windows administrators to automate installation with their standard tools.

By design, Python installs to a directory with the version number embedded, e.g. ``C:\Python27\``, so that you can have multiple versions of Python on the same system without conflicts. Of course, only one interpreter can be the default application for Python file types. It also does not automatically modify the ``PATH`` environment variable, so that you always have control over which copy of Python is run.

Typing the full path name for a Python interpreter each time quickly gets tedious, so add the directories for your default Python version to the PATH. Assuming that your Python installation is in ``C:\Python27\``, add this to your PATH::

    C:\Python27\;C:\Python27\Scripts\

You can do this easily by running the following in ``powershell``::

    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User")

You do not need to install or configure anything else to use Python. Having said that, I would strongly recommend that you install the tools and libraries described in the next section before you start building Python applications for real-world use. In particular, you should always install Distribute, as it makes it much easier for you to use other third-party Python libraries.

Distribute + Pip
----------------

The most crucial third-party Python software of all is Distribute, which extends the packaging and installation facilities provided by the distutils in the standard library. Once you add Distribute to your Python system you can download and install any compliant Python software product with a single command. It also enables you to add this network installation capability to your own Python software with very little work.

To obtain the latest version of Distribute for Windows, run the python script available here:
  http://python-distribute.org/distribute_setup.py


You'll now have a new command available to you: **easy_install**. It is considered by many to be deprecated, so we will install its replacement: **pip**. Pip allows for uninstallation of packages, and is actively maintained, unlike easy_install.

To install pip, simply open a command prompt and run::

    > easy_install pip


Virtualenv
----------

After Distribute & Pip, the next development tool that you should install is `virtualenv <http://pypi.python.org/pypi/virtualenv/>`_. Use pip::

    > pip install virtualenv

The virtualenv kit provides the ability to create virtual Python environments that do not interfere with either each other, or the main Python installation. If you install virtualenv before you begin coding then you can get into the habit of using it to create completely clean Python environments for each project. This is particularly important for Web development, where each framework and application will have many dependencies.


To set up a new Python environment, change the working directory to where ever you want to store the environment, and run the virtualenv utility in your project's directory::

    > virtualenv --distribute venv

To use an environment, run the ``activate.bat`` batch file in the ``Scripts`` subdirectory of that environment. Your command prompt will change to show the active environment. Once you have finished working in the current virtual environment, run the ``deactivate.bat`` batch file to restore your settings to normal.

Each new environment automatically includes a copy of ``pip`` in the ``Scripts`` subdirectory, so that you can setup the third-party libraries and tools that you want to use in that environment. Put your own code within a subdirectory of the environment, however you wish. When you no longer need a particular environment, simply copy your code out of it, and then delete the main directory for the environment.



--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_, which is available under the same license.
