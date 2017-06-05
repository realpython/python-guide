Picking an Interpreter
======================

.. _which-python:

The State of Python (3 & 2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

When choosing a Python interpreter, one looming question is always present:
"Should I choose Python 2 or Python 3"? The answer is a bit more subtle than
one might think.


The basic gist of the state of things is as follows:

1. Most production applications today use Python 2.7.
2. Python 3 is ready for the production deployment of applications today.
3. Python 2.7 will only receive necessary security updates until 2020 [#pep373_eol]_.
4. The brand name "Python" encapsulates both Python 3 and Python 2.

Recommendations
~~~~~~~~~~~~~~~

I'll be blunt:

- Use Python 3 for new Python applications.
- If you're learning Python for the first time, familiarizing yourself with Python 2.7 will be very
  useful, but not more useful than learning Python 3.
- Learn both. They are both "Python".
- Software that is already built often depends on Python 2.7.
- If you are writing a new open source Python library, it's best to write it for both Python 2 and 3
  simultaneously. Only supporting Python 3 for a new library you want to be widely adopted is a
  political statement and will alienate many of your users. This is not a problem — slowly, over the next three years, this will become less the case.

So.... 3?
~~~~~~~~~

If you're choosing a Python interpreter to use, I
recommend you use the newest Python 3.x, since every version brings new and
improved standard library modules, security and bug fixes.

Given such, only use Python 2 if you have a strong reason to, such as a
pre-existing code-base, a Python 2 exclusive library, simplicity/familiarity,
or, of course, you absolutely love and are inspired by Python 2. No harm in that.

Check out `Can I Use Python 3? <https://caniusepython3.com/>`_ to see if any
software you're depending on will block your adoption of Python 3.

`Further Reading <http://wiki.python.org/moin/Python2orPython3>`_

It is possible to `write code that works on Python 2.6, 2.7, and Python 3
<https://docs.python.org/3/howto/pyporting.html>`_. This
ranges from trivial to hard depending upon the kind of software
you are writing; if you're a beginner there are far more important things to
worry about.

Implementations
~~~~~~~~~~~~~~~

When people speak of *Python* they often mean not just the language but also
the CPython implementation. *Python* is actually a specification for a language
that can be implemented in many different ways.

CPython
-------

`CPython <http://www.python.org>`_ is the reference implementation of Python,
written in C. It compiles Python code to intermediate bytecode which is then
interpreted by a virtual machine. CPython provides the highest
level of compatibility with Python packages and C extension modules.

If you are writing open-source Python code and want to reach the widest possible
audience, targeting CPython is best. To use packages which rely on C extensions
to function, CPython is your only implementation option.

All versions of the Python language are implemented in C because CPython is the
reference implementation.

PyPy
----

`PyPy <http://pypy.org/>`_ is a Python interpreter implemented in a restricted
statically-typed subset of the Python language called RPython. The interpreter
features a just-in-time compiler and supports multiple back-ends (C, CLI, JVM).

PyPy aims for maximum compatibility with the reference CPython implementation
while improving performance.

If you are looking to increase performance of your Python code, it's
worth giving PyPy a try. On a suite of benchmarks, it's currently `over 5 times
faster than CPython <http://speed.pypy.org/>`_.

PyPy supports Python 2.7. PyPy3 [#pypy_ver]_, released in beta, targets Python 3.

Jython
------

`Jython <http://www.jython.org/>`_ is a Python implementation that compiles
Python code to Java bytecode which is then executed by the JVM (Java Virtual Machine).
Additionally, it is able to import and use any Java class like a Python
module.

If you need to interface with an existing Java codebase or have other reasons to
need to write Python code for the JVM, Jython is the best choice.

Jython currently supports up to Python 2.7. [#jython_ver]_

IronPython
----------

`IronPython <http://ironpython.net/>`_  is an implementation of Python for the .NET
framework. It can use both Python and .NET framework libraries, and can also
expose Python code to other languages in the .NET framework.

`Python Tools for Visual Studio <http://ironpython.net/tools/>`_ integrates
IronPython directly into the Visual Studio development environment, making it
an ideal choice for Windows developers.

IronPython supports Python 2.7. [#iron_ver]_

PythonNet
---------

`Python for .NET <http://pythonnet.github.io/>`_ is a package which
provides near seamless integration of a natively installed Python
installation with the .NET Common Language Runtime (CLR).  This is the
inverse approach to that taken by IronPython (see above), to which it
is more complementary than competing with.

In conjunction with Mono, pythonnet enables native Python
installations on non-Windows operating systems, such as OS X and
Linux, to operate within the .NET framework.  It can be run in
addition to IronPython without conflict.

Pythonnet supports from Python 2.6 up to Python 3.5. [#pythonnet_ver1]_ [#pythonnet_ver2]_

.. [#pypy_ver] http://pypy.org/compat.html

.. [#jython_ver] https://hg.python.org/jython/file/412a8f9445f7/NEWS

.. [#iron_ver] http://ironpython.codeplex.com/releases/view/81726

.. [#pythonnet_ver1] https://travis-ci.org/pythonnet/pythonnet

.. [#pythonnet_ver2] https://ci.appveyor.com/project/TonyRoberts/pythonnet-480xs

.. [#pep373_eol] https://www.python.org/dev/peps/pep-0373/#id2
