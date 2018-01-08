.. _packaging-your-code-ref:

===================
Packaging Your Code
===================

.. image:: https://farm5.staticflickr.com/4325/36137234682_be6898bf57_k_d.jpg

Package your code to share it with other developers. For example
to share a library for other developers to use in their application,
or for development tools like 'py.test'.

An advantage of this method of distribution is its well established ecosystem
of tools such as PyPI and pip, which make it easy for other developers to
download and install your package either for casual experiments, or as part of
large, professional systems.

It is a well-established convention for Python code to be shared this way.
If your code isn't packaged on PyPI, then it will be harder
for other developers to find it, and to use it as part of their existing
process. They will regard such projects with substantial suspicion of being
either badly managed or abandoned.

The downside of distributing code like this is that it relies on the
recipient understanding how to install the required version of Python,
and being able and willing to use tools such as pip to install your code's
other dependencies. This is fine when distributing to other developers, but
makes this method unsuitable for distributing applications to end-users.

The `Python Packaging Guide <https://python-packaging-user-guide.readthedocs.io/>`_
provides an extensive guide on creating and maintaining Python packages.

Alternatives to Packaging
:::::::::::::::::::::::::

To distribute applications to end-users, you should
:ref:`freeze your application <freezing-your-code-ref>`.

On Linux, you may also want to consider
:ref:`creating a Linux distro package <packaging-for-linux-distributions-ref>`
(e.g. a .deb file for Debian or Ubuntu.)

For Python Developers
:::::::::::::::::::::

If you're writing an open source Python module, `PyPI <http://pypi.python.org>`_
, more properly known as *The Cheeseshop*, is the place to host it.



Pip vs. easy_install
--------------------

Use `pip <http://pypi.python.org/pypi/pip>`_.  More details
`here <http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install>`_


Personal PyPI
-------------

If you want to install packages from a source other than PyPI, (say, if
your packages are *proprietary*), you can do it by hosting a simple http
server, running from the directory which holds those packages which need to be
installed.

**Showing an example is always beneficial**

For example, if you want to install a package called :file:`MyPackage.tar.gz`,
and assuming this is your directory structure:


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
:file:`MyPackage` and keeping :file:`MyPackage.tar.gz` inside that, is
*redundant*, you can still install MyPackage using:

.. code-block:: console

   $ pip install  http://127.0.0.1:9000/MyPackage.tar.gz

pypiserver
++++++++++

`Pypiserver <https://pypi.python.org/pypi/pypiserver>`_ is a minimal PyPI
compatible server.  It can be used to serve a set of packages to easy_install
or pip.  It includes helpful features like an administrative command
(``-U``) which will update all its packages to their latest versions
found on PyPI.


S3-Hosted PyPi
++++++++++++++

One simple option for a personal PyPi server is to use Amazon S3. A
prerequisite for this is that you have an Amazon AWS account with an S3 bucket.

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

.. _packaging-for-linux-distributions-ref:

For Linux Distributions
::::::::::::::::::::::::

Creating a Linux distro package is arguably the "right way" to distribute code
on Linux.

Because a distribution package doesn't include the Python interpreter, it
makes the download and install about 2MB smaller than
:ref:`freezing your application <freezing-your-code-ref>`.

Also, if a distribution releases a new security update for Python, then your
application will automatically start using that new version of Python.

The bdist_rpm command makes `producing an RPM file <https://docs.python.org/3/distutils/builtdist.html#creating-rpm-packages>`_
for use by distributions like Red Hat or SuSE trivially easy.

However, creating and maintaining the different configurations required for
each distribution's format (e.g. .deb for Debian/Ubuntu, .rpm for Red
Hat/Fedora, etc) is a fair amount of work. If your code is an application that
you plan to distribute on other platforms, then you'll also have to create and
maintain the separate config required to freeze your application for Windows
and OSX. It would be much less work to simply create and maintain a single
config for one of the cross platform :ref:`freezing tools
<freezing-your-code-ref>`, which will produce stand-alone executables for all
distributions of Linux, as well as Windows and OSX.

Creating a distribution package is also problematic if your code is for a
version of Python that isn't currently supported by a distribution.
Having to tell *some versions* of Ubuntu end-users that they need to add `the
'dead-snakes' PPA <https://launchpad.net/~fkrull/+archive/ubuntu/deadsnakes>`_
using `sudo apt-repository` commands before they can install your .deb file
makes for an extremely hostile user experience. Not only that, but you'd have
to maintain a custom equivalent of these instructions for every distribution,
and worse, have your users read, understand, and act on them.

Having said all that, here's how to do it:

* `Fedora <https://fedoraproject.org/wiki/Packaging:Python>`_
* `Debian and Ubuntu <http://www.debian.org/doc/packaging-manuals/python-policy/>`_
* `Arch <https://wiki.archlinux.org/index.php/Python_Package_Guidelines>`_

Useful Tools
------------

- `fpm <https://github.com/jordansissel/fpm>`_
- `alien <http://joeyh.name/code/alien/>`_
- `dh-virtualenv <https://dh-virtualenv.readthedocs.io/en/latest/info.html>`_ (for APT/DEB omnibus packaging)
