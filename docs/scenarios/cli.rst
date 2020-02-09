
#########################
Command-line Applications
#########################

.. image:: /_static/photos/34435690330_11930b5987_k_d.jpg

Command-line applications, also referred to as `Console Applications
<http://en.wikipedia.org/wiki/Console_application>`_, are computer programs
designed to be used from a text interface, such as a `shell
<http://en.wikipedia.org/wiki/Shell_(computing)>`_. Command-line applications
usually accept various inputs as arguments, often referred to as parameters or
sub-commands, as well as options, often referred to as flags or switches.

Some popular command-line applications include:

* `grep <http://en.wikipedia.org/wiki/grep>`_ - A plain-text data search utility
* `curl <http://curl.haxx.se/>`_ - A tool for data transfer with URL syntax
* `httpie <https://github.com/jakubroztocil/httpie>`_ - A command-line HTTP
  client, a user-friendly cURL replacement
* `Git <http://git-scm.com/>`_ - A distributed version control system
* `Mercurial <https://www.mercurial-scm.org/>`_ - A distributed version control
  system primarily written in Python


*****
Click
*****

`click <https://click.palletsprojects.com>`_ is a Python package for creating
command-line interfaces in a composable way with as little code as possible.
This “Command-Line Interface Creation Kit” is highly configurable but comes
with good defaults out of the box.


******
docopt
******

`docopt <http://docopt.org/>`_ is a lightweight, highly Pythonic package that
allows creating command-line interfaces easily and intuitively, by parsing
POSIX-style usage instructions.


****
Plac
****

`Plac <https://pypi.org/project/plac>`_ is a simple wrapper
over the Python standard library `argparse <http://docs.python.org/2/library/argparse.html>`_,
which hides most of its complexity by using a declarative interface: the
argument parser is inferred rather than written down imperatively. This
module targets unsophisticated users, programmers, sysadmins,
scientists, and in general people writing throw-away scripts for themselves,
who choose to create a command-line interface because it is quick and simple.


*****
Cliff
*****

`Cliff <http://docs.openstack.org/developer/cliff/>`_  is a framework for
building command-line programs. It uses setuptools entry points to provide
subcommands, output formatters, and other extensions. The framework is meant
to be used to create multi-level commands such as ``svn`` and ``git``, where
the main program handles some basic argument parsing and then invokes a
sub-command to do the work.


******
Cement
******

`Cement <http://builtoncement.com/>`_ is an advanced CLI Application
Framework. Its goal is to introduce a standard and feature-full platform for
both simple and complex command line applications as well as support rapid
development needs without sacrificing quality. Cement is flexible, and its use
cases span from the simplicity of a micro-framework to the complexity of a
mega-framework.


***********
Python Fire
***********

`Python Fire <https://github.com/google/python-fire/>`_ is a library for
automatically generating command-line interfaces from absolutely any Python
object. It can help debug Python code more easily from the command line,
create CLI interfaces to existing code, allow you to interactively explore
code in a REPL, and simplify transitioning between Python and Bash (or any
other shell).
