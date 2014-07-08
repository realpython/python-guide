.. _install-linux:

Installing Python on Linux
==========================

The latest versions of Ubuntu and Fedora **come with Python 2.7 out of the box**.

The latest versions of Redhat Enterprise (RHEL) and CentOS come with Python 2.6.
Some older versions of RHEL and CentOS come with Python 2.4 which is
unacceptable for modern Python development. Fortunately, there are
`Extra Packages for Enterprise Linux`_ which include high
quality additional packages based on their Fedora counterparts. This
repository contains a Python 2.6 package specifically designed to install
side-by-side with the system's Python 2.4 installation.

.. _Extra Packages for Enterprise Linux: http://fedoraproject.org/wiki/EPEL

You do not need to install or configure anything else to use Python. Having
said that, I would strongly recommend that you install the tools and libraries
described in the next section before you start building Python applications
for real-world use. In particular, you should always install Setuptools, as
it makes it much easier for you to use other third-party Python libraries.

Setuptools & Pip
----------------

The most crucial third-party Python software of all is Setuptools, which
extends the packaging and installation facilities provided by the distutils
in the standard library. Once you add Setuptools to your Python system you can
download and install any compliant Python software product with a single
command. It also enables you to add this network installation capability to
your own Python software with very little work.

To obtain the latest version of Setuptools for Linux, refer to the documentation
available here: `unix-setuptools <https://pypi.python.org/pypi/setuptools#unix-wget>`_

The new ``easy_install`` command you have available is considered by many to be
deprecated, so we will install its replacement: **pip**. Pip allows for
uninstallation of packages, and is actively maintained, unlike easy_install.

To install pip, simply open a command prompt and run

.. code-block:: console

    $ easy_install pip


Virtualenv
----------

After Setuptools & Pip, the next development tool that you should install is
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

    $ virtualenv venv

To use an environment, run ``source venv/bin/activate``. Your command prompt
will change to show the active environment. Once you have finished working in
the current virtual environment, run ``deactivate`` to restore your settings
to normal.

Each new environment automatically includes a copy of ``pip``, so that you can
setup the third-party libraries and tools that you want to use in that
environment. Put your own code within a subdirectory of the environment,
however you wish. When you no longer need a particular environment, simply
copy your code out of it, and then delete the main directory for the environment.


--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.

