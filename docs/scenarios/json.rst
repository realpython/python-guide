JSON parsing
===========

json
-----

`json <https://docs.python.org/2/library/json.html>`_ is a standard libary which can convert JSON to a Dictionay.

For example, a JSON string like this:

.. code-block:: python

    "{'first_name':'Guido','last_name':'Rossum'}"

can be loaded like this:

.. code-block:: python

    import json
    converted_dict = json.loads(json_string)

you can now use it as a normal dictionary:

.. code-block:: python

    converted_dict['first_name']

As well as converting a JSON string to a dictionary. You can convert a dictionary to JSON

For example, given:

.. code-block:: python

    d = {
        'first_name': 'Guido',
        'second_name': 'Rossum'
    }

    import json
    print json.dumps(d)
    "{'first_name':'Guido','last_name':'Rossum'}"

It is also possible to import JSON files:

.. code-block:: python

    import json
    with file('path/to/file.json') as json_file:
        processed_json = json.load(json_file)
    print processsed_json
    {u'first_name': u'Guido', u'last_name': u'Rossum'}

As well as write to them:

.. code-block:: python

    import json
    with file('path/to/file.json', 'w') as json_file:
        dict = {
            "first_name": "Guido",
            "last_name": "Rossum",
            "middle_name": "Van"
        }
        json.dump(dict, json_file)

simplejson
----------

Installation

.. code-block:: python

    pip install simplejson

`simplejson <https://simplejson.readthedocs.org/en/latest/>`_ is the externally maintained development version of the json library.

simplejson is updated much more frequently than the Python. Meaning you can get updates much quicker.

For example, a JSON string like this:

.. code-block:: python

    "{'first_name':'Guido','last_name':'Rossum'}"

can be loaded like this:

.. code-block:: python

    import simplejson
    converted_dict = simplejson.loads(json_string)

you can now use it as a normal dictionary:

.. code-block:: python

    converted_dict['first_name']

As well as converting a json string to dictionarys. You can convert dictionarys to json

For example, given:

.. code-block:: python

    import simplejson

    d = {
        'first_name': 'Guido',
        'second_name': 'Rossum'
    }
    print simplejson.dumps(d)
    "{'first_name':'Guido','last_name':'Rossum'}"


It is also possible to import JSON files:

.. code-block:: python

    import simplejson

    with file('path/to/file.json') as json_file:
        processed_json = simplejson.load(json_file)
    print processsed_json
    {u'first_name': u'Guido', u'last_name': u'Rossum'}

As well as write to them:

.. code-block:: python

    import simplejson

    with file('path/to/file.json', 'w') as json_file:
        dict = {
            "first_name": "Guido",
            "last_name": "Rossum",
            "middle_name": "Van"
        }
        simplejson.dump(dict, json_file)

