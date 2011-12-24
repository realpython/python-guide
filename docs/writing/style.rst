Code Style
==========


Idioms
::::::

Idiomatic Python code is often referred to as being *pythonic*.


Zen of Python
-------------

Also known as PEP 20, the guiding principles for Python's design.

::

    >>> import this

See `<http://stackoverflow.com/questions/228181/the-zen-of-python>`_ for some
examples.

PEP 8
-----

PEP 8 is the de-facto code style guide for Python.

    `PEP 8 <http://www.python.org/dev/peps/pep-0008/>`_

There exists a command-line program, `pep8` that can check your code for
conformance.

::

    pip install pep8


Simply run it on a file or series of files and get a report of any
violations

::

    $ pep8 optparse.py
    optparse.py:69:11: E401 multiple imports on one line
    optparse.py:77:1: E302 expected 2 blank lines, found 1
    optparse.py:88:5: E301 expected 1 blank line, found 0
    optparse.py:222:34: W602 deprecated form of raising exception
    optparse.py:347:31: E211 whitespace before '('
    optparse.py:357:17: E201 whitespace after '{'
    optparse.py:472:29: E221 multiple spaces before operator
    optparse.py:544:21: W601 .has_key() is deprecated, use 'in'

Conforming your style to PEP 8 is generally a good idea and helps make code a lot
more consistent when working on projects with other developers.
