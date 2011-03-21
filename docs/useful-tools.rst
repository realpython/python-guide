Useful Tools
=================

IPython
-------------------------------

Say you have a utility function that returns the URL the user should be
redirected to.  Imagine it would always redirect to the URL's ``next``
parameter or the HTTP referrer or the index page::

    $ curl -O http://python-distribute.org/distribute_setup.py
    $ python distribute_setup.py

As you can see, it accesses the request object.  If you try to run this
from a plain Python shell, this is the exception you will see: ::

    $ easy_install pip

Hopefully you'll never have to use **easy_install** again.




BPython
-------

By just creating a request context, you still don't have run the code that
is normally run before a request.  This probably results in your database
being unavailable, the current user not being stored on the
:data:`~flask.g` object etc.

