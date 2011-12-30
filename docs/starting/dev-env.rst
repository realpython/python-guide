Your Development Environment
============================


Text Editors
::::::::::::


VIM
---


There exist a couple of plugins and settings for the VIM editor to aid python
development. If you only develop in Python, a good start is to set the default
settings for indentation and linewrapping to values compliant with PEP8::

    set textwidth=79
    set shiftwidth=4
    set tabstop=4
    set expandtab
    set softtabstop=4
    set shiftround

With these settings newlines are inserted after 79  characters and indentation
is set to 4 spaces per tab. If you also use VIM for other languages, there is a
handy plugin at indent_, which handles indentation settings for python source
files.
Additionally there is also a handy syntax plugin at syntax_ featuring some
improvements over the syntax file included in VIM 6.1.

These plugins supply you with a basic environment for developing in Python.
However in order to improve the programming flow we also want to continually
check for PEP8 compliance and check syntax. Luckily there exist PEP8_ and
Pyflakes_ to do this for you. If your VIM is compiled with `+python` you can
also utilize some very handy plugins to do these checks from within the editor.
For PEP8 checking install vim-pep8_. Now you can map the vim function
`Pep8()` to any hotkey or action you want. Similarly for pyflakes you can
install vim-pyflakes_. Now you can map `Pyflakes()` like the PEP8 function and
have it called quickly. Both plugins will display errors in a quickfix list and
provide an easy way to jump to the corresponding line. A very handy setting is
calling these functions whenever a buffer is saved. In order to do this, enter
the following lines into your vimrc::

    autocmd BufWritePost *.py call Pyflakes()
    autocmd BufWritePost *.py call Pep8()


.. _indent: http://www.vim.org/scripts/script.php?script_id=974
.. _syntax: http://www.vim.org/scripts/script.php?script_id=790
.. _Pyflakes: http://pypi.python.org/pypi/pyflakes/
.. _vim-pyflakes: https://github.com/nvie/vim-pyflakes
.. _PEP8: http://pypi.python.org/pypi/pep8/
.. _vim-pep8: https://github.com/nvie/vim-pep8

.. todo:: add supertab notes


IDEs
::::

PyCharm / IntelliJ IDEA
-----------------------

PyCharm is developed by JetBrains, also known for IntelliJ IDEA. Both share the same code base and most of PyCharm's features can be brought to IntelliJ with the free `Python Plug-In <http://plugins.intellij.net/plugin/?id=631/>`_..

Eclipse
-------

The most popular Eclipse plugin for Python development is Aptana's 
`PyDev <http://pydev.org>`_.


Komodo IDE
-----------
`Komodo IDE <http://www.activestate.com/komodo-ide>`_ is developed by ActiveState and is a commerical IDE for Windows, Mac
and Linux.

Spyder 
------

`Spyder <http://code.google.com/p/spyderlib/>`_ an IDE specifically geared toward working with scientific python libraries (namely `Scipy <http://www.scipy.org/>`_).
Includes integration with `pyflakes <http://pypi.python.org/pypi/pyflakes>`_, `pylint <http://www.logilab.org/857>`_, 
and `rope <http://rope.sourceforge.net/>`_.

Spyder is open-source (free), offers code completion, syntax highlighting, class and function browser, and object
inspection



Interpreter Tools
:::::::::::::::::


virtualenv
----------

Virtualenv is a tool to keep the dependencies required by different projects in separate places, by creating virtual Python environments for them.
It solves the "Project X depends on version 1.x but, Project Y needs 4.x" dilemma and keeps your global site-packages directory clean and manageable.

virtualenvwrapper
-----------------

Virtualenvwrapper makes virtualenv a pleasure to use by wrapping the command line API with a nicer CLI.

::

    pip install virtualenvwrapper


Put this into your `~/.bash_profile` (Linux/Mac) file:

::

    export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'

This will prevent your virtualenvs from relying on your (global) site packages directory, so that they are completely separate..

Other Tools
:::::::::::

IPython
-------

::

    $ pip install ipython



BPython
-------

::

    $ pip install bpython


