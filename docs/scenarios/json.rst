JSON
====

The `json <https://docs.python.org/2/library/json.html>`_ library can parse JSON from strings or files. When parsing, the library converts the JSON into a Python dictionary or list. It can also parse Python dictionaries or lists into JSON strings.

Parsing JSON
------------

The json libary is imported like this:

.. code-block:: python

    import json

Take the following string containing JSON data:

.. code-block:: python

    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

It can be parsed like this:

.. code-block:: python

    converted_dict = json.loads(json_string)

and can now be used as a normal dictionary:

.. code-block:: python

    print(converted_dict['first_name'])
    "Guido"

You can also convert a dictionary to JSON:

.. code-block:: python

    d = {
        'first_name': 'Guido',
        'second_name': 'Rossum'
    }

    print(json.dumps(d))
    "{'first_name':'Guido','last_name':'Rossum'}"


simplejson
----------

`simplejson <https://simplejson.readthedocs.org/en/latest/>`_ is the externally maintained development version of the json library.

simplejson mimics the json standard library, it is available so that developers that use an older version of python can use the latest features available in the json lib.
