Systems Administration
======================

.. image:: https://farm5.staticflickr.com/4179/34435690580_3afec7d4cd_k_d.jpg

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

With the previous code saved in a file named :file:`fabfile.py`, we can check
memory usage with:

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

`Salt <http://saltstack.org/>`_ is an open source infrastructure management
tool.  It supports remote command execution from a central point (master host)
to multiple hosts (minions). It also supports system states which can be used
to configure multiple servers using simple template files.

Salt supports Python versions 2.6 and 2.7 and can be installed via pip:

.. code-block:: console

    $ pip install salt

After configuring a master server and any number of minion hosts, we can run
arbitrary shell commands or use pre-built modules of complex commands on our
minions.

The following command lists all available minion hosts, using the ping module.

.. code-block:: console

    $ salt '*' test.ping

The host filtering is accomplished by matching the minion id,
or using the grains system. The
`grains <http://docs.saltstack.org/en/latest/topics/targeting/grains.html>`_
system uses static host information like the operating system version or the
CPU architecture to provide a host taxonomy for the Salt modules.

The following command lists all available minions running CentOS using the
grains system:

.. code-block:: console

    $ salt -G 'os:CentOS' test.ping

Salt also provides a state system. States can be used to configure the minion
hosts.

For example, when a minion host is ordered to read the following state file,
it will install and start the Apache server:

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

`Psutil <https://github.com/giampaolo/psutil/>`_ is an interface to different
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
orchestration language and are written in YAML with Jinja2 for templating.

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

`An Ansible tutorial <https://serversforhackers.com/an-ansible-tutorial/>`_ is also a 
great and detailed introduction to getting started with Ansible.


Chef
----
`Chef <https://www.chef.io/chef/>`_  is a systems and cloud infrastructure automation 
framework that makes it easy to deploy servers and applications to any physical, 
virtual, or cloud location. In case this is your choice for configuration management, 
you will primarily use Ruby to write your infrastructure code. 

Chef clients run on every server that is part of your infrastructure and these regularly 
check with your Chef server to ensure your system is always aligned and represents the 
desired state. Since each individual server has its own distinct Chef client, each server 
configures itself and this distributed approach makes Chef a scalable automation platform.

Chef works by using custom recipes (configuration elements), implemented in cookbooks. Cookbooks, which are basically 
packages for infrastructure choices, are usually stored in your Chef server. 
Read the `Digital Ocean tutorial series 
<https://www.digitalocean.com/community/tutorials/how-to-install-a-chef-server-workstation-and-client-on-ubuntu-vps-instances>`_ 
on chef to learn how to create a simple Chef Server.

To create a simple cookbook the `knife <https://docs.chef.io/knife.html>`_ command is used:

.. code-block:: console 

    knife cookbook create cookbook_name

`Getting started with Chef <http://gettingstartedwithchef.com/first-steps-with-chef.html>`_ 
is a good starting point for Chef Beginners and many community maintained cookbooks that can 
serve as a good reference or tweaked to serve your infrastructure configuration needs can be 
found on the `Chef Supermarket <https://supermarket.chef.io/cookbooks>`_.

- `Chef Documentation <https://docs.chef.io/>`_

Puppet
------

`Puppet <http://puppetlabs.com>`_ is IT Automation and configuration management
software from Puppet Labs that allows System Administrators to define the state
of their IT Infrastructure, thereby providing an elegant way to manage their
fleet of physical and virtual machines.

Puppet is available both as an Open Source and an Enterprise variant. Modules
are small, shareable units of code written to automate or define the state of a
system.  `Puppet Forge <https://forge.puppetlabs.com/>`_ is a repository for
modules written by the community for Open Source and Enterprise Puppet.

Puppet Agents are installed on nodes whose state needs to be monitored or
changed.  A designated server known as the Puppet Master is responsible for
orchestrating the agent nodes.

Agent nodes send basic facts about the system such as to the operating system,
kernel, architecture, ip address, hostname etc. to the Puppet Master.
The Puppet Master then compiles a catalog with information provided by the
agents on how each node should be configured and sends it to the agent. The
agent enforces the change as prescribed in the catalog and sends a report back
to the Puppet Master.

Facter is an interesting tool that ships with Puppet that pulls basic facts
about the system. These facts can be referenced as a variable while writing
your Puppet modules.

.. code-block:: console

    $ facter kernel
    Linux
.. code-block:: console

    $ facter operatingsystem
    Ubuntu  

Writing Modules in Puppet is pretty straight forward. Puppet Manifests together
form Puppet Modules. Puppet manifest end with an extension of ``.pp``.
Here is an example of 'Hello World' in Puppet.

.. code-block:: puppet

    notify { 'This message is getting logged into the agent node':

        #As nothing is specified in the body the resource title
        #the notification message by default.
    }

Here is another example with system based logic. Note how the operating system
fact is being used as a variable prepended with the ``$`` sign. Similarly, this
holds true for other facts such as hostname which can be referenced by
``$hostname``

.. code-block:: puppet

    notify{ 'Mac Warning':
        message => $operatingsystem ? {
            'Darwin' => 'This seems to be a Mac.',
            default  => 'I am a PC.',
        },
    }

There are several resource types for Puppet but the package-file-service
paradigm is all you need for undertaking majority of the configuration
management. The following Puppet code makes sure that the OpenSSH-Server
package is installed in a system and the sshd service is notified to restart
everytime the sshd configuration file is changed.

.. code-block:: puppet

    package { 'openssh-server':
        ensure => installed,
    }

    file { '/etc/ssh/sshd_config':
        source   => 'puppet:///modules/sshd/sshd_config',
        owner    => 'root',
        group    => 'root',
        mode     => '640',
        notify   =>  Service['sshd'], # sshd will restart
                                      # whenever you edit this
                                      # file
        require  => Package['openssh-server'],

    }

    service { 'sshd':
        ensure    => running,
        enable    => true,
        hasstatus => true,
        hasrestart=> true,
    }

For more information, refer to the `Puppet Labs Documentation <http://docs.puppetlabs.com>`_

Blueprint
---------

.. todo:: Write about Blueprint

Buildout
--------

`Buildout <http://www.buildout.org>`_ is an open source software build tool.
Buildout is created using the Python programming language. It implements a 
principle of separation of configuration from the scripts that do the setting up.
Buildout is primarily used to download and set up dependencies in Python eggs
format of the software being developed or deployed. Recipes for build tasks in any
environment can be created, and many are already available.

Shinken
-------

`Shinken <http://www.shinken-monitoring.org/>`_ is a modern, Nagios compatible
monitoring framework written in Python. Its main goal is to give users a flexible
architecture for their monitoring system that is designed to scale to large
environments.

Shinken is backwards-compatible with the Nagios configuration standard, and
plugins.It works on any operating system, and architecture that supports Python
which includes Windows, GNU/Linux, and FreeBSD.
