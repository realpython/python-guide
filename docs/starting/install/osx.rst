.. _install-osx:

Installing Python on Mac OS X
=============================

The latest version of Mac OS X, Mountain Lion, **comes with Python 2.7 out of the box**.

You do not need to install or configure anything else to use Python. Having
said that, I would strongly recommend that you install the tools and libraries
described in the next section before you start building Python applications
for real-world use. In particular, you should always install Distribute, as it
makes it much easier for you to use other third-party Python libraries.

The version of Python that ships with OS X is great for learning, but it's not
good for development. It's slightly out of date, and Apple has made significant
changes that can cause hidden bugs.

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

While Lion comes with a large number of UNIX utilities, those familiar with
Linux systems will notice one key component missing: a decent package manager.
`Homebrew <http://mxcl.github.com/homebrew/>`_ fills this void.

To `install Homebrew <https://github.com/mxcl/homebrew/wiki/installation>`_,
simply run

.. code-block:: console

    $ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

The script will explain what changes it will make and prompt you before the
installation begins.

.. code-block:: console

    $ brew doctor

will analyse the setup and give hints which steps you might have missed.
 
Once you've installed Homebrew, move the Homebrew directory to the top
of your ``PATH`` environment variable. You can do this either globaly 
by editing ``/etc/paths``, e.g. by 

.. code-block:: console

    $ sudo nano /etc/paths

and writing the last line first or by adding

.. code-block:: console

    export PATH=/usr/local/bin:$PATH

to ``~/.bash_profile``. This is tested with OS X 10.8.5.
Rumor has it that on OS X 10.4 / 10.5 / 10.6 this line should go to ~/.profile, 
but this is not tested. 

Now, we can install Python 2.7: ::

    $ brew install python

This will take a minute or two. Once that's complete, you'll have to add the
new Python scripts directory to your ``PATH``

.. code-block:: console

    export PATH=/usr/local/share/python:$PATH


Distribute & Pip
----------------

The most crucial third-party Python software of all is Distribute, which
extends the packaging and installation facilities provided by the distutils
in the standard library. Once you add Distribute to your Python system you can
download and install any compliant Python software product with a single
command. It also enables you to add this network installation capability to
your own Python software with very little work. Homebrew already installed
Distribute for you.

Happily, when you ran `brew install python`, Homebrew also installed **pip**.
Pip allows for uninstallation of packages, and is actively maintained.


Virtualenv
----------

After Distribute & Pip, the next development tool that you should install is
`virtualenv <http://pypi.python.org/pypi/virtualenv/>`_. Use pip

.. code-block:: console

    $ pip install virtualenv

The virtualenv kit provides the ability to create virtual Python environments
that do not interfere with either each other, or the main Python installation.
If you install virtualenv before you begin coding then you can get into the
habit of using it to create completely clean Python environments for each
project. This is particularly important for Web development, where each
framework and application will have many dependencies.

To set up a new Python environment, change the working directory to where ever
you want to store the environment, and run the virtualenv utility in your
project's directory

.. code-block:: console

    $ virtualenv --distribute venv

To use an environment, run ``source venv/bin/activate``. Your command prompt
will change to show the active environment. Once you have finished working in
the current virtual environment, run ``deactivate`` to restore your settings
to normal.

Each new environment automatically includes a copy of ``pip``, so that you can
setup the third-party libraries and tools that you want to use in that
environment. Put your own code within a subdirectory of the environment,
however you wish. When you no longer need a particular environment, simply
copy your code out of it, and then delete the main directory for the environment.

An useful set of extensions to virtualenv is available in virtualenvwrapper,
`RTFD <http://virtualenvwrapper.readthedocs.org/en/latest/>`_ to find out more.


--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.
