Logging
=======

.. image:: https://farm5.staticflickr.com/4246/35254379756_c9fe23f843_k_d.jpg

The :mod:`logging` module has been a part of Python's Standard Library since
version 2.3.  It is succinctly described in :pep:`282`.  The documentation
is notoriously hard to read, except for the `basic logging tutorial`_.

Logging serves two purposes:

- **Diagnostic logging** records events related to the application's
  operation. If a user calls in to report an error, for example, the logs
  can be searched for context.
- **Audit logging** records events for business analysis. A user's
  transactions can be extracted and combined with other user details for
  reports or to optimize a business goal.


... or Print?
-------------

The only time that ``print`` is a better option than logging is when
the goal is to display a help statement for a command line application.
Other reasons why logging is better than ``print``:

- The `log record`_, which is created with every logging event, contains
  readily available diagnostic information such as the file name, full path,
  function, and line number of the logging event.
- Events logged in included modules are automatically accessible via the root
  logger to your application's logging stream, unless you filter them out.
- Logging can be selectively silenced by using the method
  :meth:`logging.Logger.setLevel` or disabled by setting the attribute
  :attr:`logging.Logger.disabled` to ``True``.


Logging in a Library
--------------------

Notes for `configuring logging for a library`_ are in the 
`logging tutorial`_.  Because the *user*, not the library, should
dictate what happens when a logging event occurs, one admonition bears
repeating:

.. note::
    It is strongly advised that you do not add any handlers other than
    NullHandler to your library’s loggers.  


Best practice when instantiating loggers in a library is to only create them
using the ``__name__`` global variable: the :mod:`logging` module creates a
hierarchy of loggers using dot notation, so using ``__name__`` ensures
no name collisions.

Here is an example of best practice from the `requests source`_ -- place
this in your ``__init__.py``

.. code-block:: python

    import logging
    logging.getLogger(__name__).addHandler(logging.NullHandler())


Logging in an Application
-------------------------

The `twelve factor app <http://12factor.net>`_, an authoritative reference
for good practice in application development, contains a section on
`logging best practice <http://12factor.net/logs>`_. It emphatically
advocates for treating log events as an event stream, and for
sending that event stream to standard output to be handled by the
application environment.


There are at least three ways to configure a logger:

- Using an INI-formatted file:
    - **Pro**: possible to update configuration while running using the
      function :func:`logging.config.listen` to listen on a socket.
    - **Con**: less control (*e.g.* custom subclassed filters or loggers)
      than possible when configuring a logger in code.
- Using a dictionary or a JSON-formatted file:
    - **Pro**: in addition to updating while running, it is possible to load
      from a file using the :mod:`json` module, in the standard library since
      Python 2.6.
    - **Con**: less control than when configuring a logger in code.
- Using code:
    - **Pro**: complete control over the configuration.
    - **Con**: modifications require a change to source code.


Example Configuration via an INI File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let us say the file is named ``logging_config.ini``.
More details for the file format are in the `logging configuration`_
section of the `logging tutorial`_.

.. code-block:: ini

    [loggers]
    keys=root
    
    [handlers]
    keys=stream_handler
    
    [formatters]
    keys=formatter
    
    [logger_root]
    level=DEBUG
    handlers=stream_handler
    
    [handler_stream_handler]
    class=StreamHandler
    level=DEBUG
    formatter=formatter
    args=(sys.stderr,)
    
    [formatter_formatter]
    format=%(asctime)s %(name)-12s %(levelname)-8s %(message)s


Then use :meth:`logging.config.fileConfig` in the code:

.. code-block:: python

    import logging
    from logging.config import fileConfig

    fileConfig('logging_config.ini')
    logger = logging.getLogger()
    logger.debug('often makes a very good meal of %s', 'visiting tourists')
    

Example Configuration via a Dictionary
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As of Python 2.7, you can use a dictionary with configuration details.
:pep:`391` contains a list of the mandatory and optional elements in
the configuration dictionary.

.. code-block:: python

    import logging
    from logging.config import dictConfig

    logging_config = dict(
        version = 1,
        formatters = {
            'f': {'format':
                  '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'}
            },
        handlers = {
            'h': {'class': 'logging.StreamHandler',
                  'formatter': 'f',
                  'level': logging.DEBUG}
            },
        root = {
            'handlers': ['h'],
            'level': logging.DEBUG,
            },
    )

    dictConfig(logging_config)

    logger = logging.getLogger()
    logger.debug('often makes a very good meal of %s', 'visiting tourists')


Example Configuration Directly in Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import logging

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)

    logger.debug('often makes a very good meal of %s', 'visiting tourists')


.. _basic logging tutorial: http://docs.python.org/howto/logging.html#logging-basic-tutorial
.. _logging configuration: https://docs.python.org/howto/logging.html#configuring-logging
.. _logging tutorial: http://docs.python.org/howto/logging.html
.. _configuring logging for a library: https://docs.python.org/howto/logging.html#configuring-logging-for-a-library
.. _log record: https://docs.python.org/library/logging.html#logrecord-attributes
.. _requests source: https://github.com/kennethreitz/requests
