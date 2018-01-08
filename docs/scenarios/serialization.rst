==================
Data Serialization
==================

.. image:: https://farm3.staticflickr.com/2927/33467946364_3e59bd376a_k_d.jpg

What is data serialization?
---------------------------

Data serialization is the concept of converting structured data into a format 
that allows it to be shared or stored in such a way that its original 
structure to be recovered. In some cases, the secondary intention of data 
serialization is to minimize the size of the serialized data which then 
minimizes disk space or bandwidth requirements.

Pickle
------

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

Protobuf
--------

If you're looking for a serialization module that has support in multiple 
languages, Google's `Protobuf 
<https://developers.google.com/protocol-buffers>`_ library is an option. 
