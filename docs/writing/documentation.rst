Documentation
=============

Readability is a primary focus for Python developers, in both project
and code documentation. Following some simple best practices can save
both you and others a lot of time.

Project Documentation
---------------------

A :file:`README` file at the root directory should give general information
to both users and maintainers of a project. It should be raw text or
written in some very easy to read markup, such as :ref:`reStructuredText-ref`
or Markdown. It should contain a few lines explaining the purpose of the
project or library (without assuming the user knows anything about the
project), the URL of the main source for the software, and some basic credit
information. This file is the main entry point for readers of the code.

An :file:`INSTALL` file is less necessary with Python.  The installation
instructions are often reduced to one command, such as ``pip install
module`` or ``python setup.py install`` and added to the :file:`README`
file.

A :file:`LICENSE` file should *always* be present and specify the license
under which the software is made available to the public.

A :file:`TODO` file or a ``TODO`` section in :file:`README` should list the
planned development for the code.

A :file:`CHANGELOG` file or section in :file:`README` should compile a short
overview of the changes in the code base for the latest versions.

Project Publication
-------------------

Depending on the project, your documentation might include some or all
of the following components:

- An *introduction* should show a very short overview of what can be
  done with the product, using one or two extremely simplified use
  cases. This is the thirty-second pitch for your project.

- A *tutorial* should show some primary use cases in more detail. The reader
  will follow a step-by-step procedure to set-up a working prototype.

- An *API reference* is typically generated from the code (see
  :ref:`docstrings <docstring-ref>`). It will list all publicly available
  interfaces, parameters, and return values.

- *Developer documentation* is intended for potential contributors. This can
  include code convention and general design strategy of the project.

.. _sphinx-ref:

Sphinx
~~~~~~

Sphinx_ is far and away the most popular Python documentation
tool. **Use it.**  It converts :ref:`restructuredtext-ref` markup language
into a range of output formats including HTML, LaTeX (for printable
PDF versions), manual pages, and plain text.

There is also **great**, **free** hosting for your Sphinx_ docs:
`Read The Docs`_. Use it. You can configure it with commit hooks to
your source repository so that rebuilding your documentation will
happen automatically.

When run, Sphinx_ will import your code and using Python's introspection 
features it will extract all function, method and class signatures. It will
also extract the accompanying docstrings, and compile it all into well
structured and easily readable documentation for your project.  

.. note::

    Sphinx is famous for its API generation, but it also works well
    for general project documentation. This Guide is built with
    Sphinx_ and is hosted on `Read The Docs`_

.. _Sphinx: http://sphinx.pocoo.org
.. _Read The Docs: http://readthedocs.org

.. _restructuredtext-ref:

reStructuredText
~~~~~~~~~~~~~~~~

Most Python documentation is written with reStructuredText_. It's like
Markdown with all the optional extensions built in.

The `reStructuredText Primer`_ and the `reStructuredText Quick
Reference`_ should help you familiarize yourself with its syntax.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _reStructuredText Primer: http://sphinx.pocoo.org/rest.html
.. _reStructuredText Quick Reference: http://docutils.sourceforge.net/docs/user/rst/quickref.html


Code Documentation Advice
-------------------------

Comments clarify the code and they are added with purpose of making the
code easier to understand. In Python, comments begin with a hash
(number sign) (``#``).

.. _docstring-ref:

In Python, *docstrings* describe modules, classes, and functions:

.. code-block:: python

    def square_and_rooter(x):
        """Return the square root of self times self."""
        ...

In general, follow the comment section of :pep:`8#comments` (the "Python Style
Guide"). More information about docstrings can be found at :pep:`0257#specification` (The Docstring Conventions Guide).

Commenting Sections of Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Do not use triple-quote strings to comment code*. This is not a good
practice, because line-oriented command-line tools such as grep will
not be aware that the commented code is inactive. It is better to add
hashes at the proper indentation level for every commented line. Your
editor probably has the ability to do this easily, and it is worth
learning the comment/uncomment toggle.

Docstrings and Magic
~~~~~~~~~~~~~~~~~~~~

Some tools use docstrings to embed more-than-documentation behavior,
such as unit test logic. Those can be nice, but you won't ever go
wrong with vanilla "here's what this does."

Tools like Sphinx_ will parse your docstrings as reStructuredText and render it
correctly as HTML. This makes it very easy to embed snippets of example code in
a project's documentation.

Additionally, Doctest_ will read all embedded docstrings that look like input
from the Python commandline (prefixed with ">>>") and run them, checking to see
if the output of the command matches the text on the following line. This
allows developers to  embed real examples and usage of functions alongside
their source code, and as a side effect, it also ensures that their code is
tested and works.

::
    
    def my_function(a, b):
        """
        >>> my_function(2, 3)
        6
        >>> my_function('a', 3)
        'aaa'
        """
        return a * b

.. _Doctest: https://docs.python.org/3/library/doctest.html

Docstrings versus Block comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These aren't interchangeable. For a function or class, the leading
comment block is a programmer's note. The docstring describes the
*operation* of the function or class:

.. code-block:: python

    # This function slows down program execution for some reason.
    def square_and_rooter(x):
        """Returns the square root of self times self."""
	...

Unlike block comments, docstrings are built into the Python language itself.
This means you can use all of Python's powerful introspection capabilities to
access docstrings at runtime, compared with comments which are optimised out.
Docstrings are accessible from both the `__doc__` dunder attribute for almost 
every Python object, as well as with the built in `help()` function.

While block comments are usually used to explain *what* a section of code is
doing, or the specifics of an algorithm, docstrings are more intended for
explaining to other users of your code (or you in 6 months time) *how* a
particular function can be used and the general purpose of a function, class, 
or module.  

Writing Docstrings
~~~~~~~~~~~~~~~~~~

Depending on the complexity of the function, method, or class being written, a
one-line docstring may be perfectly appropriate. These are generally used for
really obvious cases, such as::

    def add(a, b):
        """Add two numbers and return the result."""
        return a + b

The docstring should describe the function in a way that is easy to understand.
For simple cases like trivial functions and classes, simply embedding the 
function's signature (i.e. `add(a, b) -> result`) in the docstring is 
unnecessary. This is because with Python's `inspect` module, it is already 
quite easy to find this information if needed, and it is also readily available
by reading the source code. 

In larger or more complex projects however, it is often a good idea to give 
more information about a function, what it does, any exceptions it may raise, 
what it returns, or relevant details about the parameters.

For more detailed documentation of code a popular style is the one used for the
Numpy project, often called `Numpy style`_ docstrings. While it can take up more
lines than the previous example, it allows the developer to include a lot 
more information about a method, function, or class. ::

    def random_number_generator(arg1, arg2):
        """
        Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        int
            Description of return value

        """
        return 42

The `sphinx.ext.napoleon`_ plugin allows Sphinx to parse this style of
docstrings, making it easy to incorporate NumPy style docstrings into your
project.

At the end of the day, it doesn't really matter what style is used for writing
docstrings, their purpose is to serve as documentation for anyone who may need
to read or make changes to your code. As long as it is correct, understandable
and gets the relevant points across then it has done the job it was designed to
do.


For further reading on docstrings, feel free to consult :pep:`257`

.. _thomas-cokelaer.info: http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
.. _sphinx.ext.napoleon: https://sphinxcontrib-napoleon.readthedocs.io/
.. _`NumPy style`: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html

Other Tools
-----------

You might see these in the wild. Use :ref:`sphinx-ref`.

Pycco_
    Pycco is a "literate-programming-style documentation generator"
    and is a port of the node.js Docco_. It makes code into a
    side-by-side HTML code and documentation.

.. _Pycco: https://pycco-docs.github.io/pycco/
.. _Docco: http://jashkenas.github.com/docco

Ronn_
    Ronn builds Unix manuals. It converts human readable textfiles to roff
    for terminal display, and also to HTML for the web.

.. _Ronn: https://github.com/rtomayko/ronn

Epydoc_
    Epydoc is discontinued. Use :ref:`sphinx-ref` instead.

.. _Epydoc: http://epydoc.sourceforge.net

MkDocs_
    MkDocs is a fast and simple static site generator that's geared towards
    building project documentation with Markdown.

.. _MkDocs: http://www.mkdocs.org/
