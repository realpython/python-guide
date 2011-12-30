================
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
can be deployed in any :ref:`WSGI-compliant web server <wsgi-servers-ref>`. WSGI is
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

.. todo:: Explian Pyramid

Web Servers
:::::::::::

Apache
------

mod_python
~~~~~~~~~~

For a long period Apache with mod_python was one of the most reccomended
ways to deploy Python applications and thus you may see many tutorials
about it on the web or in books, however Apache no longer supports
mod_python [1]_ and thus this deployment mechanism is strongly discouraged in
favor of WSGI based ones.

mod_wsgi
~~~~~~~~

Many improvements have been made with mod_wsgi over mod_python for serving 
Python with Apache [2]_. If you must run the Apache web server, mod_wsgi is
your best option for running Python, other than proxying to a dedicated WSGI
server.

.. _nginx-ref:

Nginx
-----

`Nginx <http://nginx.org/>`_ (pronounced "engine-x") is a web server and
reverse-proxy for HTTP, SMTP and other protocols. It is known for its
high performance, relative simplicity, and compatibility with many
application servers (like WSGI servers). It also includes handy features
like load-balancing, basic authentication, streaming, and others. Designed
to serve high-load websites, Nginx is gradually becoming quite popular.

Mongrel2
--------

`Mongrel2 <http://mongrel2.org>`_ is an application, language, and network
architecture agnostic web server. It uses a high performance queue (zeromq) to
communicate with your applications, all asynchronously. There is a well defined
protocol to be used between mongrel2 and a backend handler (your app).

Brubeck
~~~~~~~

.. todo:: Explain Mongrel2 + Brubeck

wsgid
~~~~~

`Wsgid <http://wsgid.com>`_ is a generic mongrel2 handler that speaks both
mongrel2 protocol and WSGI. This makes it possible to run your python webapp
written with any WSGI compliant framework. Wsgid has built-in Django support but
has also a generic way to load your WSGI application object directly. It's
possible to add support for other frameworks through wsgid's pluggable
Apploading interface.

.. rubric:: Resources

* `Deploying your django application with mongrel2 and wsgid <http://daltonmatos.wordpress.com/2011/11/06/deploying-your-django-application-with-mongrel2-and-wsgid/>`_

.. _wsgi-servers-ref:

WSGI Servers
::::::::::::

Stand-alone WSGI servers typically use less resources than traditional web 
servers and provide top performance [3]_.

.. _gunicorn-ref:

gUnicorn
--------

`gUnicorn <http://gunicorn.org/>`_ (Green Unicorn) is a WSGI server used
to serve Python applications. It is a Python fork of the Ruby
`Unicorn <http://unicorn.bogomips.org/>`_ server. gUnicorn is designed to be
lightweight, easy to use, and uses many UNIX idioms. gUnicorn is not designed
to face the internet, in fact it was designed to run behind Nginx which buffers
slow requests, and takes care of other important considerations. A sample
setup for Nginx + gUnicorn can be found in the
`gUnicorn help <http://gunicorn.org/deploy.html>`_.

.. _uwsgi-ref:

uwsgi
-----

`uWSGI <http://projects.unbit.it/uwsgi/>`_ is a fast, self-healing and 
developer/sysadmin-friendly application container server coded in pure C.

Born as a WSGI-only server, over time it has evolved in a complete stack for 
networked/clustered web applications, implementing message/object passing, 
caching, RPC and process management.

Server Best Practices
:::::::::::::::::::::

While Apache will serve your Python application, and many references suggest it,
modern best practices suggest against it. With the improvements in mod_wsgi over
mod_python, Apache can handle many more requests than before. However, mod_wsgi
tends to use more memory than other WSGI solutions [3]_.

The majority of self hosted Python applications today are hosted with a WSGI
server such as :ref:`uWSGI <uwsgi-ref>` or :ref:`gUnicorn <gunicorn-ref>` behind a 
lightweight web server such as :ref:`nginx <nginx-ref>` or 
`lighttpd <http://www.lighttpd.net/>`_.

The WSGI servers serve the Python applications while the web server handles tasks
better suited for it such as static file serving, request routing, DDoS 
protection, and basic authentication.

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
Python version 2.6, and uses :ref:`nginx <nginx-ref>` and :ref:`uWSGI
<uwsgi-ref>`, and allows custom configuration of both
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

.. todo:: Fill in "Shared Web Hosting" stub

WebFaction
~~~~~~~~~~~


Twisted
:::::::


Node.js.

.. rubric:: References

.. [1] `The mod_python project is now officially dead <http://blog.dscpl.com.au/2010/06/modpython-project-is-now-officially.html>`_
.. [2] `mod_wsgi vs mod_python <http://www.modpython.org/pipermail/mod_python/2007-July/024080.html>`_
.. [3] `Benchmark of Python WSGI Servers <http://nichol.as/benchmark-of-python-web-servers>`_