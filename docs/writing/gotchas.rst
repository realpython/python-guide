Common Gotchas
==============

For the most part, Python aims to be a clean and consistent language that
avoid surprises, but there are a few cases where newcomers to the language
often get tripped up.

Some of these are intentional but surprising. Some could arguably be considered
language warts. In general though, what follows is a collection of potentially
tricky behavior that might seem strange at first glance, but is generally
sensible despite surprise after learning of its existence.


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
