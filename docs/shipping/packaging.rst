Packaging Your Code
===================

Packaging your code is important.


For Python Developers
:::::::::::::::::::::

If you're writing an open source Python module, `PyPi <http://pypi.python.org>`_, more properly known as *The Cheeseshop*, is the place to host it.



Pip vs. easy_install
--------------------

x y z


Personal PyPi
-------------

If you want to install packages from a source different from PyPI, (say, if
your packages are *proprietary*), you can do it by hosting a simple http server,
running from the directory which holds those packages which need to be installed.

**Showing an example is always benificial**

Say if you are after installing a package called MyPackage.tar.gz,  and assuming this is your directory structure


- archive
   - MyPackage
       - MyPackage.tar.gz

Go to your command prompt and type:
::

$ cd archive
$ python -m SimpleHTTPServer 9000

This runs a simple http server running on port 9000 and will list down all packages(like **MyPackage**). Now you can install **MyPackage** using any python package installer. Using Pip, you would do it like:
::

$ pip install --extra-index-url=http://127.0.0.1:9000/ MyPackage

Remember! having a folder with the same name as the package name is **crucia** here.
I got fooled by that, one time. But if you feel that creating a folder called
**MyPackag** and keeping **MyPackage.tar.gz** inside that, is *reduntant*, you can still install MyPackage using:
::

$ pip install  http://127.0.0.1:9000/MyPackage.tar.gz

Chishop
+++++++


For Linux Distributions
::::::::::::::::::::::::

Useful Tools
````````````

- epm
- alien