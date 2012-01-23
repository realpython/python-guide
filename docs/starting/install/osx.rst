Installing Python on Mac OS X
=============================

*Or, "Installing Python 2.7 via Homebrew".*

The latest version of Mac OS X, **comes with Python 2.7 out of the box**.

You do not need to install or configure anything else to use Python. Having said that, I would strongly recommend that you install the tools and libraries described in the next section before you start building Python applications for real-world use. In particular, you should always install Distribute, as it makes it much easier for you to use other third-party Python libraries.

The version of Python that ships with OS X is great for learning, but it's not good for development. It's slightly out of date, and Apple has made significant changes that can cause hidden bugs.

Doing it Right
--------------

Let's get a real version of Python.

While Lion comes with a large number of UNIX utilities, those
familiar with Linux systems will notice one key component missing: a decent
package manager. `Homebrew <http://mxcl.github.com/homebrew/>`_ fills this void.

First, you'll need to have GCC installed to compile Python. You can either get this from `XCode <http://developer.apple.com/xcode/>`_ or the smaller `OSX-GCC-Installer <https://github.com/kennethreitz/osx-gcc-installer#readme>`_ package.

To `install Homebrew <https://github.com/mxcl/homebrew/wiki/installation>`_, simply run::

    $ ruby -e "$(curl -fsS https://raw.github.com/gist/323731)"

Then, insert the hombrew directory at the top of your ``PATH`` enviornment variable. You can do this by adding the following line at the bottom of your ``~/.bashrc`` file::

    export PATH=/usr/local/bin:$PATH

Now, we can install Python 2.7: ::

    $ brew install python --framework

This will take a minute or two. Once that's complete, you'll have to add the new Python scripts directory to your ``PATH``::

    export PATH=$PATH:/usr/local/share/python

The ``--framework`` option tells Homebrew to compile a Framework-style Python build, rather than a UNIX-style build. The outdated version of Python that Snow Leopard comes packaged with is built as a Framework, so this helps avoid some future module installation bugs.


Distribute & Pip
----------------

The most crucial third-party Python software of all is Distribute, which extends the packaging and installation facilities provided by the distutils in the standard library. Once you add Distribute to your Python system you can download and install any compliant Python software product with a single command. It also enables you to add this network installation capability to your own Python software with very little work.

Hombrew already installed Distribute for you. Its ``easy_install`` command is considered by many to be deprecated, so we will install its replacement: **pip**. Pip allows for uninstallation of packages, and is actively maintained, unlike easy_install.

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
