Speed
=====

CPython, the most commonly used implementation of Python, is slow for CPU bound tasks. `PyPy`_ is fast.

Using a slightly modified version of `David Beazleys`_ CPU bound test code(added loop for multiple tests), you can see the difference between CPython and PyPy's processing.

::

   PyPy 
   $ ./pypy -V
   Python 2.7.1 (7773f8fc4223, Nov 18 2011, 18:47:10)
   [PyPy 1.7.0 with GCC 4.4.3]
   $ ./pypy measure2.py
   0.0683999061584
   0.0483210086823
   0.0388588905334
   0.0440690517426
   0.0695300102234

::

   CPython
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

`The GIL`_ (Global Interpreter Lock) is how Python allows multiple threads to operate at the same time. Python's
memory management isn't entirely thread-safe, so the GIL is requried to prevents multiple threads from running
the same Python code at once.

David Beazley has a great `guide`_ on how the GIL operates. He also covers the `new GIL`_ in Python 3.2. His
results show that maximizing performance in a Python application requires a strong understanding of the GIL,
how it affects your specific application, how many cores you have, and where your application bottlenecks are.

C Extentions
------------


The GIL
-------

`Special care`_ must be taken when writing C extensions to make sure you register your threads
with the interpreter.

C Extentions
::::::::::::


Cython
------


Pyrex
-----


Shedskin?
---------



Threading
:::::::::


Threading
---------


Spanwing Processes
------------------


Multiprocessing
---------------


.. _`PyPy`: http://pypy.org
.. _`The GIL`: http://wiki.python.org/moin/GlobalInterpreterLock
.. _`guide`: http://www.dabeaz.com/python/UnderstandingGIL.pdf
.. _`New GIL`: http://www.dabeaz.com/python/NewGIL.pdf
.. _`Special care`: http://docs.python.org/c-api/init.html#threads
.. _`David Beazleys`: http://www.dabeaz.com/GIL/gilvis/measure2.py
