.. _pip-virtualenv:

Further Configuration of Pip and Virtualenv
===========================================

Requiring an active virtual environment for ``pip``
---------------------------------------------------

By now it should be clear that using virtual envirtonments is a great way to keep
your development environment clean and keeping different projects' requirements
separate.

When you start working on many different projects, it can be hard to remember to
activate the related virtual environment when you come back to a specific project.
As a result of this, it is very easy to install packages globally while thinking
that you are actually installing the package for the virtual environment of the
project. Over time this can result in a messy global package list.

In order to make sure that you install packages to your active virtual environment
when you use ``pip install``, consider adding the following two lines to your
``~/.bashrc`` file:

.. code-block:: console

    export PIP_REQUIRE_VIRTUALENV=true

After saving this change and sourcing the ``~/.bashrc`` file with ``source ~/.bashrc``,
pip will no longer let you install packages if you are not in a virtual environment.
If you try to use ``pip install`` outside of a virtual environment pip will gently
remind you that an activated virtual environment is needed to install packages.

.. code-block:: console

    $ pip install requests
    Could not find an activated virtualenv (required).

You can also do this configuration by editing your ``pip.conf`` or ``pip.ini``
file. ``pip.conf`` is used by Unix and Mac OS X operating systems and it can be
found at:

.. code-block:: console

    $HOME/.pip/pip.conf

Similarly, the ``pip.ini`` file is used by Windows operating systems and it can
be found at:

.. code-block:: console

    %HOME%\pip\pip.ini

If you don't have a ``pip.conf`` or ``pip.ini`` file at these locations, you can
create a new file with the correct name for your operating system.

If you already have a configuration file, just add the following line under the
``[global]`` settings to require an active virtual environment:

.. code-block:: console

    require-virtualenv = true

If you did not have a configuration file, you will need to create a new one and
add the following lines to this new file:

.. code-block:: console

    [global]
    require-virtualenv = true


You will of course need to install some packages globally (usually ones that you
use across different projects consistenly) and this can be accomplished by adding
the following to your ``~/.bashrc`` file:

.. code-block:: console

    gpip() {
        PIP_REQUIRE_VIRTUALENV="" pip "$@"
    }

After saving the changes and sourcing your ``~/.bashrc`` file you can now install
packages globally by running ``gpip install``. You can change the name of the
function to anything you like, just keep in mind that you will have to use that
name when trying to install packages globally with pip.
