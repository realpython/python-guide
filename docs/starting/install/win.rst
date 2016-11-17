.. _install-windows:

Installing Python on Windows
============================

First, download the `latest version <https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi>`_
of Python 2.7 from the official Website. If you want to be sure you are installing a fully
up-to-date version, click the Downloads > Windows link from the home page of the
`Python.org web site <http://python.org>`_ .

The Windows version is provided as an MSI package. To install it manually, just
double-click the file. The MSI package format allows Windows administrators to
automate installation with their standard tools.

By design, Python installs to a directory with the version number embedded,
e.g. Python version 2.7 will install at :file:`C:\\Python27\\`, so that you can
have multiple versions of Python on the
same system without conflicts. Of course, only one interpreter can be the
default application for Python file types. It also does not automatically
modify the :envvar:`PATH` environment variable, so that you always have control over
which copy of Python is run.

Typing the full path name for a Python interpreter each time quickly gets
tedious, so add the directories for your default Python version to the :envvar:`PATH`.
Assuming that your Python installation is in :file:`C:\\Python27\\`, add this to your
:envvar:`PATH`:

.. code-block:: console

    C:\Python27\;C:\Python27\Scripts\

You can do this easily by running the following in ``powershell``:

.. code-block:: console

    [Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27\;C:\Python27\Scripts\", "User")

The second (:file:`Scripts`) directory receives command files when certain
packages are installed, so it is a very useful addition.
You do not need to install or configure anything else to use Python. Having
said that, I would strongly recommend that you install the tools and libraries
described in the next section before you start building Python applications for
real-world use. In particular, you should always install Setuptools, as it
makes it much easier for you to use other third-party Python libraries.

Setuptools + Pip
----------------

The most crucial third-party Python software of all is Setuptools, which
extends the packaging and installation facilities provided by the distutils in
the standard library. Once you add Setuptools to your Python system you can
download and install any compliant Python software product with a single
command. It also enables you to add this network installation capability to
your own Python software with very little work.

To obtain the latest version of Setuptools for Windows, run the Python script
available here: `ez_setup.py <https://bootstrap.pypa.io/ez_setup.py>`_


You'll now have a new command available to you: **easy_install**. It is
considered by many to be deprecated, so we will install its replacement:
**pip**. Pip allows for uninstallation of packages, and is actively maintained,
unlike easy_install.

To install pip, run the Python script available here:
`get-pip.py <https://raw.github.com/pypa/pip/master/contrib/get-pip.py>`_


Virtual Environments
--------------------

A Virtual Environment is a tool to keep the dependencies required by different projects 
in separate places, by creating virtual Python environments for them. It solves the 
"Project X depends on version 1.x but, Project Y needs 4.x" dilemma, and keeps 
your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.10 while also
maintaining a project which requires Django 1.8.

To start using this and see more information: :ref:`Virtual Environments <virtualenvironments-ref>` docs. 


--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.
