Systems Administration
======================

Fabric
------

Fabric is a library for simplifying system administration tasks. While Chef
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

pbs
---
`pbs <https://github.com/amoffat/pbs>`_ is a tool that take 
python a bit closer to bash. In a pythonic more "Human" way
(not like the standard library subprocess].

you can utilize it like that:

.. code-block:: python
    
    from pbs import ifconfig
    print ifconfig("eth0")

or for the lazy ones:

.. code-block:: python
    
    from pbs import *
    print ifconfig("eth0")
    print du()

RPyC
----
`RPyC <http://rpyc.sourceforge.net/>`_ is a module that can give you control on a remote interpeter, in a convientent way.
when you need two python interpeters talk with each other, make sure you try this one.
    
starting the server:
.. code-block:: bash
    
    $ ./rpyc_classic.py -m threaded
    
connect from client:
.. code-block:: python

    conn = rpyc.classic.connect("hostname")
    
    # using modules for anthoer interpeter/host
    proc = conn.modules.subprocess.Popen("ls", stdout = -1, stderr = -1)
    stdout, stderr = proc.communicate()
    print stdout.split()

    remote_list = conn.builtin.range(7)

    conn.execute("print 'foo'")