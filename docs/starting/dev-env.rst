Your Development Environment
============================

Testing your code is very important.



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

PyCharm
-------


PyDev
-----



Komodo IDE
-----------



Interpreter Tools
:::::::::::::::::


virtualenv
----------


virtualenvwrapper
-----------------



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


