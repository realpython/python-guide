================
Web Applications
================

As a powerful scripting language adapted to both fast prototyping
and bigger projects, Python is widely used in web application
development.

Context
:::::::


WSGI
----

The Web Server Gateway Interface (or "WSGI" for short) is a standard
interface between web servers and Python web application frameworks. By
standardizing behavior and communication between web servers and Python web
frameworks, WSGI makes it possible to write portable Python web code that
can be deployed in any :ref:`WSGI-compliant web server <wsgi-servers-ref>`.
WSGI is documented in :pep:`3333`.


Frameworks
::::::::::

Broadly speaking, a web framework consists of a set of libraries and a main
handler within which you can build custom code to implement a web application
(i.e. an interactive web site). Most web frameworks include patterns and
utilities to accomplish at least the following:

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

**Support** for flask can best be found in its mailing list. Just shoot an
email to flask@librelist.com and reply to the confirmation email.


Web.py
------
`Web.py <http://webpy.org/>`_ web.py is a web framework for Python that is as 
simple as it is powerful. You won't find wizards or boilerplate websites 
in Web.py and will have to build from scratch. Web.py provides no administration 
utility. Web.py is the brainchild of Aaron Swartz, who developed it while working
on Reddit.com.


Web2py
------
A full stack web framework and platform focused in the ease of use. It focuses on
rapid development, favors convention over configuration approach and follows a 
model–view–controller (MVC) architectural pattern.


Werkzeug
--------

`Werkzeug <http://werkzeug.pocoo.org/>`_ is not actually a real framework, but
rather a very powerful set of tools for building web applications. It provides
URL routing utilities, request and response objects and a basic development
server. It is mostly used where users need more flexibility for their
application than is commonly found in other web frameworks.

Support can be found on its `mailing list <http://werkzeug.pocoo.org/community/#mailinglist>`_.


Tornado
--------
`Tornado <http://www.tornadoweb.org/>`_ is a scalable, non-blocking web server
and web application framework with a relative simple usage. Tornado is known
for its high performance.  It was initially developed for
`friendfeed <http://friendfeed.com/>`_ , a real time chat and blog system.

In the Jinja2 template engine example it is used to serve the rendered pages.


Pyramid
--------

`Pyramid <http://www.pylonsproject.org/>`_ lies somewhere between a big
framework like Django and the microframeworks: It comes with a lot of libraries
and functionality and can thus not be considered lightweight. On the other
hand, it does not provide all the functionality Django does. Instead Pyramid
brings basic support for most regular tasks and provides a great deal of
extensibility. Additionally, Pyramid has a huge focus on complete
`documentation <http://docs.pylonsproject.org/en/latest/docs/pyramid.html>`__.
As a little extra it comes with the Werkzeug Debugger which allows you to debug
a running web application in the browser.

**Support** can also be found in the
`documentation <http://docs.pylonsproject.org/en/latest/index.html#support-desc>`__.


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
to face the internet -- it was designed to run behind Nginx which buffers
slow requests and takes care of other important considerations. A sample
setup for Nginx + Gunicorn can be found in the
`Gunicorn help <http://gunicorn.org/index.html#deployment>`_.

.. _uwsgi-ref:

uWSGI
-----

`uWSGI <https://uwsgi-docs.readthedocs.org>`_ is a full stack for building
hosting services.  In addition to process management, process monitoring,
and other functionality, uWSGI acts as an application server for various
programming languages and protocols - including Python and WSGI. uWSGI can
either be run as a stand-alone web router, or be run behind a full web
server (such as Nginx or Apache).  In the latter case, a web server can
configure uWSGI and an application's operation over the
`uwsgi protocol <https://uwsgi-docs.readthedocs.org/en/latest/Protocol.html>`_.
uWSGI's web server support allows for dynamically configuring
Python, passing environment variables and further tuning.  For full details,
see `uWSGI magic
variables <https://uwsgi-docs.readthedocs.org/en/latest/Vars.html>`_.


.. _server-best-practices-ref:


Server Best Practices
:::::::::::::::::::::

The majority of self-hosted Python applications today are hosted with a WSGI
server such as :ref:`Gunicorn <gunicorn-ref>`, either directly or behind a
lightweight web server such as :ref:`nginx <nginx-ref>`.

The WSGI servers serve the Python applications while the web server handles
tasks better suited for it such as static file serving, request routing, DDoS
protection, and basic authentication.

Hosting
:::::::

Platform-as-a-Service
---------------------

Platform-as-a-Service (PaaS) is a type of cloud computing infrastructure
which abstracts and manages infrastructure, routing, and scaling of web
applications. When using a PaaS, application developers can focus on writing
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

Heroku allows you to run as many Python web applications as you like, 24/7 and
free of charge. Heroku is best described as a horizontal scaling platform. They
start to charge you once you "scale" your application to run on more than one
Dyno (abstracted servers) at a time.

Heroku maintains `articles <https://devcenter.heroku.com/categories/python>`_
on using Python with Heroku as well as `step-by-step instructions
<https://devcenter.heroku.com/articles/getting-started-with-python>`_ on
how to set up your first application.


DotCloud
~~~~~~~~

`DotCloud <http://www.dotcloud.com/>`_ supports WSGI applications and
background/worker tasks natively on their platform. Web applications run
Python version 2.6, use :ref:`nginx <nginx-ref>` and :ref:`uWSGI
<uwsgi-ref>`, and allow custom configuration of both for advanced users.

DotCloud uses a custom command-line API client which can work with
applications managed in git repositories or any other version control
system.

DotCloud has a free plan with limited database size, and without extra
services (caching…).

See the `DotCloud documentation on Python
<http://docs.dotcloud.com/services/python/>`_ for more information and help
getting started.


Gondor
~~~~~~

`Gondor <https://gondor.io/>`_ is a PaaS specialized for deploying Django
and Pinax applications. Gondor recommends Django version 1.6 and supports any
WSGI application on Python version 2.7. Gondor can automatically configure your
Django site if you use :file:`local_settings.py` for site-specific configuration
information.

Gondor has a guide on deploying `Django projects <https://gondor.io/support/django/setup/>`_.


Templating
::::::::::

Most WSGI applications are responding to HTTP requests to serve content in HTML
or other markup languages. Instead of generating directly textual content from
Python, the concept of separation of concerns advises us to use templates. A
template engine manages a suite of template files, with a system of hierarchy
and inclusion to avoid unnecessary repetition, and is in charge of rendering
(generating) the actual content, filling the static content of the templates
with the dynamic content generated by the application.

As template files are
sometimes written by designers or front-end developers, it can be difficult to
handle increasing complexity.

Some general good practices apply to the part of the application passing
dynamic content to the template engine, and to the templates themselves.

- Template files should be passed only the dynamic
  content that is needed for rendering the template. Avoid
  the temptation to pass additional content "just in case":
  it is easier to add some missing variable when needed than to remove
  a likely unused variable later.

- Many template engines allow for complex statements
  or assignments in the template itself, and many
  allow some Python code to be evaluated in the
  templates. This convenience can lead to uncontrolled
  increase in complexity, and often make it harder to find bugs.

- It is often necessary to mix JavaScript templates with
  HTML templates. A sane approach to this design is to isolate
  the parts where the HTML template passes some variable content
  to the JavaScript code.



Jinja2
------
`Jinja2 <http://jinja.pocoo.org/>`_ is a template engine which is similar to
the Django template system with some extra features. It is a text-based
template language and thus can be used to generate any markup. It allows
customization of filters, tags, tests and globals, and unlike the template
system implemented in the Django Framework, also allows calling functions.
Jinja2 is released under the BSD license.

Here some important html tags in Jinja2:

.. code-block:: html

    {# This is a comment #}

    {# The next tag is a variable output: #}
    {{title}}

    {# Tag for a block, can be replaced through inheritance with other html code #}
    {% block head %}
    <h1>This is the head!</h1>
    {% endblock %}

    {# Output of an array as an iteration #}
    {% for item in list %}
    <li>{{ item }}</li>
    {% endfor %}



The next listings is an example of a web site in combination with the Tornado
web server. Tornado is not very complicated to use.

.. code-block:: python

    # import Jinja2
    from jinja2 import Environment, FileSystemLoader

    # import Tornado
    import tornado.ioloop
    import tornado.web

    # Load template file templates/site.html
    TEMPLATE_FILE = "site.html"
    templateLoader = FileSystemLoader( searchpath="templates/" )
    templateEnv = Environment( loader=templateLoader )
    template = templateEnv.get_template(TEMPLATE_FILE)

    # List for famous movie rendering
    movie_list = [[1,"The Hitchhiker's Guide to the Galaxy"],[2,"Back to future"],[3,"Matrix"]]

    # template.render() returns a string which contains the rendered html
    html_output = template.render(list=movie_list,
                            title="Here is my favorite movie list")

    # Handler for main page
    class MainHandler(tornado.web.RequestHandler):
        def get(self):
            # Returns rendered template string to the browser request
            self.write(html_output)

    # Assign handler to the server root  (127.0.0.1:PORT/)
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    PORT=8884
    if __name__ == "__main__":
        # Setup the server
        application.listen(PORT)
        tornado.ioloop.IOLoop.instance().start()

The :file:`base.html` file can be used as base for all site pages which are
for example implemented in the content block.

.. code-block:: html

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
    <html lang="en">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <link rel="stylesheet" href="style.css" />
        <title>{{title}} - My Webpage</title>
    </head>
    <body>
    <div id="content">
        {# In the next line the content from the site.html template will be added #}
        {% block content %}{% endblock %}
    </div>
    <div id="footer">
        {% block footer %}
        &copy; Copyright 2013 by <a href="http://domain.invalid/">you</a>.
        {% endblock %}
    </div>
    </body>


The next listing is our site page (:file:`site.html`) loaded in the Python
app which extends :file:`base.html`. The content block is automatically set
into the corresponding block in the :file:`base.html` page.

.. code-block:: html

    <!{% extends "base.html" %}
    {% block content %}
        <p class="important">
        <div id="content">
            <h2>{{title}}</h2>
            <p>{{ list_title }}</p>
            <ul>
                 {% for item in list %}
                 <li>{{ item[0]}} :  {{ item[1]}}</li>
                 {% endfor %}
            </ul>
        </div>
        </p>
    {% endblock %}

Chameleon
---------
`Chameleon <https://chameleon.readthedocs.org/>`_ Page Templates are an HTML/XML template
engine implementation of the `Template Attribute Language (TAL) <http://en.wikipedia.org/wiki/Template_Attribute_Language>`_,
`TAL Expression Syntax (TALES) <http://chameleon.readthedocs.org/en/latest/reference.html#expressions-tales>`_,
and `Macro Expansion TAL (Metal) <http://chameleon.readthedocs.org/en/latest/reference.html#macros-metal>`_ syntaxes.

Chameleon is available for Python 2.5 and up (including 3.x and pypy), and
is commonly used by the `Pyramid Framework <http://trypyramid.com>`_.

Page Templates add within your document structure special element attributes
and text markup. Using a set of simple language constructs, you control the
document flow, element repetition, text replacement and translation. Because
of the attribute-based syntax, unrendered page templates are valid HTML and can
be viewed in a browser and even edited in WYSIWYG editors. This can make
round-trip collaboration with designers and prototyping with static files in a
browser easier.

The basic TAL language is simple enough to grasp from an example:

.. code-block:: html

  <html>
    <body>
    <h1>Hello, <span tal:replace="context.name">World</span>!</h1>
      <table>
        <tr tal:repeat="row 'apple', 'banana', 'pineapple'">
          <td tal:repeat="col 'juice', 'muffin', 'pie'">
             <span tal:replace="row.capitalize()" /> <span tal:replace="col" />
          </td>
        </tr>
      </table>
    </body>
  </html>
  

The `<span tal:replace="expression" />` pattern for text insertion is common
enough that if you do not require strict validity in your unrendered templates,
you can replace it with a more terse and readable syntax that uses the pattern
`${expression}`, as follows:

.. code-block:: html

  <html>
    <body>
      <h1>Hello, ${world}!</h1>
      <table>
        <tr tal:repeat="row 'apple', 'banana', 'pineapple'">
          <td tal:repeat="col 'juice', 'muffin', 'pie'">
             ${row.capitalize()} ${col}
          </td>
        </tr>
      </table>
    </body>
  </html>
  

But keep in mind that the full `<span tal:replace="expression">Default Text</span>` 
syntax also allows for default content in the unrendered template.

Mako
----
`Mako <http://www.makotemplates.org/>`_ is a template language that compiles to Python
for maximum performance. Its syntax and api is borrowed from the best parts of other
templating languages like Django and Jinja2 templates. It is the default template
language included with the `Pylons and Pyramid <http://www.pylonsproject.org/>`_ web
frameworks.

An example template in Mako looks like:

.. code-block:: html

    <%inherit file="base.html"/>
    <%
        rows = [[v for v in range(0,10)] for row in range(0,10)]
    %>
    <table>
        % for row in rows:
            ${makerow(row)}
        % endfor
    </table>

    <%def name="makerow(row)">
        <tr>
        % for name in row:
            <td>${name}</td>\
        % endfor
        </tr>
    </%def>

To render a very basic template, you can do the following:

.. code-block:: python

    from mako.template import Template
    print(Template("hello ${data}!").render(data="world"))

.. rubric:: References

.. [1] `The mod_python project is now officially dead <http://blog.dscpl.com.au/2010/06/modpython-project-is-now-officially.html>`_
.. [2] `mod_wsgi vs mod_python <http://www.modpython.org/pipermail/mod_python/2007-July/024080.html>`_
.. [3] `Benchmark of Python WSGI Servers <http://nichol.as/benchmark-of-python-web-servers>`_
