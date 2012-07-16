==================
Image Manipulation
==================

.. todo::
    Add introduction about image manipulation and its Python libraries.

Python Imaging Library
----------------------

The `Python Imaging Library <http://www.pythonware.com/products/pil/>`_, or PIL
for short, is *the* library for image manipulation in Python.

It works with Python 1.5.2 and above, including 2.5, 2.6 and 2.7. Unfortunately,
it doesn't work with 3.0+ yet. 

Installation
~~~~~~~~~~~~

PIL has a reputation of not being very straightforward to install. Listed below
are installation notes on various systems.

Also, there's a fork named `Pillow <http://pypi.python.org/pypi/Pillow>`_ which is easier 
to install. It has good setup instructions for all platforms.

Installing on Linux
~~~~~~~~~~~~~~~~~~~

Ubuntu 11.04
````````````

.. todo::
    Notes on installing on Ubuntu 11.04

Installing on Mac OS X
~~~~~~~~~~~~~~~~~~~~~~

PIP doesn't know about the Mac OS X Freetype paths. To rectify that:

.. code-block:: bash

    $ ln -s /usr/X11/include/freetype2 /usr/local/include/
    $ ln -s /usr/X11/include/ft2build.h /usr/local/include/
    $ ln -s /usr/X11/lib/libfreetype.6.dylib /usr/local/lib/
    $ ln -s /usr/X11/lib/libfreetype.6.dylib /usr/local/lib/libfreetype.dylib

then:

.. code-block:: bash

    $ brew install libjpeg
    $ pip install PIL


Installing on Windows
~~~~~~~~~~~~~~~~~~~~~

.. todo::
    Notes on installing on Windows machines


