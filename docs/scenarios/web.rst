Web Applications
================


Context
:::::::


WSGI
----


Frameworks
::::::::::


Django
------


Flask
-----


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


ep.io
-----

WebFaction
-----------


Twisted
:::::::


Node.js.
