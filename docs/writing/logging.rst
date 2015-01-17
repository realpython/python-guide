Logging
=======

The :mod:`logging` module has been a part of Python's Standard Library since
version 2.3.  It is succinctly described in :pep:`282`.  The documentation
is notoriously hard to read, except for the `basic logging tutorial`_,
and often less useful than simply reading the source code.

Logging serves two purposes:

- **Diagnostic logging** records events related to the application's
  operation. If a user calls in to report an error, for example, the logs
  can be searched for context.
- **Audit logging** records events for business analysis. A user's
  transactions can be extracted and combined with other user details for
  reports or to optimize a business goal.


... or Print Statements?
------------------------

The only time that ``print`` is a better option than logging is when
the goal is to display a help statement for a command line application.
Other reasons why logging is better than ``print``:

- The `log record`_, which is created with every logging event, contains
  readily available diagnostic information such as the file name,
  full path, function, and line number of the logging event.
- Events logged in included modules are automatically accessible via the
  root logger
  to your application's logging stream, unless you filter them out.
- Logging can be selectively silenced or disabled by using the method
  :meth:`logging.Logger.setLevel` or setting the attribute
  :attr:`logging.Logger.disabled` to ``True``.


Logging in a Library
--------------------

Notes for `configuring logging for a library`_ are in the 
`basic logging tutorial`_.  Because the *user*, not the library, should
dictate what happens when a logging event occurs, One admonition bears
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

    # Set default logging handler to avoid "No handler found" warnings.
    import logging
    try:  # Python 2.7+
        from logging import NullHandler
    except ImportError:
        class NullHandler(logging.Handler):
            def emit(self, record):
                pass

    logging.getLogger(__name__).addHandler(NullHandler())



Logging in an Application
-------------------------

The `twelve factor app's <http://12factor.net>`_, an authoritative reference
for good practice in application development, contains a section on
`logging best practice <http://12factor.net/logs>`_. It emphatically
advocates for treating log events as an event stream, and for
sending that event stream to standard output to be handled by the
application environment. Do that.


There are at least three ways to configure a logger:

- using a file (recommended)
- using a dictionary
- using code

Here is how with a file -- let us say it is named ``logging_config.txt``:

.. code-block:: none

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

    fileConfig('logging_config.txt')
    logger = logging.getLogger()
    logger.debug('often makes a very good meal of %s', 'visiting tourists')
    

..
    As of Python 2.7, you can use a dictionary with configuration details:
    
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
            loggers = {
                root : {'handlers': ['h'],
                        'level': logging.DEBUG}
                }
        )
    
        dictConfig(logging_config)
    
        logger = logging.getLogger()
        logger.debug('often makes a very good meal of %s', 'visiting tourists')
    
    
    Or instantiate the logger directly in code:
    
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
.. _configuring logging for a library: https://docs.python.org/howto/logging.html#configuring-logging-for-a-library
.. _log record: https://docs.python.org/library/logging.html#logrecord-attributes
.. _requests source: https://github.com/kennethreitz/requests
