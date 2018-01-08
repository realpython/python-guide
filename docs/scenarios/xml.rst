XML parsing
===========

.. image:: https://farm3.staticflickr.com/2808/33888714601_a1f7d020a2_k_d.jpg

untangle
--------

`untangle <https://github.com/stchris/untangle>`_ is a simple library which
takes an XML document and returns a Python object which mirrors the nodes and
attributes in its structure.

For example, an XML file like this:

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

xmltodict
---------

`xmltodict <http://github.com/martinblech/xmltodict>`_ is another simple
library that aims at making XML feel like working with JSON.

An XML file like this:

.. code-block:: xml

    <mydocument has="an attribute">
      <and>
        <many>elements</many>
        <many>more elements</many>
      </and>
      <plus a="complex">
        element as well
      </plus>
    </mydocument>

can be loaded into a Python dict like this:

.. code-block:: python

    import xmltodict

    with open('path/to/file.xml') as fd:
        doc = xmltodict.parse(fd.read())

and then you can access elements, attributes and values like this:

.. code-block:: python

    doc['mydocument']['@has'] # == u'an attribute'
    doc['mydocument']['and']['many'] # == [u'elements', u'more elements']
    doc['mydocument']['plus']['@a'] # == u'complex'
    doc['mydocument']['plus']['#text'] # == u'element as well'

xmltodict also lets you roundtrip back to XML with the unparse function,
has a streaming mode suitable for handling files that don't fit in memory
and supports namespaces.
