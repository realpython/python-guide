Common Gotchas
==============

For the most part, Python aims to be a clean and consistent language that
avoid surprises, but there are a few cases where newcomers to the language
often get tripped up.

Some of these are intentional but potentially surprising. Some could arguably
be considered language warts. In general though, what follows is a collection
of potentially tricky behavior that might seem strange at first glance, but is
generally sensible once you're aware of the underlying cause for the surprise.


.. _default_args:

Mutable Default Arguments
-------------------------

Seemingly the *most* common surprise new Python programmers encounter is
Python's treatment of mutable default arguments in function definitions.

**What You Wrote**

.. code-block:: python

    def append_to(element, to=[]):
        to.append(element)
        return to

**What You Might Have Expected to Happen**

A new list is created each time the function is called if a second argument
isn't provided.

**What Does Happen**

A new list is created *once* when the function is defined, and the same list is
used in each successive call.

Python's default arguments are evaluated *once* when the function is defined,
not each time the function is called (like it is in say, Ruby). This means that
if you use a mutable default argument and mutate it, you *will* and have
mutated that object for all future calls to the function as well.

**What You Should Do Instead**

Create a new object each time the function is called, by using a default arg to
signal that no argument was provided (``None`` is often a good choice).

.. code-block:: python

    def append_to(element, to=None):
        if to is None:
            to = []
        to.append(element)
        return to


**When the Gotcha Isn't a Gotcha**

Sometimes you specifically can "exploit" (read: use as intended) this behavior
to maintain state between calls of a function. This is often done when writing
a caching function.


Late Binding Closures
---------------------

Another common source of confusion is the way Python binds its variables in
closures (or in the surrounding global scope).

**What You Wrote**

.. code-block:: python

    def create_adders():
        return [lambda x : i * x for i in range(5)]

**What You Might Have Expected to Happen**

A list containing five functions that each have their own closed-over ``i``
variable that multiplies their argument.

**What Does Happen**

Five functions are created, but all of them just multiply ``x`` by 4.

Python's closures are *late binding*. This means that names within closures are
looked up at the time the inner function is *called*.

Here, whenever *any* of the returned functions are called, the value of ``i``
is looked up in the surrounding scope at call time, when by then the loop has
completed and ``i`` is left with its final value of 4.

What's particularly nasty about this gotcha is the seemingly prevalent
misinformation that this has something to do with ``lambda``\s in Python.
Functions created with a ``lambda`` expression are in no way special, and in
fact the same exact behavior is exhibited by just using an ordinary ``def``:

.. code-block:: python

    def create_adders():
        for i in range(5):
            def adder(x):
                return i * x
            yield adder

**What You Should Do Instead**

Well. Here the general solution is arguably a bit of a hack. Due to Python's
afformentioned behavior concerning evaluating default arguments to functions
(see :ref:`default_args`), you can create a closure that binds immediately to
its arguments by using a default arg like so:

.. code-block:: python

    def create_adders():
        return [lambda x, i=i : i * x for i in range(5)]

**When the Gotcha Isn't a Gotcha**

When you want your closures to behave this way. Late binding is good in lots of
situations. Looping to create unique functions is unfortunately a case where
they can cause hiccups.
