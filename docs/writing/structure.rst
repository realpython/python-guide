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





Vendorizing Dependencies
------------------------



Runners
-------


Further Reading
---------------
