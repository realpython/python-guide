Systems Administration
======================

Fabric
------

`Fabric <http://docs.fabfile.org>`_ is a library for simplifying system
administration tasks. While Chef and Puppet tend to focus on managing servers
and system libraries, Fabric is more focused on application level tasks such
as deployment.

Install Fabric:

.. code-block:: console

    $ pip install fabric

The following code will create two tasks that we can use: ``memory_usage`` and
``deploy``. The former will output the memory usage on each machine. The
latter will ssh into each server, cd to our project directory, activate the
virtual environment, pull the newest codebase, and restart the application
server.

.. code-block:: python

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

With the previous code saved in a file named :file:`fabfile.py`, we can check memory
usage with:

.. code-block:: console

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

.. code-block:: console

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

Salt supports Python versions 2.6 and 2.7 and can be installed via pip:

.. code-block:: console

    $ pip install salt

After configuring a master server and any number of minion hosts, we can run arbitrary
shell commands or use pre-built modules of complex commands on our minions.

The following command lists all available minion hosts, using the ping module.

.. code-block:: console

    $ salt '*' test.ping

The host filtering is accomplished by matching the minion id, or using the grains system.
The `grains <http://docs.saltstack.org/en/latest/topics/targeting/grains.html>`_ system
uses static host information like the operating system version or the CPU architecture to
provide a host taxonomy for the Salt modules.

The following command lists all available minions running CentOS using the grains system:

.. code-block:: console

    $ salt -G 'os:CentOS' test.ping

Salt also provides a state system. States can be used to configure the minion hosts.

For example, when a minion host is ordered to read the following state file, it will install
and start the Apache server:

.. code-block:: yaml

    apache:
      pkg:
        - installed
      service:
        - running
        - enable: True
        - require:
          - pkg: apache

State files can be written using YAML, the Jinja2 template system or pure Python.

    `Salt Documentation <http://docs.saltstack.com>`_


Psutil
------

`Psutil <https://code.google.com/p/psutil/>`_ is an interface to different
system information (e.g. CPU, memory, disks, network, users and processes).

Here is an example to be aware of some server overload. If any of the
tests (net, CPU) fail, it will send an email.

.. code-block:: python

    # Functions to get system values:
    from psutil import cpu_percent, net_io_counters
    # Functions to take a break:
    from time import sleep
    # Package for email services:
    import smtplib
    import string
    MAX_NET_USAGE = 400000
    MAX_ATTACKS = 4
    attack = 0
    counter = 0
    while attack <= MAX_ATTACKS:
        sleep(4)
        counter = counter + 1
        # Check the cpu usage
        if cpu_percent(interval = 1) > 70:
            attack = attack + 1
        # Check the net usage
        neti1 = net_io_counters()[1]
        neto1 = net_io_counters()[0]
        sleep(1)
        neti2 = net_io_counters()[1]
        neto2 = net_io_counters()[0]
        # Calculate the bytes per second
        net = ((neti2+neto2) - (neti1+neto1))/2
        if net > MAX_NET_USAGE:
            attack = attack + 1
        if counter > 25:
            attack = 0
            counter = 0
    # Write a very important email if attack is higher than 4
    TO = "you@your_email.com"
    FROM = "webmaster@your_domain.com"
    SUBJECT = "Your domain is out of system resources!"
    text = "Go and fix your server!"
    BODY = string.join(("From: %s" %FROM,"To: %s" %TO,"Subject: %s" %SUBJECT, "",text), "\r\n")
    server = smtplib.SMTP('127.0.0.1')
    server.sendmail(FROM, [TO], BODY)
    server.quit()


A full terminal application like a widely extended top which is based on
psutil and with the ability of a client-server monitoring is
`glance <https://github.com/nicolargo/glances/>`_.

Ansible
-------

`Ansible <http://ansible.com/>`_  is an open source system automation tool.
The biggest advantage over Puppet or Chef is it does not require an agent on
the client machine. Playbooks are Ansible’s configuration, deployment, and
orchestration language and are written in in YAML with Jinja2 for templating.

Ansible supports Python versions 2.6 and 2.7 and can be installed via pip:

.. code-block:: console

    $ pip install ansible

Ansible requires an inventory file that describes the hosts to which it has
access. Below is an example of a host and playbook that will ping all the
hosts in the inventory file.

Here is an example inventory file:
:file:`hosts.yml`

.. code-block:: yaml

    [server_name]
    127.0.0.1

Here is an example playbook:
:file:`ping.yml`

.. code-block:: yaml

    ---
    - hosts: all

      tasks:
        - name: ping
          action: ping

To run the playbook:

.. code-block:: console

    $ ansible-playbook ping.yml -i hosts.yml --ask-pass

The Ansible playbook will ping all of the servers in the :file:`hosts.yml` file.
You can also select groups of servers using Ansible. For more information
about Ansible, read the `Ansible Docs <http://docs.ansible.com/>`_.


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

