Databases
=========

DB-API
------

The Python Database API (DB-API) defines a standard interface for Python
database access modules. It's documented in `PEP 249 <http://www.python.org/dev/peps/pep-0249/>`_.
Nearly all Python database modules such as `sqlite3`, `psycopg` and
`mysql-python` conform to this interface.



SQLAlchemy
----------

`SQLAlchemy <http://www.sqlalchemy.org/>`_ is a commonly used database toolkit. Unlike many database libraries
it not only provides an ORM layer but also a generalized API for writing
database-agnostic code without SQL.

::

    pip install sqlalchemy

Django ORM
----------

.. todo:: Explain Django ORM