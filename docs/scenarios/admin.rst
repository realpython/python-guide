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

Chef is a systems and cloud infrastructure automation framework that makes it easy to deploy servers and applications to any physical, virtual, or cloud location, no matter the size of the infrastructure. Each organization is comprised of one (or more) workstations, a single server, and every node that will be configured and maintained by the chef-client. Cookbooks (and recipes) are used to tell the chef-client how each node in your organization should be configured. The chef-client (which is installed on every node) does the actual configuration.

The Chef Server 
---------------

The Chef server acts as a hub for configuration data. The Chef server stores cookbooks, the policies that are applied to nodes, and metadata that describes each registered node that is being managed by the chef-client. Nodes use the chef-client to ask the Chef server for configuration details, such as recipes, templates, and file distributions. The chef-client then does as much of the configuration work as possible on the nodes themselves (and not on the Chef server). This scalable approach distributes the configuration effort throughout the organization.

Server Essentials 
-----------------

The server acts as a repository for all of the data that may be needed by the chef-client while it configures a node:

* A node object exists for each node that is being managed by the chef-client
* Each node object consists of a run-list and a collection of attributes
* All data that is stored on the Chef server—including everything uploaded to the server from the chef-repo and by the chef-client—is    searchable from both recipes (using the search method in the Recipe DSL) and the workstation (using the knife search subcommand)
* The Chef server can apply global policy settings to all nodes across the organization, including for data bags, environments, and roles
* The authentication process ensures that requests can only be made to the Chef server by authorized users
* Users, once authorized can only perform certain actions
* The Chef server provides powerful search functionality

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

Flask uses a concept of blueprints for making application components and supporting common patterns within an application or across applications. Blueprints can greatly simplify how large applications work and provide a central means for Flask extensions to register operations on applications. A Blueprint object works similarly to a Flask application object, but it is not actually an application. Rather it is a blueprint of how to construct or extend an application.

Why Blueprints?
Blueprints in Flask are intended for these kind of cases:

Factor an application into a set of blueprints. This is ideal for larger applications; a project could instantiate an application object, initialize several extensions, and register a collection of blueprints.
Register a blueprint on an application at a URL prefix and/or subdomain. Parameters in the URL prefix/subdomain become common view arguments (with defaults) across all view functions in the blueprint.
Register a blueprint multiple times on an application with different URL rules.
Provide template filters, static files, templates, and other utilities through blueprints. A blueprint does not have to implement applications or view functions.
Register a blueprint on an application for any of these cases when initializing a Flask extension.
A blueprint in Flask is not a pluggable app because it is not actually an application – it’s a set of operations which can be registered on an application, even multiple times. Why not have multiple application objects? You can do that (see Application Dispatching), but your applications will have separate configs and will be managed at the WSGI layer.

Blueprints instead provide separation at the Flask level, share application config, and can change an application object as necessary with being registered. The downside is that you cannot unregister a blueprint once an application was created without having to destroy the whole application object.

The Concept of Blueprints
-------------------------
The basic concept of blueprints is that they record operations to execute when registered on an application. Flask associates view functions with blueprints when dispatching requests and generating URLs from one endpoint to another.

My First Blueprint
------------------
This is what a very basic blueprint looks like. In this case we want to implement a blueprint that does simple rendering of static templates:
from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='templates')

@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
When you bind a function with the help of the @simple_page.route decorator the blueprint will record the intention of registering the function show on the application when it’s later registered. Additionally it will prefix the endpoint of the function with the name of the blueprint which was given to the Blueprint constructor (in this case also simple_page).

Registering Blueprints
----------------------
So how do you register that blueprint? Like this:

from flask import Flask
from yourapplication.simple_page import simple_page

app = Flask(__name__)
app.register_blueprint(simple_page)
If you check the rules registered on the application, you will find these:

[<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
 <Rule '/' (HEAD, OPTIONS, GET) -> simple_page.show>]
 The first one is obviously from the application ifself for the static files. The other two are for the show function of the simple_page blueprint. As you can see, they are also prefixed with the name of the blueprint and separated by a dot (.).

Blueprints however can also be mounted at different locations:

app.register_blueprint(simple_page, url_prefix='/pages')
And sure enough, these are the generated rules:

[<Rule '/static/<filename>' (HEAD, OPTIONS, GET) -> static>,
 <Rule '/pages/<page>' (HEAD, OPTIONS, GET) -> simple_page.show>,
 <Rule '/pages/' (HEAD, OPTIONS, GET) -> simple_page.show>]
On top of that you can register blueprints multiple times though not every blueprint might respond properly to that. In fact it depends on how the blueprint is implemented if it can be mounted more than once.

more on blueprint @http://flask.pocoo.org/docs/0.10/blueprints/ 





Buildout
--------
Q: Where can I get a copy of the example module that you used in your PyAtl talk?

A: You can download the source code for the lunar module that I use as my central example in the talk right here:

http://rhodesmill.org/brandon/static/2008/lunar.tar.gz

Q: How can I start developing my Python package with buildout?

A: Move into the top-level directory of your package — the directory that has your setup.py file inside — and place two files there: bootstrap.py, which you can get in its most recent official version from this link, and a buildout.cfg that describes the development tools you want available. To gain the three tools I discuss in my presentations — a Python interpreter, access to the command-line scripts defined in your package, and a way to invoke your test suite — try out this sample buildout.cfg:

[config]
mypkgs = lunar

[buildout]
develop = .
parts = python scripts test

[python]
recipe = zc.recipe.egg
interpreter = python
eggs = {config:mypkgs}

[scripts]
recipe = zc.recipe.egg:scripts
eggs = {config:mypkgs}

[test]
recipe = zc.recipe.testrunner
eggs = {config:mypkgs}

Edit the first section of the file (whose name is arbitrary, by the way; config just made it easy for me to remember why I put it there) and change the package name lunar to the name you gave your package in the name option of its setup.py. Then, run:
$ python bootstrap.py
$ ./bin/buildout

And you should find that a ./bin/ directory appears with a python interpreter, a test runner, and any command-line scripts your module defines as console entry-points in its setup.py.

Q: Does the buildout system destroy anything?

A: Yes; buildout will consider itself the owner of these three directories at the top level of your project, so make sure that you are not using directories with these names if you do not want them overwritten:

develop-eggs/
eggs/
parts/

Q: What if I need a buildout that pulls eggs from other locations than the main Python Package Index?

A: Add some URLs to your buildout.cfg — they can point to any package index pages that the easy_install command would normally be able to digest — by adding this parameter (you can list several URLs if you want; the following URL is simply for illustration):
find-links = http://download.zope.org/distribution/

Q: How can I avoid having every buildout on my system download a separate copy of each egg it needs?

A: You should tell your buildouts to download eggs into a single cache somewhere under your home directory. The buildouts will still be safely isolated from each other, since each version of an egg has its own filename! But instead of modifying every single buildout.cfg file to accomplish this, just create a ~/.buildout/ directory inside of your home directory, and place the following inside of a file named default.cfg:
[buildout]
eggs-directory = /home/brandon/eggs


Q: How can I develop against another package's source code, before it gets packaged up as an egg?

A: Download or checkout the other package's source code into either a sub-directory of your project, or another directory under your account. Then, mention that directory's name in the develop declaration in the main section of your buildout. For example, in my presentation above I check out the SQLAlchemy trunk into the directory sqlalchemy, and then adjust my develop line to look like:
[buildout]
develop = . sqlalchemy
But sometimes putting other projects in a sub-directory of your own project can be annoying. Your version control system might then start trying to include the other project in your commits, and if you have several projects that need access to the development version of a particular library, it might be annoying to have to check it out several times. So I often check out several projects, both my own and some others, into a single top-level directory, and then have their develop lines look something like:
[buildout]
develop = . ../sqlalchemy ../gatech.identity
This way, a small cluster of applications and libraries that I will be releasing as a set of eggs can all get developed together. But it does have the disadvantage that if I actually check in my buildout.cfg while it looks this way, then other developers will have to mimic my directory structure (or re-edit the buildout.cfg) before they too can work on the project.

Q: Buildout keeps disrupting my development by downloading newer versions of dependency packages when they appear, which often have slight changes that break my application.

A: A quick fix is to add this line to the buildout section of your buildout.cfg file:

[buildout]
newest = false
But I argue that this is inadequate protection, because if you move to another machine and re-create the buildout, then you are still vulnerable to getting newer versions of dependencies than the ones you were already working with. And specifying newer = false provides no protection for co-workers on other machines, or for your customers who might later be installing your product as an egg using easy_install!

That's why the real solution is to always specify absolute version numbers in your project's setup.py. Instead of just requiring 'pyephem', require something specific like:

install_requires=['pyephem==3.7.2.3'],
If you are afraid that you or your customers might miss out on critical security updates to a package by being stuck on a single version, then leave the lowest version number unspecified by saying something like:
install_requires=['sqlalchmey >= 0.4, < 0.5'],  _

