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
    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

For some examples of good Python style, see `this Stack Overflow question
<http://stackoverflow.com/questions/228181/the-zen-of-python>`_ or `these
slides from a Python user group
<http://artifex.org/~hblanks/talks/2011/pep20_by_example.pdf>`_.

PEP 8
-----

PEP 8 is the de-facto code style guide for Python.

    `PEP 8 <http://www.python.org/dev/peps/pep-0008/>`_

Conforming your Python code to PEP 8 is generally a good idea and helps make
code more consistent when working on projects with other developers. There
exists a command-line program, `pep8 <https://github.com/jcrocholl/pep8>`_,
that can check your code for conformance. Install it by running the following
command in your Terminal:

::

    $ pip install pep8


Then run it on a file or series of files to get a report of any violations.

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

