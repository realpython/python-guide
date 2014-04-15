Packaging Your Code
===================

Packaging your code is important.

You'll need to package your code first before sharing it with other developers.

The `Python Packaging Guide <https://python-packaging-user-guide.readthedocs.org/en/latest/>`_ provides an extensive guide on creating and maintaining Python packages.

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

Say if you are after installing a package called :file:`MyPackage.tar.gz`,  and
assuming this is your directory structure:


- archive
   - MyPackage
       - MyPackage.tar.gz

Go to your command prompt and type:

.. code-block:: console

   $ cd archive
   $ python -m SimpleHTTPServer 9000

This runs a simple http server running on port 9000 and will list all packages
(like **MyPackage**). Now you can install **MyPackage** using any Python
package installer. Using Pip, you would do it like:

.. code-block:: console

   $ pip install --extra-index-url=http://127.0.0.1:9000/ MyPackage

Having a folder with the same name as the package name is **crucial** here.
I got fooled by that, one time. But if you feel that creating a folder called
:file:`MyPackage` and keeping :file:`MyPackage.tar.gz` inside that, is *redundant*,
you can still install MyPackage using:

.. code-block:: console

   $ pip install  http://127.0.0.1:9000/MyPackage.tar.gz

pypiserver
++++++++++

`Pypiserver <https://pypi.python.org/pypi/pypiserver>`_ is a minimal PyPI compatible server.
It can be used to serve a set of packages to easy_install or pip.  It includes helpful
features like an administrative command (:option:`-U`) which will update all its packages to their
latest versions found on PyPI.


S3-Hosted PyPi
++++++++++++++

One simple option for a personal PyPi server is to use Amazon S3. A prerequisite for this is that you have an Amazon AWS account with an S3 bucket.

1. **Install all your requirements from PyPi or another source**
2. **Install pip2pi**

* :code:`pip install git+https://github.com/wolever/pip2pi.git`

3. **Follow pip2pi README for pip2tgz and dir2pi commands**

* :code:`pip2tgz packages/ YourPackage` (or :code:`pip2tgz packages/ -r requirements.txt`)
* :code:`dir2pi packages/`

4. **Upload the new files**

* Use a client like Cyberduck to sync the entire :file:`packages` folder to your s3 bucket
* Make sure you upload :code:`packages/simple/index.html` as well as all new files and directories

5. **Fix new file permissions**

* By default, when you upload new files to the S3 bucket, they will have the wrong permissions set.
* Use the Amazon web console to set the READ permission of the files to EVERYONE.
* If you get HTTP 403 when trying to install a package, make sure you've set the permissions correctly.

6. **All done**

* You can now install your package with :code:`pip install --index-url=http://your-s3-bucket/packages/simple/ YourPackage`

For Linux Distributions
::::::::::::::::::::::::

* `Ubuntu <http://packaging.ubuntu.com/html/python-packaging.html>`_
* `Fedora <https://fedoraproject.org/wiki/Packaging:Python>`_
* `Debian <http://www.debian.org/doc/packaging-manuals/python-policy/>`_
* `Arch <https://wiki.archlinux.org/index.php/Python_Package_Guidelines>`_

Useful Tools
------------

- `fpm <https://github.com/jordansissel/fpm>`_
- `alien <http://joeyh.name/code/alien/>`_
