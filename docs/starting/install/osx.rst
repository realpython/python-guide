.. _install-osx:

Installing Python 2 on Mac OS X
===============================

.. image:: https://farm5.staticflickr.com/4268/34435688560_4cc2a7bcbb_k_d.jpg

.. note::
    Check out our :ref:`guide for installing Python 3 on OS X<install3-osx>`.

The latest version of Mac OS X, High Sierra, **comes with Python 2.7 out of the box**.

You do not need to install or configure anything else to use Python. Having said
that, I would strongly recommend that you install the tools and libraries
described in the next section before you start building Python applications for
real-world use. In particular, you should always install Setuptools, as it makes
it much easier for you to install and manage other third-party Python libraries.

The version of Python that ships with OS X is great for learning, but it's not
good for development. The version shipped with OS X may be out of date from the
`official current Python release <https://www.python.org/downloads/mac-osx/>`_,
which is considered the stable production version.

Doing it Right
--------------

Let's install a real version of Python.

Before installing Python, you'll need to install a C compiler. The fastest way
is to install the Xcode Command Line Tools by running
``xcode-select --install``. You can also download the full version of
`Xcode <http://developer.apple.com/xcode/>`_ from the Mac App Store, or the
minimal but unofficial
`OSX-GCC-Installer <https://github.com/kennethreitz/osx-gcc-installer#readme>`_
package.

.. note::
    If you already have XCode installed, do not install OSX-GCC-Installer.
    In combination, the software can cause issues that are difficult to
    diagnose.

.. note::
    If you perform a fresh install of XCode, you will also need to add the
    commandline tools by running ``xcode-select --install`` on the terminal.


While OS X comes with a large number of UNIX utilities, those familiar with
Linux systems will notice one key component missing: a decent package manager.
`Homebrew <http://brew.sh>`_ fills this void.

To `install Homebrew <http://brew.sh/#install>`_, open :file:`Terminal` or
your favorite OSX terminal emulator and run

.. code-block:: console

    $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

The script will explain what changes it will make and prompt you before the
installation begins.
Once you've installed Homebrew, insert the Homebrew directory at the top
of your :envvar:`PATH` environment variable. You can do this by adding the following
line at the bottom of your :file:`~/.profile` file

.. code-block:: console

    export PATH="/usr/local/bin:/usr/local/sbin:$PATH"

Now, we can install Python 2.7:

.. code-block:: console

    $ brew install python@2

Because ``python@2`` is a "keg", we need to update our ``PATH`` again, to point at our new installation:

.. code-block:: console

    export PATH="/usr/local/opt/python@2/libexec/bin:$PATH"

Homebrew names the executable ``python2`` so that you can still run the system Python via the executable ``python``.


.. code-block:: console

    $ python -V   # Homebrew installed Python 3 interpreter (if installed)
    $ python2 -V  # Homebrew installed Python 2 interpreter
    $ python3 -V  # Homebrew installed Python 3 interpreter (if installed)


Setuptools & Pip
----------------

Homebrew installs Setuptools and ``pip`` for you.

Setuptools enables you to download and install any compliant Python
software over a network (usually the Internet) with a single command
(``easy_install``). It also enables you to add this network installation
capability to your own Python software with very little work.

``pip`` is a tool for easily installing and managing Python packages,
that is recommended over ``easy_install``. It is superior to ``easy_install``
in `several ways <https://python-packaging-user-guide.readthedocs.io/pip_easy_install/#pip-vs-easy-install>`_,
and is actively maintained.

.. code-block:: console

    $ pip2 -V  # pip pointing to the Homebrew installed Python 2 interpreter
    $ pip -V  # pip pointing to the Homebrew installed Python 3 interpreter (if installed)



Virtual Environments
--------------------

A Virtual Environment (commonly referred to as a 'virtualenv') is a tool to keep the dependencies required by different projects
in separate places, by creating virtual Python environments for them. It solves the
"Project X depends on version 1.x but, Project Y needs 4.x" dilemma, and keeps
your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.10 while also
maintaining a project which requires Django 1.8.

To start using this and see more information: :ref:`Virtual Environments <virtualenvironments-ref>` docs.

--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.
