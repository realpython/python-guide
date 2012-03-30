.. _install-windows:

============================
Installing Python on Windows
============================

Overview
========

Unlike in other operating systems, Python is not installed by default on
Windows. In this section, we'll put a remedy to that. These are the steps
involved:

* Obtaining a Python installer
* Running the installer
* Setting up the shell environment
* Installing recommended libraries
* Done!

Although this process can be completed quickly, we'll also explain a few
concepts along the way that will come in handy for your Python development.

Obtaining a Python Installer
============================

Python is free. The distribution supported by the Python dev team is available
at python.org. However, some organizations offer alternative commercial and
free Python distributions for Windows. These alternative distributions usually
include preinstalled libraries and additional documentation.

No matter what distribution you choose, you will be able to install all
libraries on your own later. Choosing one over the others is largely a matter
of preference unless you have very specific needs. If you are a beginner or
don't know which one is best for you, choose any of the free distributions.

Here's two popular free Python distributions:

* Python.org
* ActiveState Python

Running the Installer
=====================

Once you've downloaded the Windows installer, double click on it and follow
the onscreen instrunctions.

By default, Python installs to a directory with the version number embedded,
such as ``C:\Python27\``. This way, advanced users can install multiple
versions of Python on the same system without conflicts.

When the installer finishes, you will have Python installed and ``.py`` and
``.pyw`` files will be associated with the Python interpreter, so you can
easily run them by doubleclicking on them or specifying their path on the
command line, like this::

	PS> C:\Users\Frank\Documents\Dev\AwesomeProject\foo.py

Otherwise, you would have to specify the path to the Python interpreter first,
and then the path to the script, like so::

	PS> C:\Python27\python.exe C:\Users\Frank\Documents\Dev\AwesomeProject\foo.py

The :var:`PATH` Variable
========================

As the name suggest, the :var:`PATH` variable is a string of paths separated
by semicolons. It determines which program names are globally *visible* so
they can be launched conveniently by name. It saves you having to type out
full paths to executable files.

To follow on last example, if the :var:`PATH` was correctly set,  it could be
rewritten to read like this::

	PS> python "C:\Users\Frank\Documents\Dev\AwesomeProject\foo.py"

This would work because **python.exe** would be reachable everywhere from the
command line.

Because the installer will set up file type associations between ``.py`` and
``.pyw`` files, though, in a real-life situation you would most likely omit
``python`` from your command line. The above is just an example.

Some Python installers don't modify the :var:`PATH` variable, so the user is
always in control over which copy of Python is run. This is important for
advanced users who might have several versions of Python installed.

We'll see how to set the :var:`PATH` environment variable in a bit, but first
let's talk about the Windows command line.

The Windows Command Line: CMD.exe vs Powershell
-----------------------------------------------

You might know the command line by any of its many names: DOS console, shell,
command prompt, command processor, console window...

Modern versions of Windows ship with two shells: CMD and Powershell. A shell
is esentially another programming language much like Python, only with the
specialized purpose of system administration. Learning the basics of a shell
language will make you much more productive, because shell languages enable
you to automate common tasks that otherwise would require manually clicking
around in graphical user interfaces or repeating the same steps over and over.

Learn a shell language, it's worth it!

The Python interpreter has an interactive mode that runs in a console window.
You can launch it as a stand-alone program or from the shell. You will likely
be doing the latter more often than not, so that's another reason for learning
the Windows command line. If you're decided to do so, choose Powershell.
Powershell is the future of the Windows command line.

But don't fret: in this section you will only need to type in basic commands
at the Powershell prompt. You don't need to learn Powershell now.

To start Powershell, press ``Windows Key + R``, type in "powershell" without
the quotes and press :kbd:`Enter`. If you get an error, you are probably
running an ancient version of Windows and will need to install Powershell
separately. Explaining how to install Powershell is beyond the scope of this
guide.

If you must, use **cmd.exe** instead.

Setting Up the Shell Environment
================================

Shell languages run in an *environment* you can control. An important part of
that environment are environment variables, such as :var:`PATH`.

Environment variables can be set system-wide or per shell session. System-wide
environment variables will always be in effect. Per-session variables will
go away as soon as you close the corresponding shell window.

Note that if your installer has modified the :var:`PATH` variable during
installation, you will not have to perform the steps below.

System-wide environment variables can be modified through graphical user
interfaces. Per-session enviroment variables require only a shell window
to be open. We'll focus on the latter here.

Assuming you've installed Python 2.7, type this at a Powershell prompt::

	PS> $env:PATH += ";C:\Python27;C:\Python27\Scripts"

This tells Windows to *append* two more paths to the :var:`PATH` variable for
this session. Every file in those paths will now be available to you by their
name on the command line.

Now type the following and press Enter::

	PS> python -V

You should see your Python's version printed to the screen.

Recommended Libraries
=====================

You do not need to install or configure anything else to use Python.
Nevertheless, you should take the time to install the tools and libraries
described further below, which have become standard for many Python
developers. In particular, you should always install Distribute, as it
simplifies using other third-party Python libraries.

Distribute and Pip
------------------

Distribute is the most crucial third-party Python software you need. It
extends the packaging and installation facilities provided by the distutils in
the standard library. Once you add Distribute to your Python installation you
can download and install any compliant Python software product with a single
command. It also enables you to make your own Python software installable over
the network with very little work.

To obtain the latest version of Distribute for Windows, run the python script
available here: http://python-distribute.org/distribute_setup.py.

.. add instructions to download this easily with Powershell

You'll now have a new command available to you: **easy_install**. It is
considered by many to be deprecated, so we will install its replacement:
**pip**. Pip allows for uninstallation of packages, and is actively
maintained, unlike easy_install.

To install pip, simply open a command prompt and run::

    PS> easy_install pip


Virtualenv
----------

After Distribute and pip, the next development tool that you should install is
`virtualenv <http://pypi.python.org/pypi/virtualenv/>`_. Use pip for that::

    > pip install virtualenv

The virtualenv kit provides the ability to create virtual Python environments
that do not interfere with either each other, or the main Python installation.
If you install virtualenv before you begin coding then you can get into the
habit of using it to create completely clean Python environments for each
project. This is particularly important for web development, where each
framework and application will have many dependencies.

To set up a new Python environment, change the working directory to wherever
you want to store the environment, and run the virtualenv utility in your
project's directory::

    > virtualenv --distribute venv

.. TODO: Provide instructions for Powershell, not CMD.exe. I believe pip now
..		 includes an activate.ps1 script. But then we have the problem of
..	     blocked downloaded content with alternate streams... PS3 has a
..		 command to unlock bloecked files.

To use an environment, run the ``activate.bat`` batch file in the ``Scripts``
subdirectory of that environment. Your command prompt will change to show the
active environment. Once you have finished working in the current virtual
environment, run the ``deactivate.bat`` batch file to restore your settings to
normal.

Each new environment automatically includes a copy of ``pip`` in the
``Scripts`` subdirectory, so that you can setup the third-party libraries and
tools that you want to use in that environment. Put your own code within a
subdirectory of the environment, however you wish. When you no longer need a
particular environment, simply copy your code out of it, and then delete the
main directory for the environment.

PyWin32
-------

If you want to call into the Windows API or COM, you should install PyWin32,
which makes for a more Pythonic interface with those technologies.

--------------------------------

Parts of this page is a remixed version of `another guide`_ which is available
under the same license.

.. TODO: explain how to install precompiled extensions for windows.

.. _another guide: http://www.stuartellis.eu/articles/python-development-windows/
