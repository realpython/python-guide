.. _install-osx:

Installing Python on Mac OS X
=============================

The latest version of Mac OS X, Yosemite, **comes with Python 2.7 out of the box**.

You do not need to install or configure anything else to use Python. Having
said that, I would strongly recommend that you install the tools and libraries
described in the next section before you start building Python applications
for real-world use. In particular, you should always install Setuptools, as it
makes it much easier for you to use other third-party Python libraries.

The version of Python that ships with OS X is great for learning but it's not
good for development. The version shipped with OS X may be out of date from the
`official current Python release <https://www.python.org/downloads/mac-osx/>`_,
which is considered the stable production version.

Doing it Right
--------------

Let's install a real version of Python.

Before installing Python, you'll need to install GCC. GCC can be obtained
by downloading `XCode <http://developer.apple.com/xcode/>`_, the smaller
`Command Line Tools <https://developer.apple.com/downloads/>`_ (must have an
Apple account) or the even smaller `OSX-GCC-Installer <https://github.com/kennethreitz/osx-gcc-installer#readme>`_
package.

.. note::
    If you already have XCode installed, do not install OSX-GCC-Installer.
    In combination, the software can cause issues that are difficult to
    diagnose.

While OS X comes with a large number of UNIX utilities, those familiar with
Linux systems will notice one key component missing: a decent package manager.
`Homebrew <http://brew.sh>`_ fills this void.

To `install Homebrew <http://brew.sh/#install>`_, open :file:`Terminal` or
your favorite OSX terminal emulator and run

.. code-block:: console

    $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

The script will explain what changes it will make and prompt you before the
installation begins.
Once you've installed Homebrew, insert the Homebrew directory at the top
of your :envvar:`PATH` environment variable. You can do this by adding the following
line at the bottom of your :file:`~/.profile` file

.. code-block:: console

    export PATH=/usr/local/bin:/usr/local/sbin:$PATH

Now, we can install Python 2.7:

.. code-block:: console

    $ brew install python

This will take a minute or two. 


Setuptools & Pip
----------------

Homebrew installs Setuptools and ``pip`` for you.

Setuptools enables you to download and install any compliant Python
software over a network (usually the Internet) with a single command
(``easy_install``). It also enables you to add this network installation
capability to your own Python software with very little work.

``pip`` is a tool for easily installing and managing Python packages,
that is recommended over ``easy_install``. It is superior to ``easy_install`` in `several ways <https://python-packaging-user-guide.readthedocs.org/en/latest/pip_easy_install.html#pip-vs-easy-install>`_,
and is actively maintained.


Virtual Environments
--------------------

A Virtual Environment is a tool to keep the dependencies required by different projects 
in separate places, by creating virtual Python environments for them. It solves the 
"Project X depends on version 1.x but, Project Y needs 4.x" dilemma, and keeps 
your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.3 while also
maintaining a project which requires Django 1.0.

To start using and see more information: `Virtual Environments <http://github.com/kennethreitz/python-guide/blob/master/docs/dev/virtualenvs.rst>`_ docs. 


--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.
