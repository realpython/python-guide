=======================
Scientific Applications
=======================

Context
:::::::

Python is frequently used for high-performance scientific applications. Python
is widely used in academia and scientific projects because it is easy to write,
and it performs really well.

Due to its high performance nature, scientific computing in python often refers
to external libraries, typically written in faster languages (like C, or
FORTRAN for matrix operations). The main libraries used are `NumPy`_, `SciPy`_
and `Matplotlib`_. Going into detail about these libraries is beyond the scope
of the Python guide. However, a comprehensive introduction to the scientific
Python ecosystem can be found in the `Python Scientific Lecture Notes
<http://scipy-lectures.github.com/>`_

Libraries
:::::::::

NumPy
-----

`NumPy <http://numpy.scipy.org/>`_ is a low level library written in C (and
FORTRAN) for high level mathematical functions. NumPy cleverly overcomes the
problem of running slower algorithms on Python by using multidimensional arrays
and functions that operate on arrays. Any algorithm can then be expressed as a
function on arrays, allowing the algorithms to be run quickly.


NumPy is part of the SciPy project, and is released as a separate library so
people who only need the basic requirements can just use NumPy.

NumPy is compatible with Python versions 2.4 through to 2.7.2 and 3.1+.

Numba
-----
Numba is an Numpy aware Python compiler (just-in-time (JIT) specializing 
compiler) which compiles annotated Python (and Numpy) code to LLVM (Low Level 
Virtual Machine) (through special decorators). 
Briefly, Numba using system that compiles Python code with LLVM to code which 
can be natively executed at runtime.

.. todo:: Write about Numba

SciPy
-----

`SciPy <http://scipy.org/>`_ is a library that uses Numpy for more mathematical
functions. SciPy uses NumPy arrays as the basic data structure. SciPy comes
with modules for various commonly used tasks in scientific programing, for
example: linear algebra, integration (calculus), ordinary differential equation
solvers and signal processing.

Matplotlib
----------

`Matplotlib <http://matplotlib.sourceforge.net/>`_ is a flexible plotting
library for creating interactive 2D and 3D plots that can also be saved as
manuscript-quality figures.  The API in many ways reflects that of `MATLAB
<http://www.mathworks.com/products/matlab/>`_, easing transition of MATLAB
users to Python.  Many examples, along with the source code to re-create them,
can be browsed at the `matplotlib gallery
<http://matplotlib.sourceforge.net/gallery.html>`_.

Resources
:::::::::

Installation of scientific  Python packages can be troublesome. Many of these
packages are implemented as Python C extensions which need to be compiled.
This section lists various so-called scientific Python distributions which
provide precompiled and easy-to-install collections of scientific Python
packages.

Unofficial Windows Binaries for Python Extension Packages
---------------------------------------------------------

Many people who do scientific computing are on Windows. And yet many of the
scientific computing packages are notoriously difficult to build and install.
`Christoph Gohlke <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_ however, has
compiled a list of Windows binaries for many useful Python packages. The list
of packages has grown from a mainly scientific python resource to a more
general list. It might be a good idea to check it out if you're on Windows.

Enthought Python Distribution (EPD)
-----------------------------------

Installing NumPy and SciPy can be a daunting task. Which is why the
`Enthought Python distribution <http://enthought.com/>`_ was created. With
Enthought, scientific python has never been easier (one click to install about
100 scientific python packages). The Enthought Python Distribution comes in two
variants: a free version `EPD Free <http://enthought.com/products/epd_free.php>`_
and a paid version with various `pricing options.
<http://enthought.com/products/epd_sublevels.php>`_

Anaconda
--------

`Continuum Analytics <http://continuum.io/>`_ offers the `Anaconda
Python Distribution <https://store.continuum.io/cshop/anaconda>`_ which
includes all the common scientific python packages and additionally many
packages related to data analytics and big data. Anaconda comes in two
flavors, a paid for version and a completely free and open source community
edition, Anaconda CE, which contains a slightly reduced feature set. Free
licenses for the paid-for version are available for academics and researchers.
