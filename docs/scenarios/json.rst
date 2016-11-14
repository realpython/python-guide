JSON
====

The `json <https://docs.python.org/2/library/json.html>`_ library can parse
JSON from strings or files. The library parses JSON into a Python dictionary
or list. It can also convert Python dictionaries or lists into JSON strings.

Parsing JSON
------------

Take the following string containing JSON data:

.. code-block:: python

    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

It can be parsed like this:

.. code-block:: python

    import json
    parsed_json = json.loads(json_string)

and can now be used as a normal dictionary:

.. code-block:: python

    print(parsed_json['first_name'])
    "Guido"

You can also convert the following to JSON:

.. code-block:: python

    d = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
        'titles': ['BDFL', 'Developer'],
    }

    print(json.dumps(d))
    '{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "Developer"]}'


simplejson
----------

The JSON library was added to Python in version 2.6.
If you're using an earlier version of Python, the
`simplejson <https://simplejson.readthedocs.io/en/latest/>`_ library is
available via PyPI.

simplejson mimics the json standard library. It is available so that developers
that use older versions of Python can use the latest features available in the
json lib.

You can start using simplejson when the json library is not available by
importing simplejson under a different name:

.. code-block:: python
    
    import simplejson as json

After importing simplejson as json, the above examples will all work as if you
were using the standard json library.
