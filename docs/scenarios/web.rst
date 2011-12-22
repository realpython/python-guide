Web Applications
================


Context
:::::::


WSGI
----

The Web Server Gateway Interface (or "WSGI" for short) is a standard
interface between web servers and Python web application frameworks. By
standardizing behavior and communication between web servers and Python web
frameworks, WSGI makes it possible to write portable Python web code that
can be deployed in any `WSGI-compliant web server <#servers>`_. WSGI is
documented in `PEP-3333 <http://www.python.org/dev/peps/pep-3333/>`_.


Frameworks
::::::::::

Broadly speaking, a web framework is a set of libraries upon which you can
build custom code to implement a web application (i.e. an interactive web
site). Most web frameworks include patterns and utilities to accomplish at
least the following:

URL Routing
  Matches an incoming HTTP request to a particular piece of Python code to
  be invoked

Request and Response Objects
  Encapsulate the information received from or sent to a user's browser

Template Engine
  Allows for separating Python code implementing an application's logic from
  the HTML (or other) output that it produces

Development Web Server
  Runs an HTTP server on development machines to enable rapid development;
  often automatically reloads server-side code when files are updated


Django
------

`Django <http://www.djangoproject.com>`_ is a "batteries included" web
application framework. By providing many utilities and patterns out of the
box, Django aims to make it possible to build complex, database-backed web
applications quickly, while encouraging best practices in code written using
it.

Django has a large and active community, and many pre-built `re-usable
modules <http://djangopackages.com/>`_ that can be incorporated into a new
project as-is, or customized to fit your needs.

There are annual Django conferences `in the United States
<http://djangocon.us>`_ and `in Europe <http://djangocon.eu>`_.


Flask
-----

`Flask <http://flask.pocoo.org/>`_ is a "microframework" for Python. Rather
than aiming to provide everything you could possibly need, Flask implements
the most commonly-used core components of a web application framework, like
URL routing, request and response objects, and templates. As a user of
Flask, it is therefore up to you to choose and integrate other components
you may need, such as database access or form generation and validation. For
many popular modules, `Extensions <http://flask.pocoo.org/extensions/>`_ may
already exist to suit your needs.


Pyramid
-------


Servers
:::::::

Apache + mod_wsgi
-----------------

Apache + mod_python
-------------------


Nginx + gunicorn
----------------

Mongrel2 + Brubeck
------------------


Mongrel2 + wsgid
----------------

Mongrel2 is an application, language, and network architecture agnostic web server. It uses a high performance queue (zeromq) to communicate
with you applications, all asynchronously. There is a well defined protocol to be used between mongrel2 and a backend handler (your app).

Wsgid is a generic mongrel2 handler that speaks both mongrel2 protocol and WSGI. This makes it possible to run your python webapp written with any
WSGI compliant framework. Wsgid has built-in Django support but has also a generic way to load your WSGI application object directly. It's possible
to add support for other frameworks through wsgid's pluggable Apploading interface.

To know more about mongrel2 and wsgid go to: http://mongrel2.org and http://wsgid.com

There is also a tutorial about deploying Django using this stack: http://daltonmatos.wordpress.com/2011/11/06/deploying-your-django-application-with-mongrel2-and-wsgid/


Hosting
:::::::

Platform-as-a-Service
---------------------

Platform-as-a-Service (PaaS) is a type of cloud computing infrastructure
which abstracts and manages infrastructure, routing, and scaling of web
applications. When using PaaS, application developers can focus on writing
application code rather than needing to be concerned with deployment
details.

Most PaaS services offer a command-line interface that developers can use to
set up and interrogate configuration, and to deploy new releases of an
application to the service.

PaaS services and their partners offer add-on functionality which is well
integrated into the platform, such as database hosting, email services,
logging, scheduled and background tasks, billing and payment, etc.


Heroku
~~~~~~

`Heroku <http://www.heroku.com/>`_'s
`Cedar <http://devcenter.heroku.com/articles/cedar>`_ stack supports Python
web applications running on Python version 2.7. At this time, Cedar is in
public beta, but it is intended to become the default stack for all new
Heroku applications at some point.

Heroku uses a git-based workflow, so it is well-suited for use with
applications whose source control is managed in a git repository.

Heroku publishes `step-by-step instructions
<http://devcenter.heroku.com/articles/python>`_ on how to set up your first
application for use in Heroku, and maintains a list of `example applications
<http://python.herokuapp.com/>`_ using Heroku.


DotCloud
~~~~~~~~

`DotCloud <http://www.dotcloud.com/>`_ supports WSGI applications and
background/worker tasks natively on their platform. Web applications running
Python version 2.6, and uses `nginx <http://nginx.org/>`_ and `uWSGI
<http://projects.unbit.it/uwsgi/>`_, and allows custom configuration of both
for advanced users.

DotCloud uses a custom command-line API client which can work with
applications managed in git repositories or any other version control
system.

See the `DotCloud documentation on Python
<http://docs.dotcloud.com/services/python/>`_ for more information and help
getting started.


ep.io
~~~~~

`ep.io <https://www.ep.io/>`_ is a PaaS designed specifically for Python web
applications. It supports Python versions 2.6 and 2.7, and has Pythonic
integrations with a variety of services.

ep.io publishes `step-by-step instructions
<https://www.ep.io/docs/quickstart/>`_ on how to get started with their
platform and how to deploy Django, Flask, or generic WSGI applications.

ep.io is currently in invite-only beta.


Gondor
~~~~~~

`Gondor <https://gondor.io/>`_ is a PaaS specailized for deploying Django
and Pinax applications. Gondor supports Django versions 1.2 and 1.3 on
Python version 2.7, and can automatically configure your Django site if you
use ``local_settings.py`` for site-specific configuration information.

Gondor publishes guides to deploying `Django projects
<https://gondor.io/support/setting-up-django/>`_ and `Pinax projects
<https://gondor.io/support/setting-up-pinax/>`_ on their platform.

Shared Web Hosting
------------------

WebFaction
~~~~~~~~~~~


Twisted
:::::::


Node.js.
