.. _freezing-your-code-ref:


##################
Freezing Your Code
##################

.. image:: /_static/photos/33907151034_e0a9e53402_k_d.jpg

"Freezing" your code is creating a single-file executable file to distribute
to end-users, that contains all of your application code as well as the
Python interpreter.

Applications such as 'Dropbox', 'Eve Online',  'Civilization IV', and
BitTorrent clients do this.

The advantage of distributing this way is that your application will "just work",
even if the user doesn't already have the required version of Python (or any)
installed. On Windows, and even on many Linux distributions and OS X, the right
version of Python will not already be installed.

Besides, end-user software should always be in an executable format. Files
ending in ``.py`` are for software engineers and system administrators.

One disadvantage of freezing is that it will increase the size of your
distribution by about 2–12 MB. Also, you will be responsible for shipping
updated versions of your application when security vulnerabilities to
Python are patched.


************************
Alternatives to Freezing
************************

:ref:`Packaging your code <packaging-your-code-ref>` is for distributing
libraries or tools to other developers.

On Linux, an alternative to freezing is to
:ref:`create a Linux distro package <packaging-for-linux-distributions-ref>`
(e.g. .deb files for Debian or Ubuntu, or .rpm files for Red Hat and SuSE.)

.. todo:: Fill in "Freezing Your Code" stub


****************************
Comparison of Freezing Tools
****************************

Date of this writing: Oct 5, 2019
Solutions and platforms/features supported:

=========== ======= ===== ==== ======== ======= ============= ============== ==== ===================== =====================
Solution    Windows Linux OS X Python 3 License One-file mode Zipfile import Eggs pkg_resources support Latest release date
=========== ======= ===== ==== ======== ======= ============= ============== ==== ===================== =====================
bbFreeze    yes     yes   yes  no       MIT     no            yes            yes  yes                   Jan 20, 2014
py2exe      yes     no    no   yes      MIT     yes           yes            no   no                    Oct 21, 2014
pyInstaller yes     yes   yes  yes      GPL     yes           no             yes  no                    Jul 9, 2019
cx_Freeze   yes     yes   yes  yes      PSF     no            yes            yes  no                    Aug 29, 2019
py2app      no      no    yes  yes      MIT     no            yes            yes  yes                   Mar 25, 2019
=========== ======= ===== ==== ======== ======= ============= ============== ==== ===================== =====================

.. note::
    Freezing Python code on Linux into a Windows executable was only once
    supported in PyInstaller `and later dropped
    <https://stackoverflow.com/questions/2950971/cross-compiling-a-python-script-on-linux-into-a-windows-executable#comment11890276_2951046>`_.

.. note::
    All solutions need a Microsoft Visual C++ to be installed on the target machine, except py2app.
    Only PyInstaller makes a self-executable exe that bundles the appropriate DLL when
    passing ``--onefile`` to :file:`Configure.py`.


*******
Windows
*******

bbFreeze
~~~~~~~~

Prerequisite is to install :ref:`Python, Setuptools and pywin32 dependency on Windows <install-windows>`.

1. Install :code:`bbfreeze`:

.. code-block:: console

    $ pip install bbfreeze

2. Write most basic :file:`bb_setup.py`

.. code-block:: python

    from bbfreeze import Freezer

    freezer = Freezer(distdir='dist')
    freezer.addScript('foobar.py', gui_only=True)
    freezer()

.. note::

    This will work for the most basic one file scripts. For more advanced freezing you will have to provide
    include and exclude paths like so:

    .. code-block:: python

        freezer = Freezer(distdir='dist', includes=['my_code'], excludes=['docs'])

3. (Optionally) include icon

.. code-block:: python

    freezer.setIcon('my_awesome_icon.ico')

4. Provide the Microsoft Visual C++ runtime DLL for the freezer. It might be possible to append your :code:`sys.path`
with the Microsoft Visual Studio path but I find it easier to drop :file:`msvcp90.dll` in the same folder where your script
resides.

5. Freeze!

.. code-block:: console

    $ python bb_setup.py

py2exe
~~~~~~

Prerequisite is to install :ref:`Python on Windows <install-windows>`. The last release of py2exe is from the year 2014. There is not active development.

1. Download and install http://sourceforge.net/projects/py2exe/files/py2exe/

2. Write :file:`setup.py` (`List of configuration options <http://www.py2exe.org/index.cgi/ListOfOptions>`_):

.. code-block:: python

    from distutils.core import setup
    import py2exe

    setup(
        windows=[{'script': 'foobar.py'}],
    )

3. (Optionally) `include icon <http://www.py2exe.org/index.cgi/CustomIcons>`_

4. (Optionally) `one-file mode <https://stackoverflow.com/questions/112698/py2exe-generate-single-executable-file#113014>`_

5. Generate :file:`.exe` into :file:`dist` directory:

.. code-block:: console

   $ python setup.py py2exe

6. Provide the Microsoft Visual C++ runtime DLL. Two options: `globally install dll on target machine <https://www.microsoft.com/en-us/download/details.aspx?id=29>`_ or `distribute dll alongside with .exe <http://www.py2exe.org/index.cgi/Tutorial#Step52>`_.

PyInstaller
~~~~~~~~~~~

Prerequisite is to have installed :ref:`Python, Setuptools and pywin32 dependency on Windows <install-windows>`.

- `Most basic tutorial <http://bojan-komazec.blogspot.com/2011/08/how-to-create-windows-executable-from.html>`_
- `Manual <https://pyinstaller.readthedocs.io/en/stable/>`_


****
OS X
****


py2app
~~~~~~

PyInstaller
~~~~~~~~~~~

PyInstaller can be used to build Unix executables and windowed apps on Mac OS X 10.6 (Snow Leopard) or newer.

To install PyInstaller, use pip:

.. code-block:: console

 $ pip install pyinstaller

To create a standard Unix executable, from say :code:`script.py`, use:

.. code-block:: console

 $ pyinstaller script.py

This creates:

- a :code:`script.spec` file, analogous to a :code:`make` file
- a :code:`build` folder, that holds some log files
- a :code:`dist` folder, that holds the main executable :code:`script`, and some dependent Python libraries

all in the same folder as :code:`script.py`. PyInstaller puts all the Python libraries used in :code:`script.py` into the :code:`dist` folder, so when distributing the executable, distribute the whole :code:`dist` folder.

The :code:`script.spec` file can be edited to `customise the build <http://pythonhosted.org/PyInstaller/#spec-file-operation>`_, with options such as:

- bundling data files with the executable
- including run-time libraries (:code:`.dll` or :code:`.so` files) that PyInstaller can't infer automatically
- adding Python run-time options to the executable

Now :code:`script.spec` can be run with :code:`pyinstaller` (instead of using :code:`script.py` again):

.. code-block:: console

  $ pyinstaller script.spec

To create a standalone windowed OS X application, use the :code:`--windowed` option:

.. code-block:: console

 $ pyinstaller --windowed script.spec

This creates a :code:`script.app` in the :code:`dist` folder. Make sure to use GUI packages in your Python code, like `PyQt <https://riverbankcomputing.com/software/pyqt/intro>`_ or `PySide <http://wiki.qt.io/About-PySide>`_, to control the graphical parts of the app.

There are several options in :code:`script.spec` related to Mac OS X app bundles `here <http://pythonhosted.org/PyInstaller/spec-files.html#spec-file-options-for-a-mac-os-x-bundle>`_. For example, to specify an icon for the app, use the :code:`icon=\path\to\icon.icns` option.


*****
Linux
*****


bbFreeze
~~~~~~~~
.. warning:: bbFreeze will ONLY work in Python 2.x environment, since it's no longer being maintained as stated by it's former maintainer. If you're interested in it, check the repository in `here <https://github.com/schmir/bbfreeze>`_.

bbFreeze can be used with all distributions that has Python installed along with pip2 and/or easy_install.

For pip2, use the following:

.. code-block:: console

  $ pip2 install bbfreeze

Or, for easy_install:

.. code-block:: console

  $ easy_install bbfreeze

With bbFreeze installed, you're ready to freeze your applications. 

Let's assume you have a script, say, "hello.py" and a module called "module.py" and you have a function in it that's being used in your script.
No need to worry, you can just ask to freeze the main entrypoint of your script and it should freeze entirely:

.. code-block:: console

  $ bbfreeze script.py

With this, it creates a folder called dist/, of which contains the executable of the script and required .so (shared objects) files linked against libraries used within the Python script.

Alternatively, you can create a script that does the freezing for you. An API for the freezer is available from the library within:

.. code-block:: python

   from bbfreeze import Freezer

   freezer = Freezer(distdir='dist')
   freezer.addScript('script.py', gui_only=True) # Enable gui_only kwarg for app that uses GUI packages.
   freezer()

PyInstaller
~~~~~~~~~~~
PyInstaller can be used in a similar fashion as in OS X. The installation goes in the same manner as shown in the OS X section.

Don't forget to have dependencies such as Python and pip installed for usage.
