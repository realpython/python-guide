Properly Installing Python
==========================

Any Platform (with Pythonbrew)
::::::::::::::::::::::::::::::

Pythonbrew is a version manager for Python which makes it easy to install
Python and have multiple versions alongside each other, and switch between
them. If you are familiar with RVM for Ruby, it's like that. To install Pythonbrew, ::

    $ curl -kL http://github.com/utahta/pythonbrew/raw/master/pythonbrew-install | bash

You are now presented with further setup instructions. Next, installing Pythons is simple: ::

    $ pythonbrew install 2.7.1 # installs Python 2.7.1
    $ pythonbrew install 3.1.2 # ... and Python 3, if you like

And you can switch to a pythonbrew install and make it your default Python interpreter like so: ::

    $ pythonbrew switch 2.7.1 # makes Python 2.7 default, ignoring any system defaults

Finally, this lets you use a certain Python in your shell: ::

    $ pythonbrew use 3.1.2

And that's about it; pythonbrew will take care of the rest!


Mac OS X
::::::::

*Or, "Installing Python 2.7 via Homebrew".*

One of the reasons everybody loves Python is the interactive shell.  It
basically allows you to execute Python commands in real time and
immediately get results back.  Flask itself does not come with an
interactive shell, because it does not require any specific setup upfront,
just import your application and start playing around.


Package Manager
---------------

While Snow Leopard comes with a large number of UNIX utilities, those
familiar with Linux systems will notice one key component missing: a
package manager. Mxcl's *Homebrew* is the answer.

To install Homebrew, simply run: ::

    $ ruby -e "$(curl -fsS http://gist.github.com/raw/323731/install_homebrew.rb)"


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



To install ``pip``: ::

Hopefully you'll never have to use **easy_install** again.


Updating Python
---------------

Homebrew makes it simple. ::

    $ brew update
    $ brew install --force python


Windows
:::::::



Prerequisites:
--------------

* Python2.7 (x86) from Python.org
* Microsoft Visual Studio


Step 1: Install Distribute & Pip
--------------------------------

**Distribute** is a fantastic drop-in replacement for **easy_install** and **setuptools**. It allows you to install and manage python packages from PyPi, amongst a few other sources.

To install it, run the python script available here:
  <http://python-distribute.org/distribute_setup.py>

Make sure that ```C:\Python27\```, and  ```C:\Python27\Scripts``` are in your PATH.

**easy_install** is considered by many to be a deprecated system, so we will install it's replacement: **pip**. Pip allows for uninstallation of packages, and is actively maintained, unlike setuptool's easy_install.

To install pip, simply run: ::

    $ easy_install pip


Linux (Ubuntu)
::::::::::::::

Oneiric Ocelot, the latest version of Ubuntu, **comes with Python 2.7 out of the box**. Python 3.2 can be installed and run with the following commands::

    $ sudo apt-get install python3-minimal
    $ python3

Older versions of Python aren't available from the official repository. However, if it's needed (for example to support legacy code), we can add an unsupported repository and install an older version of Python (2.5 in the example below)::

    $ sudo apt-get install python-software-properties
    $ sudo add-apt-repository ppa:fkrull/deadsnakes
    $ sudo apt-get update
    $ sudo apt-get install python2.5

Installing setuptools and pip
-----------------------------

While Python has an extensive standard library, the set of packages available from the Internet is even more extensive. In order to install them easily, we'll install the ``setuptools`` package and ``pip`` installer::

.. XXX: sudo?

    $ wget http://python-distribute.org/distribute_setup.py
    $ python distribute_setup.py
    $ wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py 
    $ python get-pip.py
    $ rm get-pip.py distribute_setup.py

Now, most Python packages can be installed using the ``pip`` command. For example, if we wanted to install Django::

    $ sudo pip install django

A full list of ``pip``'s capabilities is available by typing ``pip --help``.

Linux (Manual)
--------------

While your system will quite likely already have Python installation, you might wish to install a different version. This is done in the typical Linux software source install procedure::

    $ wget http://www.python.org/ftp/python/2.7.2/Python-2.7.2.tgz
    $ tar -xvf Python-2.7.2.tgz
    $ cd Python-2.7.2
    $ ./configure
    $ make
    $ make install



