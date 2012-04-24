Structuring Your Project
========================

Structuring your project properly is extremely important.

.. todo:: Fill in "Structuring Your Project" stub

Structure is Key
----------------

Thanks to the way imports and module are handled in Python, it is
relatively easy to structure a python project. Easy, here, means
actually that you have not many constraints and that the module
importing model is easy grasp. Therefore, you are left with the
pure architectural task of drawing the different parts of your
project and their interactions.

Easy structuration of a project means it is also easy
to do it poorly. Some signs of a poorly structured projects
include:

- Multiple and messy circular dependencies: if your classes
  Table and Chair in furn.py need to import Carpenter from workers.py
  to answer to a question such as table.isdoneby(),
  and if convertly the class Carpenter need to import Table and Chair,
  for example to answer to carpenter.whatdo(), then you
  have a circular dependency, and will have to resort to
  fragile hacks such has using import statements inside
  methods or functions.

- Hidden coupling. Each and every change in Table implementation
  breaks 20 tests in unrelated test cases because it breaks Carpenter's code,
  which requires very careful surgery to adapt the change. This means
  you have too many assumptions about Table in Carpenter's code or the
  reverse.

- Heavy usage of global state or context: Instead of explicitely
  passing ``(height, width, type, wood)`` to each other, Table
  and Carpenter rely on global variables that can be modified
  and are modified on the fly by different agent. You need to
  scrutinize all access to this global variables to understand why
  a rectangular table became a sqaure, and discover that a remote
  template code is also modifying this context, messing with
  table dimensions.

- Spaghetti code: Multiple pages of nested if clauses and for loops
  with a lot of copy-pasted procedural code and no
  proper segmentation are known as spaghetti code. Python's 
  meaningful indentation (one of its most controversial feature) make
  it very hard to maintain this kind of code. So the good news is that
  you might not see too much of it.

- Ravioli code is more likely in Python: it consists of hundreds of
  similar little pieces of logic, often classes or objects, without
  proper structure. If you never can remember if you have to use
  FurnitureTable, AssetTable or Table, or even TableNew for your
  task at hand, you might be swimming in ravioli code.


Modules
-------

Python modules are one of the main abstraction layer available and probably the
most natural one. Abstraction layers allow separating code into parts holding
related data and functionalities.

For example, a layer of a project can handle interfacing with user actions,
while another would handle low-level manipulation of data. The most natural way
to separate these two layers is to regroup all interfacing functionalities
in one file, and all low-level operations in another file. In this case,
the interface file need to import the low-level file. This is done with the
`import` and `from ... import` statements.

As soon as you use `import` statements you use modules, either builtin modules
such as `os` and `sys`, or third-party modules you have installed in your
environment, or project's internal modules.

Nothing special is required for a Python file to be a module, but the import
mechanism need to be understood in order to use this concept properly and avoid
some issues.

Concretely, the `import modu` statement will look for the proper file, which is
`modu.py` in the same directory as the caller if it exists.  If it is not
found, the Python interpreter with search for `modu.py` in the "path"
recursively and raise an ImportError exception if it is not found.

Once `modu.py` is found, the Python interpreter will execute the module in an
isolated scope. Any top-level statement in `modu.py` will be executed,
including other imports if any. Function and classes definitions are stored in
the module's dictionary.

Then modules variables, functions and classes will be available to the caller
through the module's namespace, a central concept in programming that is
particularly helpful and powerful in Python.

In many languages, a `include file` directive is used by the preprocessor to
take all code found in the file and 'copy' it in the caller's code. It is
different in Python: the included code is isolated in a module namespace, which
means that you generally don't have to worry that the included code could have
unwanted effect, eg override an existing function with the same name.

It is possible to simulate the more standard behavior by using a special syntax
of the import statement: `from modu import *`. This is generally considered bad
practice, **using import * makes code harder to read and dependencies less
compartimented**.

Using `from modu import func` is a way to pinpoint the function you want to
import and put it is the global namespace. While much less harmful than `import
*` because it shows explicitely what is imported in the global namespace, it's
advantage over a simpler `import modu` is only that it will save some typing.

**Very bad**

.. code-block:: python

    [...]
    from modu import *
    [...]
    x = sqrt(4)  # Is sqrt part of modu? A builtin? Defined above?

**Better**

.. code-block:: python

    from modu import sqrt
    [...]
    x = sqrt(4)  # sqrt may be part of modu, if not redefined in between

**Best**

.. code-block:: python

    import modu
    [...]
    x = modu.sqrt(4)  # sqrt is visibly part of modu's namespace

As said in the section about style, readability is one of the main feature of
Python. Readability means to avoid useless boilerplate text and clutter,
therefore some efforts are spent trying to achieve a certain level of brevity.
But terseness and obscurity are the limits where brevity should stop: being
able to tell immediately from where comes a class or a function, as in the
`modu.func` idiom, improves greatly code readability and understandability in
most cases but the simplest single file projects.


Packages --------

Python provides a very straightforward packaging system, which is simply an
extension of the module mechanism to a directory.

Any directory with a __init__.py file is considered a Python package. The
different modules in the package are imported in a similar manner as plain
modules, will a special behavior for the __init__.py file, that is used to
gather all package-wide definitions.

A file modu.py in the directory pack/ is imported with the statement `import
pack.modu`. This statement will look for a __init__.py file in `pack`, execute
all its top-level statements. Then it will look for a file `pack/modu.py` and
execute all its top-level statements. After these operations, any variable,
function or class defined in modu.py is available in pack.modu namespace.

A commonly seen issue is to add too many code and functions in __init__.py
files. When the project complexity grows, there may be sub-packages and
sub-sub-packages in a deep directory structure, and then, import a single item
from a sub-sub-package will require to execute all __init__.py file met while
descending the tree.

Leaving a __init__.py file empty is considered normal and even a good pratice,
if the package's modules and sub-packages do not need to share any code.

Lastly, a convenient syntax is available for importing deeply nested packages:
`import very.deep.module as mod` allow to use `mod` in place of the verbose
repetition of `very.deep.module` in front of each calls to module items.

Vendorizing Dependencies
------------------------



Runners
-------


Further Reading
---------------
