JSON
====

The `json <https://docs.python.org/2/library/json.html>`_ library can read JSON strings into a Python dictionary or array. It can also serialize Python dictionaries or arrays into JSON strings.

Parsing JSON
------------

Take the following string containing JSON data:

.. code-block:: python

    json_string = '{"name": "Guido van Rossum", "invented_python": true, "age": 56, "employers": ["Google", "Dropbox"]}, "important_people": {"spouse": "Kim Knapp", "children": ["Orlijn Michiel Knapp-van Rossum"]}'

Let's look at an easier-to-read version:

.. code-block:: json

    {
        "name": "Guido van Rossum",
        "invented_python": true,
        "age": 56,
        "employers": [ "Google", "Dropbox" ],
        "important_people": {
            "spouse": "Kim Knapp",
            "children": [ "Orlijn Michiel Knapp-van Rossum" ]
        }
    }

This example displays some of the features of JSON. 

* There are six basic types in JSON: objects, arrays, numbers, strings, booleans, and null.
* The root element of this JSON representation is an object, signified by the braces ``{ ... }``. JSON objects are analogous to Python dictionaries: they have keys which correspond to values.
* JSON can be nested to represent complex structures. For example, the value for the "important_people" key is an object. This object contains a string and an array.
* JSON does not use single quotes. JSON exclusively uses double quotes. Using single quotes in the place of double quotes is invalid JSON syntax.

We can load the string containing a JSON object as a Python dictionary with ``json.loads`` (for *load string*):

.. code-block:: python

    import json
    loaded_json = json.loads(json_string)

Let's try reading some of its data:

.. code-block:: python

    loaded_json['name']  # Guido van Rossum

The JSON library can also be used to serialize a Python object into a string containing JSON data.

For example, let's serialize this very simple dictionary using ``json.dumps`` (for *dump string*):

.. code-block:: python

    my_data = {
        'name': 'Biggie Smalls',
        'birthplace': 'New York City',
        'studio_albums': 2
    }

    import json
    print(json.dumps(my_data))  # {"birthplace": "New York City", "studio_albums": 2, "name": "Biggie Smalls"}

We can also load a JSON file by using ``json.load`` instead of ``json.loads``:

.. code-block:: python

    import json
    
    with file('path/to/file.json') as f:
        loaded_json = json.load(f)
    
    print(loaded_json)  # {'first_name': 'Ada', 'last_name': 'Lovelace'}

Here's an example of writing directly to a file by using ``json.dump`` instead of ``json.dumps``:

.. code-block:: python

    import json

    my_data = {
        'name': 'Alan Turing',
        'played_by': 'Benedict Cumberbatch'
    }

    with file('path/to/file.json', 'w') as f:
        json.dump(my_data, f)

``path/to/file.json`` now contains a JSON representation of the my_data dictionary.

simplejson
----------

The JSON library was added to Python in version 2.6. If you're using an earlier version of Python, the `simplejson <https://simplejson.readthedocs.org/en/latest/>`_ library is available via PyPI.

simplejson mimics the json standard library, so you can start using simplejson instead of json by importing it under a different name:

.. code-block:: python
    
    import simplejson as json

If you import simplejson as json, the above examples will all work as if you were using the standard library.
