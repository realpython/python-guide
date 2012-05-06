Packaging Your Code
===================

Packaging your code is important.

You'll need to package your code first before sharing it with other developers.

For Python Developers
:::::::::::::::::::::

If you're writing an open source Python module, `PyPI <http://pypi.python.org>`_,
more properly known as *The Cheeseshop*, is the place to host it.



Pip vs. easy_install
--------------------

Use `pip <http://pypi.python.org/pypi/pip>`_.  More details `here <http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install>`_


Personal PyPI
-------------

If you want to install packages from a source different from PyPI, (say, if
your packages are *proprietary*), you can do it by hosting a simple http server,
running from the directory which holds those packages which need to be installed.

**Showing an example is always beneficial**

Say if you are after installing a package called MyPackage.tar.gz,  and
assuming this is your directory structure:


- archive
   - MyPackage
       - MyPackage.tar.gz

Go to your command prompt and type:

.. code-block:: console

   $ cd archive
   $ python -m SimpleHTTPServer 9000

This runs a simple http server running on port 9000 and will list all packages
(like **MyPackage**). Now you can install **MyPackage** using any python
package installer. Using Pip, you would do it like:

.. code-block:: console

   $ pip install --extra-index-url=http://127.0.0.1:9000/ MyPackage

Having a folder with the same name as the package name is **crucial** here.
I got fooled by that, one time. But if you feel that creating a folder called
**MyPackage** and keeping **MyPackage.tar.gz** inside that, is *redundant*,
you can still install MyPackage using:

.. code-block:: console

   $ pip install  http://127.0.0.1:9000/MyPackage.tar.gz

Chishop
+++++++

`Chishop <https://github.com/benliles/djangopypi>`_ is a simple PyPI server
written in django which allows you to register/upload with distutils and
install with easy_install/pip.

For Linux Distributions
::::::::::::::::::::::::

* `Ubuntu <https://wiki.ubuntu.com/PackagingGuide/Python>`_
* `Fedora <https://fedoraproject.org/wiki/Packaging:Python>`_
* `Debian <http://www.debian.org/doc/packaging-manuals/python-policy/>`_
* `Arch <https://wiki.archlinux.org/index.php/Python_Package_Guidelines>`_

Useful Tools
------------

- epm
- alien
