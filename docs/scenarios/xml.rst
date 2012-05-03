XML parsing
===========

untangle
--------

`untangle <http://0chris.com/untangle>`_ is a simple library which takes
an XML document and returns a Python object which mirrors the nodes and
attributes in its structure.

For example, an xml file like this:

.. code-block:: xml

    <?xml version="1.0"?>
    <root>
        <child name="child1">
    </root>

can be loaded like this:

.. code-block:: python

    import untangle
    obj = untangle.parse('path/to/file.xml')

and then you can get the child elements name like this:

.. code-block:: python

    obj.root.child['name']

untangle also supports loading XML from a string or an URL.

