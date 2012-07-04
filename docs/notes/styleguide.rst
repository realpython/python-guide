.. _guide-style-guide:

=====================
The Guide Style Guide
=====================

As with all documentation, having a consistent formating helps make the
document more understandable. In order to make The Guide easier to digest,
all contributions should fit within the rules of this style guide where
appropriate.

The Guide is written as :ref:`restructuredtext-ref`.

.. note:: Parts of The Guide may not yet match this style guide. Feel free
   to update those parts to be in sync with The Guide Style Guide

.. note:: On any page of the rendered HTML you can click "Show Source" to
   see how authors have styled the page.

Relevancy
---------

Strive to keep any contributions relevant to the :ref:`purpose of The Guide
<about-ref>`.

* Avoid including too much information on subjects that don't directly
  relate to Python development.
* Prefer to link to other sources if the information is already out there.
  Be sure to describe what and why you are linking.
* `Cite <http://sphinx.pocoo.org/rest.html?highlight=citations#citations>`_
  references where needed.
* If a subject isn't directly relevant to Python, but useful in conjunction
  with Python (ex: Git, Github, Databases), reference by linking to useful
  resources and describe why it's useful to Python.
* When in doubt, ask.

Headings
--------

Use the following styles for headings.

Chapter title::

    #########
    Chapter 1
    #########

Page title::

    ===================
    Time is an Illusion
    ===================

Section headings::

    Lunchtime Doubly So
    -------------------

Sub section headings::

    Very Deep
    ~~~~~~~~~

Prose
-----

Wrap text lines at 78 characters. Where necessary, lines may exceed 78
characters, especially if wrapping would make the source text more difficult
to read.


Code Examples
-------------

Wrap all code examples at 70 characters to avoid horizontal scrollbars.

Command line examples::

    .. code-block:: console

        $ run command --help
        $ ls ..

Be sure to include the ``$`` prefix before each line.

Python interpreter examples::

    Label the example::

    .. code-block:: python

        >>> import this

Python examples::

    Descriptive title::

    .. code-block:: python

        def get_answer():
            return 42

Externally Linking
------------------

* Prefer labels for well known subjects (ex: proper nouns) when linking::

    Sphinx_ is used to document Python.

    .. _Sphinx: http://sphinx.pocoo.org

* Prefer to use descriptive labels with inline links instead of leaving bare
  links::

    Read the `Sphinx Tutorial <http://sphinx.pocoo.org/tutorial.html>`_

* Avoid using labels such as "click here", "this", etc. preferring
  descriptive labels (SEO worthy) instead.

Linking to Sections in The Guide
--------------------------------

To cross-reference other parts of this documentation, use the `:ref:
<http://sphinx.pocoo.org/markup/inline.html#cross-referencing-arbitrary-locations>`_
keyword and labels.

To make reference labels more clear and unique, always add a ``-ref`` suffix::

    .. _some-section-ref:

    Some Section
    ------------

Notes and Warnings
------------------

Make use of the appropriate `admonitions directives
<http://sphinx.pocoo.org/rest.html#directives>`_ when making notes.

Notes::

    .. note::
        The Hitchhiker’s Guide to the Galaxy has a few things to say
        on the subject of towels. A towel, it says, is about the most
        massively useful thing an interstellar hitch hiker can have.

Warnings::

    .. warning:: DON'T PANIC

TODOs
-----

Please mark any incomplete areas of The Guide with a `todo directive
<http://sphinx.pocoo.org/ext/todo.html?highlight=todo#directive-todo>`_. To
avoid cluttering the :ref:`todo-list-ref`, use a single ``todo`` for stub
documents or large incomplete sections.

::

    .. todo::
        Learn the Ultimate Answer to the Ultimate Question
        of Life, The Universe, and Everything

