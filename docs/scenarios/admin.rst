Systems Administration
======================

Fabric
------

`Fabric <http://docs.fabfile.org>`_ is a library for simplifying system administration tasks. While Chef
and Puppet tend to focus on managing servers and system libraries,
fabric is more focused on application level tasks such as deployment.

Install Fabric:

.. code-block:: bash

    $ pip install fabric

The following code will create two tasks that we can use: ``memory_usage`` and
``deploy``. The former will output the memory usage on each machine. The
latter will ssh into each server, cd to our project directory, activate the
virtual environment, pull the newest codebase, and restart the application
server.

::

    from fabric.api import cd, env, prefix, run, task

    env.hosts = ['my_server1', 'my_server2']

    @task
    def memory_usage():
        run('free -m')

    @task
    def deploy():
        with cd('/var/www/project-env/project'):
            with prefix('. ../bin/activate'):
                run('git pull')
                run('touch app.wsgi')

With the previous code saved in a file named fabfile.py, we can check memory
usage with:

.. code-block:: bash

    $ fab memory_usage
    [my_server1] Executing task 'memory'
    [my_server1] run: free -m
    [my_server1] out:              total     used     free   shared  buffers   cached
    [my_server1] out: Mem:          6964     1897     5067        0      166      222
    [my_server1] out: -/+ buffers/cache:     1509     5455
    [my_server1] out: Swap:            0        0        0

    [my_server2] Executing task 'memory'
    [my_server2] run: free -m
    [my_server2] out:              total     used     free   shared  buffers   cached
    [my_server2] out: Mem:          1666      902      764        0      180      572
    [my_server2] out: -/+ buffers/cache:      148     1517
    [my_server2] out: Swap:          895        1      894

and we can deploy with:

.. code-block:: bash

    $ fab deploy

Additional features include parallel execution, interaction with remote
programs, and host grouping.

    `Fabric Documentation <http://docs.fabfile.org>`_

Salt
----

`Salt <http://saltstack.org/>`_ is an open source infrastructure management tool.
It supports remote command execution from a central point (master host) to multiple
hosts (minions). It also supports system states which can be used to configure
multiple servers using simple template files.

Salt supports python versions 2.6 and 2.7 and can be installed via pip:

.. code-block:: bash

    $ pip install salt

After configuring a master server and any number of minion hosts, we can run arbitrary
shell commands or use pre-built modules of complex commands on our minions.

The following command lists all available minion hosts, using the ping module.

.. code-block:: bash

    $ salt '*' test.ping

The host filtering is accomplished by matching the minion id, or using the grains system.
The `grains <http://docs.saltstack.org/en/latest/topics/targeting/grains.html>`_ system
uses static host information like the operating system version or the CPU architecture to
provide a host taxonomy for the salt modules.

The following command lists all available minions running CentOS using the grains system:

.. code-block:: bash

    $ salt -G 'os:CentOS' test.ping

Salt also provides a state system. States can be used to configure the minion hosts.

For example, when a minion host is ordered to read the following state file, will install
and start the Apache server:

.. code-block:: yaml

    apache:
      pkg:
        - installed
      service:
        - running

State files can be written using YAML, the Jinja2 template system or pure python.

    `Salt Documentation <http://docs.saltstack.org/en/latest/index.html>`_

Chef
----

.. todo:: Write about Chef

    `Chef Documentation
    <http://wiki.opscode.com/display/chef/Documentation>`_

Puppet
------

.. todo:: Write about Puppet

    `Puppet Labs Documentation <http://docs.puppetlabs.com>`_

Blueprint
---------

.. todo:: Write about Blueprint

Buildout
--------

.. todo:: Write about Buildout

    `Buildout Website <http://www.buildout.org>`_

