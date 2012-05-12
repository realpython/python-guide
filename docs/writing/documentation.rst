Documenting Your Code
=====================

With readability of the code being a main focus for Python developers, proper
commenting is naturally important. Some best practice apply to code comments
and project documents, depending on the scope of the project.

Project documents
-----------------

A README file at the root directory give general information to the users and
the maintainers. It should be raw text or written in some very easy to read
markup, such as reStructuredText and Markdown. It should contain a few lines
explaining the purpose of the project or the library (without assuming the user
knows anything about the project), the url of the main source for the software,
and some basic credit information. This file is the main entry point for
readers of the code.

An INSTALL file is less often necessary with python, except if the dependencies
are complex or unusual, or if some C modules need to be compiled before use.
The installation instructions are often reduced to one command, such as ``pip
install module`` or ``python setup.py install`` and added to the README file.

A LICENSE file should always be present and specify the license under which the
software is made available to the public.

A TODO file or a TODO section in README should list the planned modifications
of the code.

A CHANGELOG file or section in README should compile a short overview of the
changes in the code base for the latest versions.

Documentation
-------------

As the project or library reaches a certain level of complexity, it may require
a fuller documentation, which can be of different flavors:

The introduction may show a very short overview of what can be done with the
product, using one or two extremely simplified use cases.

The tutorials will show in more details some main use cases. The reader will
follow a step-by-step procedure to set-up a working prototype.

The API reference, which is often generated automatically from the code, will
list all publicly available interfaces, their parameters and their return
values, with an explanation of their use.

Some documents intended for developers might give guidance about code
convention and general design decision of the project.

Comments
--------

Comments are written directly inside the code, either using the hash sign (#)
or a docstring_.

Finding the correct balance between undocumented code and verbose and useless
comment boilerplates is difficult, and is the subject of heated discussion
among developers.

The following guidelines seem to be most commonly agreed upon:

**Wrong or outdated comments are worse than no comments at all.** Following the
saying that it is better, on a boat, to know that we do not know were we are
than to wrongly believe we know where we are, wrong or outdated comments can be
misleading for the maintainers, slow down considerably bug hunting or
refactoring, and then, when discovered wrong, they will throw suspicion on all
other comments in the code, regardless of their individual correctness.

**No need comments for perfect code...** An hypothetical perfectly readable
code, with a crystal clear logic stream, expressive variable and function
names, orthogonal segmentation passing exactly between the flesh and the bones,
and no implicit assumptions of any kind, would not require any comment at all.
When striving for coding excellence, it is useful to see any existing comment,
or any feeling of a need for a comment, as the sign that the code do not
express clearly enough its intent and can be improved.

**.. but no code is perfect.**  Perfect code is a chimere, it exists only in
our dreams.  In real life, a code base is full of trade offs, and comments are
often needed in the most difficult parts. Moreover, any special case, any
obscure hack, any monkey patch and any ugly workaround MUST be signaled and
explained by a proper comment. This should be enforced by the law!

**TODOs** are special comments that a developer write as a reminder for later
use. It is said that its original intent was that someone might, one day,
search for the string "TODO" in the code base and actually roll their sleeves
and start *to do the TODOs*. There is no avalaible record that it ever
happened. However, TODOs comment are still very useful, because they mark the
current limits of the code, and it is not unlikely that, when required to add a
new behavior to the actual code, looking at the TODOs will show where to start.

**Do not use triple-quote strings to comment code.** A common operation when
modifiying code is to comment out some lines or even a full function or class
definition. This can be done by adding triple-quotes around the code block to
be skipped, but this is not a good pratice, because line-oriented command-line
tools such as ``grep`` will not be aware that the commented code is inactive.
It is better to add hashes at the proper indentation level for every commented
line. Good editors allow to do this with few keystrokes (ctrl-v on Vim).

**Bad**

.. code-block:: python

    def tricky_function():
        '''
        Commented out because its breaks something.
        if foo:
            do_bar()
        '''
        return baz

    def tricky_function():
        # Commented out because its breaks something.
        #if foo:
            #do_bar()
        return baz


    def tricky_function():
    # Commented out because its breaks something.
    #   if foo:
    #       do_bar()
        return baz

**Good**

.. code-block:: python

    def tricky_function():
        # Commented out because its breaks something.
        #if foo:
        #    do_bar()
        return baz

Note that comment text is properly written and separated from the hash by a
space. Commented code is not separated from the hash by an additional space;
this helps when uncommented the code.

The Basics
::::::::::


Code Comments
-------------

Information regarding code comments is taken from PEP 008 (http://www.python.org/dev/peps/pep-0008/).
Block comment styling should be used when commenting out multiple lines of code.: ::

    Block comments generally apply to some (or all) code that follows them,
    and are indented to the same level as that code.  Each line of a block
    comment starts with a # and a single space (unless it is indented text
    inside the comment).
    Paragraphs inside a block comment are separated by a line containing a
    single #.

Inline comments are used for individual lines and should be used sparingly.: ::

    An inline comment is a comment on the same line as a statement.  Inline
    comments should be separated by at least two spaces from the statement.
    They should start with a # and a single space.
    Inline comments are unnecessary and in fact distracting if they state
    the obvious.  Don't do this:
        x = x + 1                 # Increment x
    But sometimes, this is useful: ::
        x = x + 1                 # Compensate for border

Docstrings
-----------

PEP 257 is the primary reference for docstrings. (http://www.python.org/dev/peps/pep-0257/)

There are two types of docstrings, one-line and multi-line.  Their names
should be fairly self explanatory.
One-line docstrings: ::

    def kos_root():
        """Return the pathname of the KOS root directory."""
        global _kos_root
        if _kos_root: return _kos_root
        ...

Multi-line docstrings: ::

    def complex(real=0.0, imag=0.0):
        """Form a complex number.

        Keyword arguments:
        real -- the real part (default 0.0)
        imag -- the imaginary part (default 0.0)

        """
        if imag == 0.0 and real == 0.0: return complex_zero
        ...

Sphinx
------

Sphinx_ is a tool which converts documentation in the :ref:`restructuredtext-ref`
markup language into a range of output formats including HTML, LaTeX (for
printable PDF versions), manual pages and plain text.

.. note:: This Guide is built with Sphinx_

.. _Sphinx: http://sphinx.pocoo.org

.. _restructuredtext-ref:


reStructuredText
----------------

Most Python documentation is written with reStructuredText_. The
`reStructuredText Primer <http://sphinx.pocoo.org/rest.html>`_ and the
`reStructuredText Quick Reference <http://docutils.sourceforge.net/docs/user/rst/quickref.html>`_
should help you familiarize yourself with its syntax.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html

Other Tools
:::::::::::

Epydoc
------
Epydoc generates API documentation based on docstrings. 
Epydoc is able to parse docstrings marked up with reStructuredText, Javadoc, 
plaintext or epytext. It supports various output formats, most notable HTML, 
PDF or LaTeX documents.

The development of Epydoc is discontinued. You should use Sphinx instead.

pycco / docco / shocco
----------------------

Ronn
----
