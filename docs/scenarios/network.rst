Networking
==========

.. image:: https://farm3.staticflickr.com/2892/34151833832_6bdfd930af_k_d.jpg

Twisted
-------

`Twisted <http://twistedmatrix.com/trac/>`_ is an event-driven networking
engine. It can be used to build applications around many different networking
protocols, including http servers and clients, applications using SMTP, POP3,
IMAP or SSH protocols, instant messaging
and `much more <http://twistedmatrix.com/trac/wiki/Documentation>`_.

PyZMQ
-----

`PyZMQ <http://zeromq.github.com/pyzmq/>`_ is the Python binding for
`ZeroMQ <http://www.zeromq.org/>`_, which is a high-performance asynchronous
messaging library. One great advantage of ZeroMQ is that it can be used for
message queuing without a message broker. The basic patterns for this are:

- request-reply: connects a set of clients to a set of services. This is a
  remote procedure call and task distribution pattern.
- publish-subscribe: connects a set of publishers to a set of subscribers.
  This is a data distribution pattern.
- push-pull (or pipeline): connects nodes in a fan-out / fan-in pattern that
  can have multiple steps, and loops. This is a parallel task distribution
  and collection pattern.

For a quick start, read the `ZeroMQ guide <http://zguide.zeromq.org/page:all>`_.

gevent
------

`gevent <http://www.gevent.org/>`_ is a coroutine-based Python networking
library that uses greenlets to provide a high-level synchronous API on top of
the libev event loop. 
