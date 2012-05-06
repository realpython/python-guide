Code Style
==========

If you ask to Python programmers what they like the most in Python, they will
often say it is its high readability.  Indeed, a high level of readability of
the code is at the heart of the design of the Python language, following the
recognised fact that code is read much more often than it is written.

One reason for Python code to be easily read and understood is its relatively
complete set of Code Style guidelines and "Pythonic" idioms.

On the opposite, when a veteran Python developper (a Pythonistas) point to some
parts of a code and say it is not "Pythonic", it usually means that these lines
of code do not follow the common guidelines and fail to express the intent is
what is considered the best (hear: most readable) way.

On some border cases, no best way has been agreed upon on how to express
an intent in Python code, but these cases are rare.

General concepts
----------------

Explicit code
~~~~~~~~~~~~~

While any kind of black magic is possible with Python, the
most explicit and straightforward manner is preferred.

**Bad**

.. code-block:: python

    def make_complex(\*args):
        x, y = args
        return dict(\**locals())

**Good**

.. code-block:: python

    def make_complex(x, y):
        return {'x': x, 'y': y}

In the good code above, x and y are explicitely received from
the caller, and an explicit dictionary is returned. The developer
using this function knows exactly what to do by reading the
first and last lines, which is not the case with the bad example.

One statement per line
~~~~~~~~~~~~~~~~~~~~~~

While some compound statements such as list comprehensions are
allowed and appreciated for their brevity and their expressivity,
it is bad practice to have two disjoint statements on the same line.

**Bad**

.. code-block:: python

    print 'one'; print 'two'

    if x == 1: print 'one'

    if <complex comparison> and <other complex comparison>:
        # do something

**Good**

.. code-block:: python

    print 'one'
    print 'two'

    if x == 1:
        print 'one'

    cond1 = <complex comparison>
    cond2 = <other complex comparison>
    if cond1 and cond2:
        # do something


Avoid the magical wand
~~~~~~~~~~~~~~~~~~~~~~

A powerful tool for hackers, Python comes with a very rich set of hooks and
tools allowing to do almost any kind of tricky tricks. For instance, it is
possible to change how objects are created and instanciated, it is possible to
change how the Python interpreter imports modules, it is even possible (and
recommended if needed) to embed C routines in Python.

However, all these options have many drawbacks and it is always better to use
the most straightforward way to achieve your goal. The main drawback is that
readability suffers deeply from them. Many code analysis tools, such as pylint
or pyflakes, will be unable to parse this "magic" code.

We consider that a Python developer should know about these nearly infinite
possibilities, because it grows the confidence that no hard-wall will be on the
way.  However, knowing how to use them and particularly when **not** to use
them is the most important.

Like a Kungfu master, a pythonistas knows how to kill with a single finger, and
never do it.

We are all consenting adults
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As seen above, Python allows many tricks, and some of them are potentially
dangerous. A good example is that any client code can override an object's
properties and methods: There is no "private" keyword in Python. This
philosophy, very different from highly defensive languages like Java, which
give a lot of mechanism to prevent any misuse, is expressed by the saying: "We
are consenting adults".

This doesn't mean that, for example, no properties are considered private, and
that no proper encapsulation is possible in Python. But, instead of relying on
concrete walls erected by the developers between their code and other's, the
Python community prefers to rely on a set of convention indicating that these
elements should not be accessed directly.

The main convention for private properties and implementation details is to
prefix all "internals" with an underscore. If the client code breaks this rule
and access to these marked elements, any misbehavior or problems encountered if
the code is modified is the responsibility of the client code.

Using this convention generously is encouraged: any method or property that is
not intended to be used by client code should be prefixed with an underscore.
This will guarantee a better separation of duties and easier modifications of
existing code, and it will always be possible to publicize a private property,
while privatising a public property might be a much harder operation.

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

The ``enumerate`` function has better readability than handling a counter
manually. Moreover,
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

The ``with`` statement is better because it will ensure you always close the
file, even if an exception is raised.

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

Line Continuations
~~~~~~~~~~~~~~~~~~

When a logical line of code is longer than the accepted limit, you need to
split it over multiple physical lines. Python interpreter will join consecutive
lines if the last character of the line is a backslash. This is helpful
sometime but is preferably avoided, because of its fragility: a white space
added to the end of the line, after the backslash, will break the code and may
have unexpected results.

A prefered solution is to use parenthesis around your elements. Left with an
unclosed parenthesis on an end-of-line the Python interpreter will join the
next line until the parenthesis is closed. The same behavior holds for curly
and square braces.

**Bad**:

.. code-block:: python

    my_very_big_string = """For a long time I used to go to bed early. Sometimes, \
        when I had put out my candle, my eyes would close so quickly that I had not even \
        time to say “I’m going to sleep.”"""

    from some.deep.module.inside.a.module import a_nice_function, another_nice_function, \
        yet_another_nice_functio

**Good**:

.. code-block:: python

    my_very_big_string = ("For a long time I used to go to bed early. Sometimes, "
        "when I had put out my candle, my eyes would close so quickly that I had not even "
        "time to say “I’m going to sleep.”")

    from some.deep.module.inside.a.module import (a_nice_function, another_nice_function,
                                                  yet_another_nice_functio)

However, more often than not having to split long logical line is a sign that
you are trying to do too many things at the same time, which may hinder
readability.
