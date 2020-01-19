.. _virtualenvironments-ref:

Package Installation and Project Isolation
==========================================

.. image:: /_static/photos/35294660055_42c02b2316_k_d.jpg

This tutorial walks you through installing and using Python packages.

It will show you how to install and use the necessary tools and make strong
recommendations on best practices. Keep in mind that Python is used for a great
many different purposes, and precisely how you want to manage your dependencies
may change based on how you decide to publish your software. The guidance
presented here is most directly applicable to the development and deployment of
network services (including web applications), but is also very well suited to
managing development and testing environments for any kind of project.

.. Note:: This guide is written for Python 3, however, these instructions
    should work fine on Python 2.7—if you are still using it, for some reason.


Make sure you've got Python & pip
---------------------------------

Before you go any further, make sure you have Python and that it's available
from your command line. You can check this by simply running:

.. code-block:: console

    $ python --version

You should get some output like ``3.6.2``. If you do not have Python, please
install the latest 3.x version from `python.org`_ or refer to the
`Installing Python`_ section of this guide.

.. Note:: If you're newcomer and you get an error like this:

    .. code-block:: python

        >>> python
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        NameError: name 'python' is not defined

    It's because this command is intended to be run in a *shell* (also called
    a *terminal* or *console*). See the Python for Beginners
    `getting started tutorial`_ for an introduction to using your operating
    system's shell and interacting with Python.

Additionally, you'll need to make sure you have `pip`_ available. You can
check this by running:

.. code-block:: console

    $ pip --version

If you installed Python from source, with an installer from `python.org`_, or
via `Homebrew`_ you should already have pip. If you're on Linux and installed
using your OS package manager, you may have to `install pip <https://pip.pypa.io/en/stable/installing/>`_ separately.

.. _getting started tutorial: https://opentechschool.github.io/python-beginners/en/getting_started.html#what-is-python-exactly
.. _python.org: https://python.org
.. _pip: https://pypi.org/project/pip/
.. _Homebrew: https://brew.sh
.. _Installing Python: https://docs.python-guide.org/starting/installation/


Pipenv
======

Installing Pipenv
-----------------

`Pipenv`_ is a dependency manager for Python projects. If you're familiar
with Node.js' `npm`_ or Ruby's `bundler`_, it is similar in spirit to those
tools. While `pip`_ can install Python packages, Pipenv is recommended as
it's a higher-level tool that simplifies dependency management for common use
cases.

Use ``pip`` to install Pipenv:

.. code-block:: console

    $ pip install --user pipenv


.. Note:: This does a `user installation`_ to prevent breaking any system-wide
    packages. If ``pipenv`` isn't available in your shell after installation,
    you'll need to add the `user base`_'s binary directory to your ``PATH``.

    On Linux and macOS you can find the user base binary directory by running
    ``python -m site --user-base`` and adding ``bin`` to the end. For example,
    this will typically print ``~/.local`` (with ``~`` expanded to the
    absolute path to your home directory) so you'll need to add
    ``~/.local/bin`` to your ``PATH``. You can set your ``PATH`` permanently by
    `modifying ~/.profile`_.

    On Windows you can find the user base binary directory by running
    ``py -m site --user-site`` and replacing ``site-packages`` with
    ``Scripts``. For example, this could return
    ``C:\Users\Username\AppData\Roaming\Python36\site-packages`` so you would
    need to set your ``PATH`` to include
    ``C:\Users\Username\AppData\Roaming\Python36\Scripts``. You can set your
    user ``PATH`` permanently in the `Control Panel`_. You may need to log
    out for the ``PATH`` changes to take effect.

.. _Pipenv: https://pipenv.kennethreitz.org/
.. _npm: https://www.npmjs.com/
.. _bundler: http://bundler.io/
.. _user base: https://docs.python.org/3/library/site.html#site.USER_BASE
.. _user installation: https://pip.pypa.io/en/stable/user_guide/#user-installs
.. _modifying ~/.profile: https://stackoverflow.com/a/14638025
.. _Control Panel: https://msdn.microsoft.com/en-us/library/windows/desktop/bb776899(v=vs.85).aspx

Installing packages for your project
------------------------------------

Pipenv manages dependencies on a per-project basis. To install packages,
change into your project's directory (or just an empty directory for this
tutorial) and run:

.. code-block:: console

    $ cd project_folder
    $ pipenv install requests

Pipenv will install the excellent `Requests`_ library and create a ``Pipfile``
for you in your project's directory. The `Pipfile`_ is used to track which
dependencies your project needs in case you need to re-install them, such as
when you share your project with others. You should get output similar to this
(although the exact paths shown will vary):

.. _Pipfile: https://github.com/pypa/pipfile

.. code-block:: text

    Creating a Pipfile for this project...
    Creating a virtualenv for this project...
    Using base prefix '/usr/local/Cellar/python3/3.6.2/Frameworks/Python.framework/Versions/3.6'
    New python executable in ~/.local/share/virtualenvs/tmp-agwWamBd/bin/python3.6
    Also creating executable in ~/.local/share/virtualenvs/tmp-agwWamBd/bin/python
    Installing setuptools, pip, wheel...done.

    Virtualenv location: ~/.local/share/virtualenvs/tmp-agwWamBd
    Installing requests...
    Collecting requests
      Using cached requests-2.18.4-py2.py3-none-any.whl
    Collecting idna<2.7,>=2.5 (from requests)
      Using cached idna-2.6-py2.py3-none-any.whl
    Collecting urllib3<1.23,>=1.21.1 (from requests)
      Using cached urllib3-1.22-py2.py3-none-any.whl
    Collecting chardet<3.1.0,>=3.0.2 (from requests)
      Using cached chardet-3.0.4-py2.py3-none-any.whl
    Collecting certifi>=2017.4.17 (from requests)
      Using cached certifi-2017.7.27.1-py2.py3-none-any.whl
    Installing collected packages: idna, urllib3, chardet, certifi, requests
    Successfully installed certifi-2017.7.27.1 chardet-3.0.4 idna-2.6 requests-2.18.4 urllib3-1.22

    Adding requests to Pipfile's [packages]...
    P.S. You have excellent taste! ✨ 🍰 ✨

.. _Requests: http://docs.python-requests.org/en/master/


Using installed packages
------------------------

Now that Requests is installed you can create a simple ``main.py`` file to
use it:

.. code-block:: python

    import requests

    response = requests.get('https://httpbin.org/ip')

    print('Your IP is {0}'.format(response.json()['origin']))

Then you can run this script using ``pipenv run``:

.. code-block:: console

    $ pipenv run python main.py

You should get output similar to this:

.. code-block:: text

    Your IP is 8.8.8.8

Using ``$ pipenv run`` ensures that your installed packages are available to
your script. It's also possible to spawn a new shell that ensures all commands
have access to your installed packages with ``$ pipenv shell``.


Next steps
----------

Congratulations, you now know how to install and use Python packages! ✨ 🍰 ✨



Project Isolation with Virtual Environments
=======================

If you choose not to use Pipenv or it does not fit your needs, you can
use the `venv <https://docs.python.org/3/library/venv.html>`_ tool directly to create
isolated Python environments. The ``venv`` module is part of Python's standard library,
and was introduced in Python 3.3. It creates a folder which contains all the necessary
executables to use the packages that a Python project would need.

It can be used standalone, in place of Pipenv.

Basic Usage
-----------

1. Create a virtual environment for a project:

.. code-block:: console

   $ cd project_folder
   $ python -m venv venv

``python -m venv venv`` will create a folder in the current directory which will
contain the Python executable files, and a copy of the ``pip`` application which you
can use to install other packages. The name of the virtual environment (in this
case, it was ``venv``) can be anything.

.. note::
    'venv' is the general convention used globally. As it is readily available in ignore files (eg: .gitignore')

This creates a copy of Python in whichever directory you ran the command in,
placing it in a folder named :file:`venv`.

You can also use the Python interpreter of your choice (like ``python3.8``).

.. code-block:: console

   $ python3.8 -m venv venv


2. To begin using the virtual environment, you can either invoke the virtual environment's executables
directly, or activate it.

To use the virtual environment's Python executable directly, run
``venv/bin/python``; to use its pip executable, ``venv/bin/pip``.

Alternatively, you can "activate"
the environment so you can just type ``python`` or ``pip`` and it will automatically use the
executables in the virtual environment (in this case, at ``venv/bin``).

.. code-block:: console

   $ source venv/bin/activate

Now, the name of the current virtual environment will appear on the left of
the prompt (e.g. ``(venv)Your-Computer:project_folder UserName$``) to let you know
that it's active. From now on, any package that you install using pip will be
placed in the ``venv`` folder, isolated from the global Python installation.

For Windows, the same command mentioned in step 1 can be used to create a virtual environment.
However, activating the environment requires a slightly different command.

Assuming that you are in your project directory:

.. code-block:: console

    C:\Users\SomeUser\project_folder> venv\Scripts\activate

Install packages using the ``pip`` command:

.. code-block:: console

    $ pip install requests

3. If you are done working in the virtual environment for the moment, you can
   deactivate it:

.. code-block:: console

    $ deactivate

This puts you back to the system's default Python interpreter with all its
installed libraries. This is not necessary if you invoked the executables directly.

To delete a virtual environment, just delete its folder. (In this case,
it would be ``rm -rf venv``.)

After a while, though, you might end up with a lot of virtual environments
littered across your system. It's possible you'll forget their names or
where they were placed, so try to follow a convention across your projects.

.. note::
    The ``venv`` module is part of Python's standard library in Python3.3+.
    Older versions of Python can use the
    3rd party package `virtualenv <https://pypi.org/project/virtualenv/>`_.

Other Notes
-----------

Running ``python -m venv`` with the option ``--no-site-packages`` will not
include the packages that are installed globally. This can be useful
for keeping the package list clean in case it needs to be accessed later.

In order to keep your environment consistent, it's a good idea to "freeze"
the current state of the environment packages. To do this, run:

.. code-block:: console

    $ pip freeze > requirements.txt

This will create a :file:`requirements.txt` file, which contains a simple
list of all the packages in the current environment, and their respective
versions. You can see the list of installed packages without the requirements
format using ``pip list``. Later it will be easier for a different developer
(or you, if you need to re-create the environment) to install the same packages
using the same versions:

.. code-block:: console

    $ pip install -r requirements.txt

This can help ensure consistency across installations, across deployments,
and across developers.

Lastly, remember to exclude the virtual environment folder from source
control by adding it to the ignore list (see :ref:`Version Control Ignores<version_control_ignores>`).

direnv
-------
When you ``cd`` into a directory containing a :file:`.env`, `direnv <https://direnv.net>`_
automagically activates the environment.

Install it on Mac OS X using ``brew``:

.. code-block:: console

   $ brew install direnv

On Linux follow the instructions at `direnv.net <https://direnv.net>`_