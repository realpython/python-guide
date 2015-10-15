Speed
=====

CPython, the most commonly used implementation of Python, is slow for CPU bound
tasks. `PyPy`_ is fast.

Using a slightly modified version of `David Beazleys`_ CPU bound test code
(added loop for multiple tests), you can see the difference between CPython
and PyPy's processing.

.. code-block:: console

   # PyPy
   $ ./pypy -V
   Python 2.7.1 (7773f8fc4223, Nov 18 2011, 18:47:10)
   [PyPy 1.7.0 with GCC 4.4.3]
   $ ./pypy measure2.py
   0.0683999061584
   0.0483210086823
   0.0388588905334
   0.0440690517426
   0.0695300102234

.. code-block:: console

   # CPython
   $ ./python -V
   Python 2.7.1
   $ ./python measure2.py
   1.06774401665
   1.45412397385
   1.51485204697
   1.54693889618
   1.60109114647

Context
:::::::


The GIL
-------

`The GIL`_ (Global Interpreter Lock) is how Python allows multiple threads to
operate at the same time. Python's memory management isn't entirely thread-safe,
so the GIL is required to prevent multiple threads from running the same
Python code at once.

David Beazley has a great `guide`_ on how the GIL operates. He also covers the
`new GIL`_ in Python 3.2. His results show that maximizing performance in a
Python application requires a strong understanding of the GIL, how it affects
your specific application, how many cores you have, and where your application
bottlenecks are.

C Extensions
------------


The GIL
-------

`Special care`_ must be taken when writing C extensions to make sure you
register your threads with the interpreter.

C Extensions
::::::::::::


Cython
------

`Cython <http://cython.org/>`_ implements a superset of the Python language
with which you are able to write C and C++ modules for Python. Cython also
allows you to call functions from compiled C libraries. Using Cython allows
you to take advantage of Python's strong typing of variables and operations.

Here's an example of strong typing with Cython:

.. code-block:: cython

    def primes(int kmax):
    """Calculation of prime numbers with additional
    Cython keywords"""

        cdef int n, k, i
        cdef int p[1000]
        result = []
        if kmax > 1000:
            kmax = 1000
        k = 0
        n = 2
        while k < kmax:
            i = 0
            while i < k and n % p[i] != 0:
                i = i + 1
            if i == k:
                p[k] = n
                k = k + 1
                result.append(n)
            n = n + 1
        return result


This implementation of an algorithm to find prime numbers has some additional
keywords compared to the next one, which is implemented in pure Python:

.. code-block:: python

    def primes(kmax):
    """Calculation of prime numbers in standard Python syntax"""

        p= range(1000)
        result = []
        if kmax > 1000:
            kmax = 1000
        k = 0
        n = 2
        while k < kmax:
            i = 0
            while i < k and n % p[i] != 0:
                i = i + 1
            if i == k:
                p[k] = n
                k = k + 1
                result.append(n)
            n = n + 1
        return result

Notice that in the Cython version you declare integers and integer arrays
to be compiled into C types while also creating a Python list:


.. code-block:: cython

    def primes(int kmax):
        """Calculation of prime numbers with additional
        Cython keywords"""

        cdef int n, k, i
        cdef int p[1000]
        result = []


.. code-block:: python

    def primes(kmax):
        """Calculation of prime numbers in standard Python syntax"""

        p= range(1000)
        result = []

What is the difference? In the upper Cython version you can see the
declaration of the variable types and the integer array in a similar way as
in standard C. For example `cdef int n,k,i` in line 3. This additional type
declaration (i.e. integer) allows the Cython compiler to generate more
efficient C code from the second version. While standard Python code is saved
in :file:`*.py` files, Cython code is saved in :file:`*.pyx` files.

What's the difference in speed? Let's try it!

.. code-block:: python

	import time
	#activate pyx compiler
	import pyximport
	pyximport.install()
	#primes implemented with Cython
	import primesCy
	#primes implemented with Python
	import primes

	print "Cython:"
	t1= time.time()
	print primesCy.primes(500)
	t2= time.time()
	print "Cython time: %s" %(t2-t1)
	print ""
	print "Python"
	t1= time.time()
	print primes.primes(500)
	t2= time.time()
	print "Python time: %s" %(t2-t1)


These lines both need a remark:

.. code-block:: python

    import pyximport
    pyximport.install()


The `pyximport` module allows you to import :file:`*.pyx` files (e.g.,
:file:`primesCy.pyx`) with the Cython-compiled version of the `primes`
function. The `pyximport.install()` command allows the Python interpreter to
start the Cython compiler directly to generate C-code, which is automatically
compiled to a :file:`*.so` C-library. Cython is then able to import this
library for you in your Python code, easily and efficiently. With the
`time.time()` function you are able to compare the time between these 2
different calls to find 500 prime numbers. On a standard notebook (dual core
AMD E-450 1.6 GHz), the measured values are:

.. code-block:: console

    Cython time: 0.0054 seconds

    Python time: 0.0566 seconds


And here the output of an embedded `ARM beaglebone <http://beagleboard.org/Products/BeagleBone>`_ machine:

.. code-block:: console

    Cython time: 0.0196 seconds

    Python time: 0.3302 seconds


Pyrex
-----

Pyrex is a Python-like language for rapidly and easily writing python extension modules. It can be described as python with C data types. With Pyrex, one can produce Python-like code that runs as fast as in C, with easy access to C libraries and functions.

The Pyrex homepage is at http://www.cosc.canterbury.ac.nz/~greg/python/Pyrex/

The two main uses of Pyrex are:

To speed up the execution of Python code
To provide a Python interface to existing C modules/libraries

There is an enhanced fork of Pyrex, called Cython. It features substantial performance optimisations and improved support for newer Python language features.

PyrexOnWindows provides a step-by-step guide to Pyrex installation on Windows.

pyrexdoc is a tool for generating HTML documentation from a compiled Pyrex module, by DavidMcNab. See other DocumentationTools.

If you are looking for speed improvement, you may also want to consider other Python speedup solutions such as psyco and weave.

For accessing existing C libraries, the ctypes module is also available in Python 2.5 and above.


Shedskin?
---------
Shed Skin is a Python to C++ programming language compiler. It is experimental, and can translate pure, but implicitly statically typed Python programs into optimized C++. It can generate stand-alone programs or extension modules that can be imported and used in larger Python programs.

Shed Skin is an open source project with contributions from many people, however the main author is Mark Dufour. Work has been going into Shed Skin since 2005.

Besides the typing restriction,programs cannot freely use the Python standard library, although about 20 common modules, such as random, itertools and re (regular expressions), are supported as of 2011. Also, not all Python features, such as nested functions and variable numbers of arguments, are supported. Many introspective dynamic parts of the language are unsupported. For example, functions like getattr, and hasattr are unsupported.

As of May 2011, Unicode is not supported.

For a set of 54 non-trivial test programs (at over 15,000 lines in total (sloccount)), measurements show a typical speedup of 2-20 times over Psyco, and 2-200 times over CPython. Shed Skin is still in an early stage of development, so many other programs will not compile unmodified.

Shed Skin can be used to generate standalone executables which need only the C++ runtime libraries. It can also be used to generate CPython modules. This allows compiling parts of larger programs with Shed Skin, while running the other parts using regular CPython.

Another use has been to wrap C++ classes using Shed Skin to allow C++ classes to be used as Python classes.

The license of the Shed Skin source code is under two parts. The main compiler code is under the GNU General Public License (GPL). The supporting code that it uses as a run time library is under a BSD or MIT license depending on the module. This allows compiling programs which are considered under the GPL or are not considered under the GPL.

Numba
-----
Numba is an Open Source NumPy-aware optimizing compiler for Python sponsored by Continuum Analytics, Inc. It uses the remarkable LLVM compiler infrastructure to compile Python syntax to machine code.

It is aware of NumPy arrays as typed memory regions and so can speed-up code using NumPy arrays. Other, less well-typed code will be translated to Python C-API calls effectively removing the "interpreter" but not removing the dynamic indirection.

Numba is also not a tracing JIT. It compiles your code before it gets run either using run-time type information or type information you provide in the decorator.

Numba is a mechanism for producing machine code from Python syntax and typed data structures such as those that exist in NumPy.
Numba gives you the power to speed up your applications with high performance functions written directly in Python. With a few annotations, array-oriented and math-heavy Python code can be just-in-time compiled to native machine instructions, similar in performance to C, C++ and Fortran, without having to switch languages or Python interpreters.

Numba works by generating optimized machine code using the LLVM compiler infrastructure at import time, runtime, or statically (using the included pycc tool). Numba supports compilation of Python to run on either CPU or GPU hardware, and is designed to integrate with the Python scientific software stack.
Example :
---------
from numba import jit
from numpy import arange

# jit decorator tells Numba to compile this function.
# The argument types will be inferred by Numba when function is called.
@jit
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result

a = arange(9).reshape(3,3)
print(sum2d(a))

Installing:
-----------
The easiest way to install numba and get updates is by using the Anaconda Distribution: https://store.continuum.io/cshop/anaconda/

$ conda install numba
If you wanted to compile Numba from source, it is recommended to use conda environment to maintain multiple isolated development environments. To create a new environment for Numba development:

$ conda create -p ~/dev/mynumba python numpy llvmlite
To select the installed version, append "=VERSION" to the package name, where, "VERSION" is the version number. For example:

$ conda create -p ~/dev/mynumba python=2.7 numpy=1.6 llvmlite
to use Python 2.7 and Numpy 1.6.

If you need CUDA support, you should also install the CUDA toolkit:

$ conda install cudatoolkit 

Threading
:::::::::


Threading
---------


Spawning Processes
------------------


Multiprocessing
---------------


.. _`PyPy`: http://pypy.org
.. _`The GIL`: http://wiki.python.org/moin/GlobalInterpreterLock
.. _`guide`: http://www.dabeaz.com/python/UnderstandingGIL.pdf
.. _`New GIL`: http://www.dabeaz.com/python/NewGIL.pdf
.. _`Special care`: http://docs.python.org/c-api/init.html#threads
.. _`David Beazleys`: http://www.dabeaz.com/GIL/gilvis/measure2.py
