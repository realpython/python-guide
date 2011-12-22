Testing Your Code
=====================

Testing your code is very important.


The Basics
::::::::::


Unittest
--------

Unittest is the batteries-included test module in the Python standard library.
Its API will be familiar to anyone who has used any of the JUnit/nUnit/CppUnit
series of tools.

Creating testcases is accomplished by subclassing a TestCase base class

::

    import unittest

    def fun(x):
        return x + 1

    class MyTest(unittest.TestCase):
        def test(self):
            self.assertEqual(fun(3), 4)

As of Python 2.7 unittest also includes its own test discovery mechanisms.

    `unittest in the standard library documentation <http://docs.python.org/library/unittest.html>`_


Doctest
-------

The doctest module searches for pieces of text that look like interactive Python
sessions, and then executes those sessions to verify that they work exactly as
shown.


Tools
:::::


py.test
-------

py.test is a no-boilerplate alternative to Python's standard unittest module.

::

    $ pip install pytest

Despite being a fully-featured and extensible test tool it boasts a simple 
syntax. Creating a test suite is as easy as writing a module with a couple of
functions

::

    # content of test_sample.py
    def func(x):
        return x + 1

    def test_answer():
        assert func(3) == 5

and then running the `py.test` command

::

    $ py.test
    =========================== test session starts ============================
    platform darwin -- Python 2.7.1 -- pytest-2.2.1
    collecting ... collected 1 items

    test_sample.py F

    ================================= FAILURES =================================
    _______________________________ test_answer ________________________________

        def test_answer():
    >       assert func(3) == 5
    E       assert 4 == 5
    E        +  where 4 = func(3)

    test_sample.py:5: AssertionError
    ========================= 1 failed in 0.02 seconds =========================

far less work than would be required for the equivalent functionality with the
unittest module!

    `py.test <http://pytest.org/latest/>`_


Nose
----

nose extends unittest to make testing easier.


::

    $ pip install nose

nose provides automatic test discovery to save you the hassle of manually
creating test suites. It also provides numerous plugins for features such as
xUnit-compatible test output, coverage reporting, and test selection.

    `nose <http://readthedocs.org/docs/nose/en/latest/>`_


tox
---

tox is a tool for automating test environment management and testing against multiple
interpreter configurations

::

    $ pip install tox

tox allows you to configure complicatated multi-parameter test matrices via a
simple ini-style configuration file.

    `tox <http://tox.testrun.org/latest/>`_

Unittest2
---------

unittest2 is a a backport of Python 2.7's unittest module which has an improved
API and better assertions over the one available in previous versions of Python.

If you're using Python 2.6 or below, you can install it with pip

::

    $ pip install unittest2

You may want to import the module under the name unittest to make porting code
to newer versions of the module easier in the future

::

    import unittest2 as unittest

    class MyTest(unittest.TestCase):
        ...

This way if you ever switch to a newer python version and no longer need the
unittest2 module, you can simply change the import in your test module without
the need to change any other code.

    `unittest2 <http://pypi.python.org/pypi/unittest2>`_


