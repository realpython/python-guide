Code Style
==========


Idioms
::::::

Idiomatic Python code is often referred to as being *pythonic*.

A common idiom for creating strings is to use `join <http://docs.python.org/library/string.html#string.join>`_ on an empty string.::

    letters = ['s', 'p', 'a', 'm']
    word = ''.join(letters)

This will set the value of the variable *word* to 'spam'. This idiom can be applied to lists and tuples.

Sometimes we need to search through a collection of things. Let's look at two options: lists and dictionaries.

Take the following code for example::
    
    d = {'s': [], 'p': [], 'a': [], 'm': []}
    l = ['s', 'p', 'a', 'm']
    
    def lookup_dict(d):
        return 's' in d

    def lookup_list(l):
        return 's' in l

Even though both functions look identical, because *lookup_dict* is utilizing the fact that dictionaries in python are hashtables, the lookup performance between the two is very different.
Python will have to go through each item in the list to find a matching case, which is time consuming. By analysing the hash of the dictionary finding keys in the dict can be done very quickly.
For more information see this `StackOverflow <http://stackoverflow.com/questions/513882/python-list-vs-dict-for-look-up-table>`_ page.

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
