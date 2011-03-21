Properly Installing Python 
==========================

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



Python Interpreter
------------------

And we can now install Python 2.7: ::

    $ brew install python --framework


The ``--framework`` option tells Homebrew to compile a Framework-style Python build, rather than a UNIX-style build. The outdated version of Python that Snow Leopard comes packaged with 
is built as a Framework, so this helps avoid some future module installation 
bugs. 

*Don't forget to update your environment PATH.* 


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



Linux (Manual)
::::::::::::::



