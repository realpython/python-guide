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


Pylons
------


Web2Py
------


Servers
:::::::

Apache + mod_wsgi
-----------------

Apache + mod_python
-------------------


Nginx + gunicorn
----------------


Hosting
:::::::

Heroku
------

DotCloud
--------

gondor.io
---------

ep.io
-----

WebFaction
-----------


Twisted
:::::::


Node.js.
