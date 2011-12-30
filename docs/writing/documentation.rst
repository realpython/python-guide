Documenting Your Code
=====================

Documenting your code is extremely important. It is debatebly even
more important than testing.


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

Doc Strings
-----------
PEP 257 is the primary reference for docstrings. (http://www.python.org/dev/peps/pep-0257/)
|There are two types of docstrings, one-line and multi-line.  Their names should be fairly self explanatory.
|One-line docstrings: ::

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
Sphinx (http://sphinx.pocoo.org) is a tool  which converts documentation in the reStructured text markup language into a range of output formats including HTML, LaTeX (for printable PDF versions), manual pages and plain text.



Other Tools
:::::::::::

that old thing
--------------

pocco / docco / shocco
----------------------

Ronn
----