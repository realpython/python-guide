Installing Python on Linux
==========================


The latest version of Ubuntu, **comes with Python 2.7 out of the box**. Python 3.2 can be installed and run with the following commands::

    $ sudo apt-get install python3-minimal
    $ python3

Older versions of Python aren't available from the official repository. However, if it's needed (for example to support legacy code), we can add an unsupported repository and install an older version of Python (2.5 in the example below)::

    $ sudo apt-get install python-software-properties
    $ sudo add-apt-repository ppa:fkrull/deadsnakes
    $ sudo apt-get update
    $ sudo apt-get install python2.5

Installing setuptools and pip
-----------------------------

While Python has an extensive standard library, the set of packages available from the Internet is even more extensive. In order to install them easily, we'll install the ``distribute`` package and then ``pip``::

    $ wget http://python-distribute.org/distribute_setup.py
    $ sudo python distribute_setup.py
    $ sudo easy_install pip

Now, most Python packages can be installed using the ``pip`` command. For example, if we wanted to install Django::

    $ sudo pip install django

A full list of ``pip``'s capabilities is available by typing ``pip --help``.

