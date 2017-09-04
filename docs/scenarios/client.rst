Network Applications
====================

.. image:: https://farm5.staticflickr.com/4251/34364815780_bea6614025_k_d.jpg

HTTP
::::

The Hypertext Transfer Protocol (HTTP) is an application protocol for
distributed, collaborative, hypermedia information systems. HTTP is the
foundation of data communication for the World Wide Web.

Requests
--------

Python’s standard urllib2 module provides most of the HTTP capabilities you
need, but the API is thoroughly broken. It was built for a different time —
and a different web. It requires an enormous amount of work (even method
overrides) to perform the simplest of tasks.

Requests takes all of the work out of Python HTTP — making your integration
with web services seamless. There’s no need to manually add query strings to
your URLs, or to form-encode your POST data. Keep-alive and HTTP connection
pooling are 100% automatic, powered by urllib3, which is embedded within
Requests.

- `Documentation <http://docs.python-requests.org/en/latest/index.html>`_
- `PyPi <http://pypi.python.org/pypi/requests>`_
- `GitHub <https://github.com/kennethreitz/requests>`_


Distributed Systems
::::::::::::::::::::


ZeroMQ
------

ØMQ (also spelled ZeroMQ, 0MQ or ZMQ) is a high-performance asynchronous
messaging library aimed at use in scalable distributed or concurrent
applications. It provides a message queue, but unlike message-oriented
middleware, a ØMQ system can run without a dedicated message broker. The
library is designed to have a familiar socket-style API.

RabbitMQ
--------

RabbitMQ is an open source message broker software that implements the Advanced
Message Queuing Protocol (AMQP).  The RabbitMQ server is written in the Erlang
programming language and is built on the Open Telecom Platform framework for
clustering and failover. Client libraries to interface with the broker are
available for all major programming languages.

- `Homepage <http://www.rabbitmq.com/>`_
- `GitHub Organization <https://github.com/rabbitmq?page=1>`_
