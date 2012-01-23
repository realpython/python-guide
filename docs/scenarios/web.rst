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

**Support** for flask can best be found in its mailing list. Just shoot an email to
flask@librelist.com and reply to the confirmation email.


.. todo:: Explain Pyramid


Web Servers
:::::::::::

.. _nginx-ref:

Nginx
-----

`Nginx <http://nginx.org/>`_ (pronounced "engine-x") is a web server and
reverse-proxy for HTTP, SMTP and other protocols. It is known for its
high performance, relative simplicity, and compatibility with many
application servers (like WSGI servers). It also includes handy features
like load-balancing, basic authentication, streaming, and others. Designed
to serve high-load websites, Nginx is gradually becoming quite popular.


.. _wsgi-servers-ref:

WSGI Servers
::::::::::::

Stand-alone WSGI servers typically use less resources than traditional web
servers and provide top performance [3]_.

.. _gunicorn-ref:

Gunicorn
--------

`Gunicorn <http://gunicorn.org/>`_ (Green Unicorn) is a WSGI server used
to serve Python applications. It is a Python interpretation of the Ruby
`Unicorn <http://unicorn.bogomips.org/>`_ server. Unicorn is designed to be
lightweight, easy to use, and uses many UNIX idioms. Gunicorn is not designed
to face the internet, in fact it was designed to run behind Nginx which buffers
slow requests, and takes care of other important considerations. A sample
setup for Nginx + gUnicorn can be found in the
`Gunicorn help <http://gunicorn.org/deploy.html>`_.

.. _uwsgi-ref:


Server Best Practices
:::::::::::::::::::::

The majority of self hosted Python applications today are hosted with a WSGI
server such as :ref:`gUnicorn <gunicorn-ref>`, either directly or behind a
lightweight web server such as :ref:`nginx <nginx-ref>`.

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
`Cedar stack <http://devcenter.heroku.com/articles/cedar>`_ offers first class
support for Python 2.7 applications.

Heroku allows you to run as many Python web applications as you like, 24/7 and free
of charge. Heroku is best described as a horizontal scaling platform. They start
to charge you once you "scale" you application to run on more than one Dyno
(abstacted servers) at a time.

Heroku publishes `step-by-step instructions
<http://devcenter.heroku.com/articles/python>`_ on how to set up your first
application for use in Heroku, and maintains a list of `example applications
<http://python.herokuapp.com/>`_.


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

DotCloud has a free plan with limited database size, and without extra
services (caching…).

See the `DotCloud documentation on Python
<http://docs.dotcloud.com/services/python/>`_ for more information and help
getting started.


ep.io
~~~~~

`ep.io <https://www.ep.io/>`_ is a PaaS designed specifically for Python web
applications. It supports Python versions 2.6 and 2.7, and has Pythonic
integrations with a variety of services.

ep.io has a free plan with bandwidth and disk space limitations. Also, in the
free plan, the web process is only loaded when needed. This means that the
first request after some inactivity may take up to 15 seconds.

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


.. rubric:: References

.. [1] `The mod_python project is now officially dead <http://blog.dscpl.com.au/2010/06/modpython-project-is-now-officially.html>`_
.. [2] `mod_wsgi vs mod_python <http://www.modpython.org/pipermail/mod_python/2007-July/024080.html>`_
.. [3] `Benchmark of Python WSGI Servers <http://nichol.as/benchmark-of-python-web-servers>`_
