
##################
Data Serialization
##################

.. image:: /_static/photos/33467946364_3e59bd376a_k_d.jpg


***************************
What is data serialization?
***************************

Data serialization is the process of converting structured data to a format
that allows sharing or storage of the data in a form that allows recovery of its original
structure. In some cases, the secondary intention of data
serialization is to minimize the data's size which then
reduces disk space or bandwidth requirements.

********************
Flat vs. Nested data
********************

Before beginning to serialize data, it is important to identify or decide how the
data should be structured during data serialization - flat or nested.
The differences in the two styles are shown in the below examples.

Flat style:

.. code-block:: python

        { "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }


Nested style:

.. code-block:: python

        {"A"
            { "field1": "value1", "field2": "value2", "field3": "value3" } }


For more reading on the two styles, please see the discussion on
`Python mailing list <https://mail.python.org/pipermail/python-list/2010-October/590762.html>`__,
`IETF mailing list <https://www.ietf.org/mail-archive/web/json/current/msg03739.html>`__ and
`in stackexchange <https://softwareengineering.stackexchange.com/questions/350623/flat-or-nested-json-for-hierarchal-data>`__.

****************
Serializing Text
****************

=======================
Simple file (flat data)
=======================

If the data to be serialized is located in a file and contains flat data, Python offers two methods to serialize data.

repr
----

The repr method in Python takes a single object parameter and returns a printable representation of the input:

.. code-block:: python

        # input as flat text
        a =  { "Type" : "A", "field1": "value1", "field2": "value2", "field3": "value3" }

        # the same input can also be read from a file
        a = open('/tmp/file.py', 'r')

        # returns a printable representation of the input;
        # the output can be written to a file as well
        print(repr(a))

        # write content to files using repr
        with open('/tmp/file.py') as f:f.write(repr(a))


ast.literal_eval
----------------

The literal_eval method safely parses and evaluates an expression for a Python datatype.
Supported data types are: strings, numbers, tuples, lists, dicts, booleans, and None.

.. code-block:: python

        with open('/tmp/file.py', 'r') as f: inp = ast.literal_eval(f.read())

====================
CSV file (flat data)
====================

The CSV module in Python implements classes to read and write tabular
data in CSV format.

Simple example for reading:

.. code-block:: python

        # Reading CSV content from a file
        import csv
        with open('/tmp/file.csv', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)

Simple example for writing:

.. code-block:: python

        # Writing CSV content to a file
        import csv
        with open('/temp/file.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(iterable)


The module's contents, functions, and examples can be found
`in the Python documentation <https://docs.python.org/3/library/csv.html>`__.

==================
YAML (nested data)
==================

There are many third party modules to parse and read/write YAML file
structures in Python. One such example is below.

.. code-block:: python

        # Reading YAML content from a file using the load method
        import yaml
        with open('/tmp/file.yaml', 'r', newline='') as f:
            try:
                print(yaml.load(f))
            except yaml.YAMLError as ymlexcp:
                print(ymlexcp)

Documentation on the third party module can be found
`in the PyYAML Documentation <https://pyyaml.org/wiki/PyYAMLDocumentation>`__.

=======================
JSON file (nested data)
=======================

Python's JSON module can be used to read and write JSON files.
Example code is below.

Reading:

.. code-block:: python

        # Reading JSON content from a file
        import json
        with open('/tmp/file.json', 'r') as f:
            data = json.load(f)

Writing:

.. code-block:: python

        # Writing JSON content to a file using the dump method
        import json
        with open('/tmp/file.json', 'w') as f:
            json.dump(data, f, sort_keys=True)

=================
XML (nested data)
=================

XML parsing in Python is possible using the `xml` package.

Example:

.. code-block:: python

        # reading XML content from a file
        import xml.etree.ElementTree as ET
        tree = ET.parse('country_data.xml')
        root = tree.getroot()

More documentation on using the `xml.dom` and `xml.sax` packages can be found
`in the Python XML library documentation <https://docs.python.org/3/library/xml.html>`__.


*******
Binary
*******

=======================
NumPy Array (flat data)
=======================

Python's NumPy array can be used to serialize and deserialize data to and from byte representation.

Example:

.. code-block:: python

    import NumPy as np

    # Converting NumPy array to byte format
    byte_output = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]).tobytes()

    # Converting byte format back to NumPy array
    array_format = np.frombuffer(byte_output)



====================
Pickle (nested data)
====================

The native data serialization module for Python is called `Pickle
<https://docs.python.org/2/library/pickle.html>`_.

Here's an example:

.. code-block:: python

        import pickle

        #Here's an example dict
        grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

        #Use dumps to convert the object to a serialized string
        serial_grades = pickle.dumps( grades )

        #Use loads to de-serialize an object
        received_grades = pickle.loads( serial_grades )


********
Protobuf
********

If you're looking for a serialization module that has support in multiple
languages, Google's `Protobuf
<https://developers.google.com/protocol-buffers>`_ library is an option.
