
#########
Databases
#########

.. image:: /_static/photos/33907152464_a99fdcc8de_k_d.jpg


******
DB-API
******

The Python Database API (DB-API) defines a standard interface for Python
database access modules. It's documented in :pep:`249`.
Nearly all Python database modules such as `sqlite3`, `psycopg`, and
`mysql-python` conform to this interface.

Tutorials that explain how to work with modules that conform to this interface can be found
`here <http://halfcooked.com/presentations/osdc2006/python_databases.html>`__ and
`here <http://web.archive.org/web/20120815130844/http://www.amk.ca/python/writing/DB-API.html>`__.


**********
SQLAlchemy
**********

`SQLAlchemy <http://www.sqlalchemy.org/>`_ is a commonly used database toolkit.
Unlike many database libraries it not only provides an ORM layer but also a
generalized API for writing database-agnostic code without SQL.

.. code-block:: console

    $ pip install sqlalchemy


*******
Records
*******

`Records <https://github.com/kennethreitz/records>`_ is minimalist SQL library,
designed for sending raw SQL queries to various databases. Data can be used
programmatically or exported to a number of useful data formats.

.. code-block:: console

    $ pip install records

Also included is a command-line tool for exporting SQL data.


******
PugSQL
******

`PugSQL <https://pugsql.org>`_ is a simple Python interface for organizing
and using parameterized, handwritten SQL. It is an anti-ORM that is
philosophically lo-fi, but it still presents a clean interface in Python.

.. code-block:: console

    $ pip install pugsql


**********
Django ORM
**********

The Django ORM is the interface used by `Django <https://www.djangoproject.com>`_
to provide database access.

It's based on the idea of
`models <https://docs.djangoproject.com/en/dev/#the-model-layer>`_,
an abstraction that makes it easier to manipulate data in Python.

The basics:

- Each model is a Python class that subclasses django.db.models.Model.
- Each attribute of the model represents a database field.
- Django gives you an automatically-generated database-access API; see
  `Making queries <https://docs.djangoproject.com/en/dev/topics/db/queries/>`__.


******
peewee
******

`peewee <http://docs.peewee-orm.com/en/latest/>`_ is another ORM with a focus
on being lightweight with support for Python 2.6+ and 3.2+ which supports
SQLite, MySQL, and PostgreSQL by default. The
`model layer <https://peewee.readthedocs.io/en/latest/peewee/quickstart.html#model-definition>`_
is similar to that of the Django ORM and it has
`SQL-like methods <https://peewee.readthedocs.io/en/latest/peewee/quickstart.html#retrieving-data>`_
to query data. While SQLite, MySQL, and PostgreSQL are supported out-of-the-box,
there is a `collection of add-ons <https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#playhouse>`_
available.


*******
PonyORM
*******

`PonyORM <http://ponyorm.com/>`_ is an ORM that takes a different approach to
querying the database. Instead of writing an SQL-like language or boolean
expressions, Python's generator syntax is used. There's also a graphical
schema editor that can generate PonyORM entities for you. It supports Python
2.6+ and Python 3.3+ and can connect to SQLite, MySQL, PostgreSQL, and Oracle.


*********
SQLObject
*********

`SQLObject <http://www.sqlobject.org/>`_ is yet another ORM. It supports a wide
variety of databases: common database systems like MySQL, PostgreSQL, and SQLite and
more exotic systems like SAP DB, SyBase, and Microsoft SQL Server. It only supports Python 2
from Python 2.6 upwards.

.. There's no official information on this on their page; this information was gathered by looking at their source code.
