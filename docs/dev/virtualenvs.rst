Virtual Environments
====================

A Virtual Environment, put simply, is an isolated working copy of Python which allows you to work on a specific project without worry of affecting other projects.

For example, you can work on a project which requires Django 1.3 at the same time with a project which requires Django 1.0.


virtualenv
----------

`virtualenv <http://pypi.python.org/pypi/virtualenv>`_ is a tool to create isolated Python environments.

Install it via pip::

  $ pip install virtualenv

Basic Usage
~~~~~~~~~~~

1. Create a virtual environment::

   $ virtualenv ENVIRONMENT_NAME

This creates a copy of Python in whichever directory you ran the command in, placing it in a folder named ``ENVIRONMENT_NAME``.

2. To begin using the virtual environment, it needs to be activated::

   $ source ENVIRONMENT_NAME/bin/activate

You can then begin installing any new modules without affecting the system default Python or other virtual environments.

3. If you are done working in the virtual environment for the moment, you can deactivate it::

   $ deactivate

This puts you back to the system's default Python interpreter with all its installed libraries.

To delete a virtual environment, just delete its folder.

virtualenvwrapper
-----------------

`virtualenvwrapper <http://www.doughellmann.com/projects/virtualenvwrapper/>`_ provides a set of commands which makes working with virtual environments much more pleasant. It also places all your virtual environments into one place.

To install (make sure virtualenv is already installed)::

  $ pip install virtualenvwrapper
  $ export WORKON_HOME=~/Envs
  $ source /usr/local/bin/virtualenvwrapper.sh

(Full instructions `here <http://www.doughellmann.com/docs/virtualenvwrapper/#introduction>`_.)

Basic Usage
~~~~~~~~~~~

1. Create a virtual environment::

   $ mkvirtualenv ENVIRONMENT_NAME

This creates the ``ENVIRONMENT_NAME`` folder inside ``~/Envs``. 

2. Work on a virtual environment::

   $ workon ENVIRONMENT_NAME

**virtualenvwrapper** provides tab-completion on environment names. It really helps when you have a lot of environments and have trouble remembering their names. 
``workon`` also deactivates whatever environment you are currently in, so you can quickly switch between environments.

3. Deactivating is still the same::

   $ deactivate

4. To delete::

   $ rmvirtualenv ENVIRONMENT_NAME

Other nifty commands include:

``lsvirtualenv``
  List all of the environments.

``cdvirtualenv``
  Navigate into the directory of the currently activated virtual environment, so you can browse its ``site-packages``, for example. 

``cdsitepackages``
  Like the above, but directly into ``site-packages`` directory.

``lssitepackages``
  Shows contents of ``site-packages`` directory.

Full list of commands can be found `here <http://www.doughellmann.com/docs/virtualenvwrapper/command_ref.html#managing-environments>`_.
