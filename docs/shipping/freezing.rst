.. _freezing-your-code-ref:

==================
Freezing Your Code
==================

To 'Freeze' your code is to distribute to end-users as an executable which
includes a bundled Python interpreter.

Applications such as 'Dropbox', BitTorrent clients, 'Eve Online' and
'Civilisation IV' do this.

The advantage of distributing this way is that your application will work even
if the user doesn't already have the required version of Python installed. On
Windows, and even on many Linux distributions and OSX versions, the right
version of Python will not already be installed.

One disadvantage is that it will bloat your distribution by about 2MB.
Another problem is that your application will not receive any security updates
to the version of Python it uses unless you freeze a new version and get
users to download it.

Alternatives to Freezing
------------------------

:ref:`Packaging your code <packaging-your-code-ref>` is for distributing
libraries or tools to other developers.

On Linux, an alternative to freezing is to
:ref:`create a Linux distro package <packaging-for-linux-distributions-ref>`
(e.g. .deb files for Debian or Ubuntu, or .rpm files for Red Hat and SuSE.)

.. todo:: Fill in "Freezing Your Code" stub


Comparison
----------

Solutions and platforms/features supported:

=========== ======= ===== ==== ======== ======= ============= ============== ==== =====================
Solution    Windows Linux OS X Python 3 License One-file mode Zipfile import Eggs pkg_resources support
=========== ======= ===== ==== ======== ======= ============= ============== ==== =====================
bbFreeze    yes     yes   yes  no       MIT     no            yes            yes  yes
py2exe      yes     no    no   yes      MIT     yes           yes            no   no
pyInstaller yes     yes   yes  yes      GPL     yes           no             yes  no
cx_Freeze   yes     yes   yes  yes      PSF     no            yes            yes  no
py2app      no      no    yes  yes      MIT     no            yes            yes  yes
=========== ======= ===== ==== ======== ======= ============= ============== ==== =====================

.. note::
    Freezing Python code on Linux into a Windows executable was only once
    supported in PyInstaller `and later dropped.
    <http://stackoverflow.com/questions/2950971/cross-compiling-a-python-script-on-linux-into-a-windows-executable#comment11890276_2951046>`_.

.. note::
    All solutions need MS Visual C++ dll to be installed on target machine, except py2app.
    Only Pyinstaller makes self-executable exe that bundles the dll when
    passing :option:`--onefile` to :file:`Configure.py`.

Windows
-------

bbFreeze
~~~~~~~~

Prerequisite is to install :ref:`Python, Setuptools and pywin32 dependency on Windows <install-windows>`.

.. todo:: Write steps for most basic .exe

py2exe
~~~~~~

Prerequisite is to install :ref:`Python on Windows <install-windows>`.

1. Download and install http://sourceforge.net/projects/py2exe/files/py2exe/

2. Write :file:`setup.py` (`List of configuration options <http://www.py2exe.org/index.cgi/ListOfOptions>`_):

.. code-block:: python

    from distutils.core import setup
    import py2exe

    setup(
        windows=[{'script': 'foobar.py'}],
    )

3. (Optionally) `include icon <http://www.py2exe.org/index.cgi/CustomIcons>`_

4. (Optionally) `one-file mode <http://stackoverflow.com/questions/112698/py2exe-generate-single-executable-file#113014>`_

5. Generate :file:`.exe` into :file:`dist` directory:

.. code-block:: console

   $ python setup.py py2exe

6. Provide the Microsoft Visual C runtime DLL. Two options: `globally install dll on target machine <https://www.microsoft.com/en-us/download/details.aspx?id=29>`_ or `distribute dll alongside with .exe <http://www.py2exe.org/index.cgi/Tutorial#Step52>`_.

PyInstaller
~~~~~~~~~~~

Prerequisite is to have installed :ref:`Python, Setuptools and pywin32 dependency on Windows <install-windows>`.

- `Most basic tutorial <http://bojan-komazec.blogspot.com/2011/08/how-to-create-windows-executable-from.html>`_
- `Manual <http://www.pyinstaller.org/export/d3398dd79b68901ae1edd761f3fe0f4ff19cfb1a/project/doc/Manual.html?format=raw>`_


OS X
----


py2app
~~~~~~

PyInstaller
~~~~~~~~~~~


Linux
-----


bbFreeze
~~~~~~~~

PyInstaller
~~~~~~~~~~~
