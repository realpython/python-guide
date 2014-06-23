Databases
=========

DB-API
------

The Python Database API (DB-API) defines a standard interface for Python
database access modules. It's documented in :pep:`249`.
Nearly all Python database modules such as `sqlite3`, `psycopg` and
`mysql-python` conform to this interface.

Tutorials that explain how to work with modules that conform to this interface can be found
`here <http://halfcooked.com/presentations/osdc2006/python_databases.html>`__ and
`here <http://web.archive.org/web/20120815130844/http://www.amk.ca/python/writing/DB-API.html>`__.

SQLAlchemy
----------

`SQLAlchemy <http://www.sqlalchemy.org/>`_ is a commonly used database toolkit.
Unlike many database libraries it not only provides an ORM layer but also a
generalized API for writing database-agnostic code without SQL.

.. code-block:: console

    $ pip install sqlalchemy

Django ORM
----------

The Django ORM is the interface used by `Django <http://www.djangoproject.com>`_
to provide database access.

It's based on the idea of `models <https://docs.djangoproject.com/en/1.3/#the-model-layer>`_,
an abstraction that makes it easier to manipulate data in Python.

The basics:

- Each model is a Python class that subclasses django.db.models.Model.
- Each attribute of the model represents a database field.
- Django gives you an automatically-generated database-access API; see `Making queries <https://docs.djangoproject.com/en/dev/topics/db/queries/>`__.
