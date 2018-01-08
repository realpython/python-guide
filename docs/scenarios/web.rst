=============================
Web Applications & Frameworks
=============================

.. image:: https://farm3.staticflickr.com/2891/34309496175_b82d104282_k_d.jpg

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
application framework, and is an excellent choice for creating content-oriented
websites. By providing many utilities and patterns out of the box, Django aims
to make it possible to build complex, database-backed web applications quickly,
while encouraging best practices in code written using it.

Django has a large and active community, and many pre-built `re-usable
modules <http://djangopackages.com/>`_ that can be incorporated into a new
project as-is, or customized to fit your needs.

There are annual Django conferences `in the United States
<http://djangocon.us>`_, `Europe <http://djangocon.eu>`_, and `Australia <http://djangocon.com.au>`_.

The majority of new Python web applications today are built with Django.

Flask
-----

`Flask <http://flask.pocoo.org/>`_ is a "microframework" for Python, and is
an excellent choice for building smaller applications, APIs, and web services.

Building an app with Flask is a lot like writing standard Python modules,
except some functions have routes attached to them. It's really beautiful.

Rather than aiming to provide everything you could possibly need, Flask
implements the most commonly-used core components of a web application
framework, like URL routing, request and response objects, and templates.

If you use Flask, it is up to you to choose other components for your
application, if any. For example, database access or form generation and
validation are not built-in functions of Flask.

This is great, because many web applications don't need those features.
For those that do, there are many
`Extensions <http://flask.pocoo.org/extensions/>`_ available that may
suit your needs. Or, you can easily use any library you want yourself!

Flask is default choice for any Python web application that isn't a good
fit for Django.


Tornado
--------

`Tornado <http://www.tornadoweb.org/>`_ is an asyncronous web framework
for Python that has its own event loop. This allows it to natively support
WebSockets, for example. Well-written Tornado applications are known to
have excellent performance characteristics.

I do not recommend using Tornado unless you think you need it.

Pyramid
--------

`Pyramid <https://trypyramid.com/>`_ is a very flexible framework with a heavy
focus on modularity. It comes with a small number of libraries ("batteries")
built-in, and encourages users to extend its base functionality.

Pyramid does not have a large user base, unlike Django and Flask. It's a
capable framework, but not a very popular choice for new Python web
applications today.

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

`Gunicorn <http://gunicorn.org/>`_ (Green Unicorn) is a pure-python WSGI
server used to serve Python applications. Unlike other Python web servers,
it has a thoughtful user-interface, and is extremely easy to use and
configure.

Gunicorn has sane and reasonable defaults for configurations. However, some
other servers, like uWSGI, are tremendously more customizable, and therefore,
are much more difficult to effectively use.

Gunicorn is the recommended choice for new Python web applications today.


Waitress
--------

`Waitress <https://waitress.readthedocs.io>`_ is a pure-python WSGI server
that claims "very acceptable performance". Its documentation is not very
detailed, but it does offer some nice functionality that Gunicorn doesn't have
(e.g. HTTP request buffering).

Waitress is gaining popularity within the Python web development community.

.. _uwsgi-ref:

uWSGI
-----

`uWSGI <https://uwsgi-docs.readthedocs.io>`_ is a full stack for building
hosting services.  In addition to process management, process monitoring,
and other functionality, uWSGI acts as an application server for various
programming languages and protocols - including Python and WSGI. uWSGI can
either be run as a stand-alone web router, or be run behind a full web
server (such as Nginx or Apache).  In the latter case, a web server can
configure uWSGI and an application's operation over the
`uwsgi protocol <https://uwsgi-docs.readthedocs.io/en/latest/Protocol.html>`_.
uWSGI's web server support allows for dynamically configuring
Python, passing environment variables and further tuning.  For full details,
see `uWSGI magic
variables <https://uwsgi-docs.readthedocs.io/en/latest/Vars.html>`_.

I do not recommend using uWSGI unless you know why you need it.

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

Platform-as-a-Service (PaaS) is a type of cloud computing infrastructure
which abstracts and manages infrastructure, routing, and scaling of web
applications. When using a PaaS, application developers can focus on writing
application code rather than needing to be concerned with deployment
details.

Heroku
------

`Heroku <http://www.heroku.com/python>`_ offers first-class support for
Python 2.7–3.5 applications.

Heroku supports all types of Python web applications, servers, and frameworks.
Applications can be developed on Heroku for free. Once your application is
ready for production, you can upgrade to a Hobby or Professional application.

Heroku maintains `detailed articles <https://devcenter.heroku.com/categories/python>`_
on using Python with Heroku, as well as `step-by-step instructions
<https://devcenter.heroku.com/articles/getting-started-with-python>`_ on
how to set up your first application.

Heroku is the recommended PaaS for deploying Python web applications today.

Eldarion
--------

`Eldarion <http://eldarion.cloud/>`_ (formely known as Gondor) is a PaaS powered
by Kubernetes, CoreOS, and Docker. They support any WSGI application and have a
guide on deploying `Django projects <https://eldarion-gondor.github.io/docs/how-to/setup-deploy-first-django-project/>`_.

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
`Jinja2 <http://jinja.pocoo.org/>`_ is a very well-regarded template engine.

It uses a text-based template language and can thus be used to generate any
type markup, not just HTML. It allows customization of filters, tags, tests
and globals. It features many improvements over Django's templating system.

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

    {% extends "base.html" %}
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


Jinja2 is the recommended templating library for new Python web applications.

Chameleon
---------

`Chameleon <https://chameleon.readthedocs.io/>`_ Page Templates are an HTML/XML template
engine implementation of the `Template Attribute Language (TAL) <http://en.wikipedia.org/wiki/Template_Attribute_Language>`_,
`TAL Expression Syntax (TALES) <https://chameleon.readthedocs.io/en/latest/reference.html#expressions-tales>`_,
and `Macro Expansion TAL (Metal) <https://chameleon.readthedocs.io/en/latest/reference.html#macros-metal>`_ syntaxes.

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

Being from the Pyramid world, Chameleon is not widely used.

Mako
----

`Mako <http://www.makotemplates.org/>`_ is a template language that compiles to Python
for maximum performance. Its syntax and api is borrowed from the best parts of other
templating languages like Django and Jinja2 templates. It is the default template
language included with the `Pylons and Pyramid <http://www.pylonsproject.org/>`_ web
frameworks.

An example template in Mako looks like:

.. code-block:: mako

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

Mako is well respected within the Python web community.

.. rubric:: References

.. [1] `The mod_python project is now officially dead <http://blog.dscpl.com.au/2010/06/modpython-project-is-now-officially.html>`_
.. [2] `mod_wsgi vs mod_python <http://www.modpython.org/pipermail/mod_python/2007-July/024080.html>`_
.. [3] `Benchmark of Python WSGI Servers <http://nichol.as/benchmark-of-python-web-servers>`_
