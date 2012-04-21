Code Style
==========


Idioms
------

Idiomatic Python code is often referred to as being *Pythonic*.

.. _unpacking-ref:

Unpacking
~~~~~~~~~

If you know the length of a list or tuple, you can assign names to its
elements with unpacking:

.. code-block:: python

    for index, item in enumerate(some_list):
        # do something with index and item

You can use this to swap variables, as well:

.. code-block:: python

    a, b = b, a

Create an ignored variable
~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to assign something (for instance, in :ref:`unpacking-ref`) but
will not need that variable, use ``_``:

.. code-block:: python

    filename = 'foobar.txt'
    basename, _, ext = filename.rpartition()

.. note::

   "``_``" is commonly used as an alias for the :func:`~gettext.gettext`
   function. If your application uses (or may someday use) :mod:`gettext`,
   you may want to avoid using ``_`` for ignored variables, as you may
   accidentally shadow :func:`~gettext.gettext`.

Create a length-N list of the same thing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the Python list ``*`` operator:

.. code-block:: python

    four_nones = [None] * 4

Create a length-N list of lists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because lists are mutable, the ``*`` operator (as above) will create a list
of N references to the `same` list, which is not likely what you want.
Instead, use a list comprehension:

.. code-block:: python

    four_lists = [[] for _ in xrange(4)]



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

Conventions
:::::::::::

Here are some conventions you should follow to make your code easier to read.

Check if variable equals a constant
-----------------------------------

You don't need to explicitly compare a value to True, or None, or 0 - you can
just add it to the if statement. See `Truth Value Testing
<http://docs.python.org/library/stdtypes.html#truth-value-testing>`_ for a
list of what is considered false.

**Bad**:

.. code-block:: python

    if attr == True:
        print 'True!'

    if attr == None:
        print 'attr is None!'

**Good**:

.. code-block:: python

    # Just check the value
    if attr:
        print 'attr is truthy!'

    # or check for the opposite
    if not attr:
        print 'attr is falsey!'

    # or, since None is considered false, explicity check for it
    if attr is None:
        print 'attr is None!'

Access a Dictionary Element
---------------------------

Don't use the ``has_key`` function. Instead use ``x in d`` syntax, or pass
a default argument to ``get``.

**Bad**:

.. code-block:: python

    d = {'hello': 'world'}
    if d.has_key('hello'):
        print d['hello']    # prints 'world'
    else:
        print 'default_value'

**Good**:

.. code-block:: python

    d = {'hello': 'world'}

    print d.get('hello', 'default_value') # prints 'world'
    print d.get('thingy', 'default_value') # prints 'default_value'

    # Or:
    if 'hello' in d:
        print d['hello']

Short Ways to Manipulate Lists
------------------------------

`List comprehensions
<http://docs.python.org/tutorial/datastructures.html#list-comprehensions>`_
provide a powerful, concise way to work with lists. Also, the `map
<http://docs.python.org/library/functions.html#map>`_ and `filter
<http://docs.python.org/library/functions.html#filter>`_ functions can perform
operations on lists using a different concise syntax.

**Bad**:

.. code-block:: python

    # Filter elements greater than 4
    a = [3, 4, 5]
    b = []
    for i in a:
        if i > 4:
            b.append(i)

**Good**:

.. code-block:: python

    b = [i for i in a if i > 4]
    b = filter(lambda x: x > 4, a)

**Bad**:

.. code-block:: python

    # Add three to all list members.
    a = [3, 4, 5]
    count = 0
    for i in a:
        a[count] = i + 3
        count = count + 1

**Good**:

.. code-block:: python

    a = [3, 4, 5]
    a = [i + 3 for i in a]
    # Or:
    a = map(lambda i: i + 3, a)

Use `enumerate <http://docs.python.org/library/functions.html#enumerate>`_ to
keep a count of your place in the list.

.. code-block:: python

    for i, item in enumerate(a):
        print i + ", " + item
    # prints
    # 0, 3
    # 1, 4
    # 2, 5

The ``enumerate`` function has better readability than handling a counter manually. Moreover,
it is better optimized for iterators.

Read From a File
----------------

Use the ``with open`` syntax to read from files. This will automatically close
files for you.

**Bad**:

.. code-block:: python

    f = open('file.txt')
    a = f.read()
    print a
    f.close()

**Good**:

.. code-block:: python

    with open('file.txt') as f:
        for line in f:
            print line

The ``with`` statement is better because it will ensure you always close the file,
even if an exception is raised.

Returning Multiple Values from a Function
-----------------------------------------

Python supports returning multiple values from a function as a comma-separated
list, so you don't have to create an object or dictionary and pack multiple
values in before you return

**Bad**:

.. code-block:: python

    def math_func(a):
        return {'square': a ** 2, 'cube': a ** 3}

    d = math_func(3)
    s = d['square']
    c = d['cube']

**Good**:

.. code-block:: python

    def math_func(a):
        return a ** 2, a ** 3

    square, cube = math_func(3)

