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


Virtual Environments
--------------------

A Virtual Environment is a tool to keep the dependencies required by different projects 
in separate places, by creating virtual Python environments for them. It solves the 
"Project X depends on version 1.x but, Project Y needs 4.x" dilemma, and keeps 
your global site-packages directory clean and manageable.

For example, you can work on a project which requires Django 1.3 while also
maintaining a project which requires Django 1.0.

To start using and see more information: `Virtual Environments <http://github.com/kennethreitz/python-guide/blob/master/docs/dev/virtualenvs.rst>`_ docs. 

You can also use :ref:`virtualenvwrapper <virtualenvwrapper-ref>` to make it easier to
manage your virtual environments.

--------------------------------

This page is a remixed version of `another guide <http://www.stuartellis.eu/articles/python-development-windows/>`_,
which is available under the same license.

