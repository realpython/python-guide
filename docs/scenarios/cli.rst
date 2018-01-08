Command-line Applications
=========================

.. image:: https://farm5.staticflickr.com/4272/34435690330_11930b5987_k_d.jpg

Command-line applications, also referred to as
`Console Applications <http://en.wikipedia.org/wiki/Console_application>`_,
are computer programs designed to be used from a text interface, such as a
`shell <http://en.wikipedia.org/wiki/Shell_(computing)>`_. Command-line
applications usually accept various inputs as arguments, often referred to as
parameters or sub-commands, as well as options, often referred to as flags or
switches.

Some popular command-line applications include:

* `Grep <http://en.wikipedia.org/wiki/Grep>`_ - A plain-text data search utility
* `curl <http://curl.haxx.se/>`_ - A tool for data transfer with URL syntax
* `httpie <https://github.com/jakubroztocil/httpie>`_ - A command line HTTP
  client, a user-friendly cURL replacement
* `git <http://git-scm.com/>`_ - A distributed version control system
* `mercurial <https://www.mercurial-scm.org/>`_ - A distributed version control
  system primarily written in Python

Clint
-----

`clint <https://pypi.python.org/pypi/clint/>`_ is a Python module which is
filled with very useful tools for developing command-line applications.
It supports features such as; CLI colors and indents, simple and powerful
column printer, iterator based progress bars and implicit argument handling.

Click
-----

`click <http://click.pocoo.org/>`_ is a Python package for creating
command-line interfaces in a composable way with as little code as
possible. This “Command-line Interface Creation Kit” is highly
configurable but comes with good defaults out of the box.

docopt
------

`docopt <http://docopt.org/>`_ is a lightweight, highly Pythonic package that
allows creating command-line interfaces easily and intuitively, by parsing
POSIX-style usage instructions.

Plac
------

`Plac <https://pypi.python.org/pypi/plac>`_ is a simple wrapper
over the Python standard library `argparse <http://docs.python.org/2/library/argparse.html>`_,
which hides most of its complexity by using a declarative interface: the
argument parser is inferred rather than written down by imperatively. This
module targets especially unsophisticated users, programmers, sys-admins,
scientists and in general people writing throw-away scripts for themselves,
who choose to create a command-line interface because it is quick and simple.

Cliff
------

`Cliff <http://docs.openstack.org/developer/cliff/>`_  is a framework for
building command-line programs. It uses setuptools entry points to provide
subcommands, output formatters, and other extensions. The framework is meant
to be used to create multi-level commands such as subversion and git, where
the main program handles some basic argument parsing and then invokes a
sub-command to do the work.

Cement
------

`Cement <http://builtoncement.com/>`_ is an advanced CLI Application Framework. 
Its goal is to introduce a standard, and feature-full platform
for both simple and complex command line applications as well
as support rapid development needs without sacrificing quality. 
Cement is flexible, and it's use cases span from the simplicity of a micro-framework 
to the complexity of a meg-framework. 
