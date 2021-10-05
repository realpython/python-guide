
################
GUI Applications
################

.. image:: /_static/photos/33907143624_cd621b535c_k_d.jpg


Alphabetical list of GUI Applications.


*******
Camelot
*******

`Camelot <http://www.python-camelot.com>`_ provides components for building
applications on top of Python, SQLAlchemy, and Qt.  It is inspired by the Django
admin interface.

The main resource for information is the website:
http://www.python-camelot.com
and the mailing list https://groups.google.com/forum/#!forum/project-camelot.


*****
Cocoa
*****

.. note:: The Cocoa framework is only available on OS X. Don't pick this if you're writing a cross-platform application!


***
GTk
***

.. note:: PyGTK provides Python bindings for the GTK+ toolkit. However, it has been superseded by PyGObject. PyGTK should not be used for new projects and existing projects should be ported to PyGObject.


********************
PyGObject aka (PyGi)
********************

`PyGObject <https://wiki.gnome.org/Projects/PyGObject>`_ provides Python
bindings which gives access to the entire GNOME software platform. It is fully
compatible with GTK+ 3. Here is a tutorial to get started with `Python GTK+ 3
Tutorial <https://python-gtk-3-tutorial.readthedocs.io/en/latest/>`_.

`API Reference <http://lazka.github.io/pgi-docs/>`_


****
Kivy
****

`Kivy <http://kivy.org>`_ is a Python library for development of multi-touch
enabled media rich applications. The aim is to allow for quick and easy
interaction design and rapid prototyping, while making your code reusable and
deployable.

Kivy is written in Python, based on OpenGL, and supports different input devices
such as: Mouse, Dual Mouse, TUIO, WiiMote, WM_TOUCH, HIDtouch, Apple's products,
and so on.

Kivy is actively being developed by a community and is free to use. It operates
on all major platforms (Linux, OS X, Windows, Android).

The main resource for information is the website: http://kivy.org


******
PyObjC
******

.. note:: Only available on OS X. Don't pick this if you're writing a cross-platform application.


******
PySide
******

PySide is a Python binding of the cross-platform GUI toolkit Qt.
The package name depends on the major Qt version (`PySide` for Qt4,
`PySide2` for Qt5, and `PySide6` for Qt6).
This set of bindings is developed by `The Qt Company <https://qt.io>`_.

.. code-block:: console

  $ pip install pyside6

https://pyside.org


****
PyQt
****

.. note:: If your software does not fully comply with the GPL you will need a commercial license!

PyQt provides Python bindings for the Qt Framework (see below).

http://www.riverbankcomputing.co.uk/software/pyqt/download


***************************************
Pyjs Desktop (formerly Pyjamas Desktop)
***************************************

Pyjs Desktop is a application widget set for desktop and a cross-platform
framework. It allows the exact same Python web application source code to be
executed as a standalone desktop application.


The main website: `pyjs <http://pyjs.org/>`_.


**
Qt
**

`Qt <http://qt-project.org/>`_ is a cross-platform application framework that is
widely used for developing software with a GUI but can also be used for non-GUI
applications.


***********
PySimpleGUI
***********

`PySimpleGUI <https://pysimplegui.readthedocs.io/>`_ is a  wrapper for Tkinter
and Qt (others on the way).  The amount of code required to implement custom
GUIs is much shorter using PySimpleGUI than if the same GUI were written
directly using Tkinter or Qt.  PySimpleGUI code can be "ported" between GUI
frameworks by changing import statements.

.. code-block:: console

  $ pip install pysimplegui

PySimpleGUI is contained in a single PySimpleGUI.py file.  Should pip
installation be impossible, copying the PySimpleGUI.py file into a project's
folder is all that's required to import and begin using.


****
Toga
****

`Toga <https://toga.readthedocs.io/en/latest/>`_ is a Python native, OS native,
cross platform GUI toolkit. Toga consists of a library of base components with a
shared interface to simplify platform-agnostic GUI development.

Toga is available on macOS, Windows, Linux (GTK), and mobile platforms such as
Android and iOS.


**
Tk
**

Tkinter is a thin object-oriented layer on top of Tcl/Tk. **It has the advantage
of being included with the Python standard library, making it the most
convenient and compatible toolkit to program with.**

Both Tk and Tkinter are available on most Unix platforms, as well as on Windows
and Macintosh systems. Starting with the 8.0 release, Tk offers native look and
feel on all platforms.

There's a good multi-language Tk tutorial with Python examples at `TkDocs
<http://www.tkdocs.com/tutorial/index.html>`_. There's more information
available on the `Python Wiki <http://wiki.python.org/moin/TkInter>`_.


********
wxPython
********

wxPython is a GUI toolkit for the Python programming language. It allows Python
programmers to create programs with a robust, highly functional graphical user
interface, simply and easily. It is implemented as a Python extension module
(native code) that wraps the popular wxWidgets cross platform GUI library, which
is written in C++.

**Install (Stable) wxPython**
*go to https://www.wxpython.org/pages/downloads/ and download the appropriate
package for your OS.*
