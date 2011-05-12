GUI Applications
================


Qt
::
Qt is a cross-platform application framework that is widely used for developing software with a GUI but can also be used for non-GUI applications.

PySide
------
http://developer.qt.nokia.com/wiki/PySideDownloads/

PyQt
----
*Note: If your software does not fully comply with the GPL you will need a commercial license!*
http://www.riverbankcomputing.co.uk/software/pyqt/download

Cocoa
:::::
*Note: The Cocoa framework is only available on Mac OSX. Don't pick this if you're writing a cross-platform application!*

PyObjC
------
PyObjC 2.0 is included in the default python installation of Mac OS X 10.5 Leopard.
To install the latest version: ::
    $ pip install pyobjc 
or go to http://pyobjc.sourceforge.net/downloads.html

WXPython
::::::::
Install (Stable)
----
*Go to http://www.wxpython.org/download.php#stable and download the appropriate package for your OS.*
The simplest method to test if it works is to attempt to import it. ::
    Aarons-MacBook:docs aaron$ python
    Python 2.6.6 (r266:84374, Aug 31 2010, 11:00:51) 
    [GCC 4.0.1 (Apple Inc. build 5493)] on darwin
    >>> import wx
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ImportError: No module named wx
If you don't get the above error, WXPython is installed.

Gtk
:::

tk
::