Systems Administration
======================

Fabric
------

Fabric is a library for simplifying system administration tasks. While Chef
and Puppet tend to focus on managing servers and system libraries,
fabric is more focused on application level tasks such as deployment.

Install Fabric:

::

    $ pip install fabric

The following code will ssh into both of our servers, cd to our project
directory, activate the virtual environment, pull the newest codebase,
and restart the application server.

::

    from fabric.api import cd, env, prefix, run, task

    env.hosts = ['my_server1', 'my_server2']

    @task
    def deploy():
        with cd('/var/www/project-env/project'):
            with prefix('. ../bin/activate'):
                run('git pull')
                run('touch app.wsgi')

With the previous code saved in a file named fabfile.py, we merely need to run
the following command to deploy our application to both of our servers.

::

    $ fab deploy

Additional features include parallel execution, interaction with remote
programs, and host grouping.

Chef
----

.. todo:: Write about Chef

Puppet
------

.. todo:: Write about Puppet

Blueprint
---------

.. todo:: Write about Blueprint

Buildout
--------

.. todo:: Write about Buildout