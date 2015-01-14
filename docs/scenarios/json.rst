JSON
===========

The `json <https://docs.python.org/2/library/json.html>`_ library can read JSON strings into a Python dictionary or array. It can also serialize Python dictionaries or arrays into JSON strings.

* There are six basic types in JSON: objects, arrays, numbers, strings, booleans, and null.
* The root element of JSON representation is an object, signified by ``{ ... }``. JSON objects are analogous to Python dictionaries: they have keys which correspond to values.
* JSON does not use single quotes. JSON exclusively uses double quotes. Using single quotes in the place of double quotes is invalid JSON syntax.

Parsing JSON
------------
The `json <https://docs.python.org/2/library/json.html>`_ libary is imported like this:

.. code-block:: python

    import json

Take the following string containing JSON data:

.. code-block:: python

    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

It can be manpulated like this:

.. code-block:: python

    converted_dict = json.loads(json_string)

and can now be used as a normal dictionary:

.. code-block:: python

    converted_dict['first_name']

As well as converting a JSON string to a dictionary. You can convert a dictionary to JSON:

.. code-block:: python

    d = {
        'first_name': 'Guido',
        'second_name': 'Rossum'
    }

    print(json.dumps(d))
    "{'first_name':'Guido','last_name':'Rossum'}"

We can also load a JSON file by using ``json.load`` instead of ``json.loads``:

.. code-block:: python

    with file('path/to/file.json') as json_file:
        processed_json = json.load(json_file)

    print(processsed_json)
    {u'first_name': u'Guido', u'last_name': u'Rossum'}


Here's an example of writing directly to a file by using ``json.dump`` instead of ``json.dumps``:

.. code-block:: python

    with file('path/to/file.json', 'w') as json_file:
        dict = {
            "first_name": "Guido",
            "last_name": "Rossum",
            "middle_name": "Van"
        }
        json.dump(dict, json_file)

simplejson
----------
`simplejson <https://simplejson.readthedocs.org/en/latest/>`_ is the externally maintained development version of the json library.

simplejson mimics the json standard library, so you can start using simplejson instead of json by importing it under a different name

Installation

.. code-block:: python

    pip install simplejson

Usage

.. code-block:: python

    import simplejson as json

simplejson is available so that developers that use an older version of python can use the latest features available in the json lib.


