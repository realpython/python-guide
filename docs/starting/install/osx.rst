Mac OS X
========

*Or, "Installing Python 2.7 via Homebrew".*

Package Manager
---------------

While Snow Leopard comes with a large number of UNIX utilities, those
familiar with Linux systems will notice one key component missing: a
package manager. Mxcl's `Homebrew <http://mxcl.github.com/homebrew/>`_ is the answer.

To `install Homebrew <https://github.com/mxcl/homebrew/wiki/installation>`_, simply run: ::

    $ ruby -e "$(curl -fsS https://raw.github.com/gist/323731)"


It's basic commands are **update**, **install**, and **remove**.

.. man brew


And we can now install Python 2.7: ::

    $ brew install python --framework


The ``--framework`` option tells Homebrew to compile a Framework-style Python build, rather than a UNIX-style build. The outdated version of Python that Snow Leopard comes packaged with
is built as a Framework, so this helps avoid some future module installation
bugs.

*Don't forget to update your environment PATH.*

Building From Source
--------------------

.. todo:: Write "Building From Source"


Distribute & Pip
----------------

*Distribute* is a fantastic drop-in replacement for *easy_install* and
*setuptools*. It allows you to install and manage python packages from
pypi.python.org, amongst a few other sources. It also plays well with
*virtualenv* and user-enviornments.

**easy_install** is considered by many to be a deprecated system, so we
will install it's replacement: **pip**. Pip allows for uninstallation
of packages, and is actively maintained, unlike setuptool's easy_install.

To install *pip* and Distribute's *easy_install*:

If you have homebrew: ::

    $ brew install pip

...And, if you're a masochist: ::

    $ curl -O http://python-distribute.org/distribute_setup.py
    $ python distribute_setup.py

    $ easy_install pip

Hopefully you'll never have to use **easy_install** again.


Updating Python
---------------

Homebrew makes it simple. ::

    $ brew update
    $ brew install --force python

