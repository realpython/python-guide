==================
Image Manipulation
==================

.. todo::
    Add introduction about image manipulation and its Python libraries.

Python Imaging Library
----------------------

The `Python Imaging Library <http://www.pythonware.com/products/pil/>`_, or PIL
for short, is *the* library for image manipulation in Python. Unfortunately,
its development has stagnated, with its last release in 2009.

Luckily for you, there's an actively-developed fork of PIL called
`Pillow <http://python-pillow.github.io/>`_ - it's easier to install, runs on
all operating systems, and supports Python 3.

Installation
~~~~~~~~~~~~

Before installing Pillow, you'll have to install Pillow's prerequisites. Find
the instructions for your platform
`here <https://pillow.readthedocs.org/en/3.0.0/installation.html>`_.

After that, it's straightforward:

.. code-block:: console

    $ pip install Pillow

To check that it's installed, open up Terminal and type:

.. code-block:: console

    $ python
    Python 2.7.10 (default, Aug 22 2015, 20:33:39) 
    [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.1)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from PIL import *

If it returns a **>>>**, then it's installed properly.

Basic PIL Features
~~~~~~~~~~~~~~~~~~

Most of the basic image processing functions are found in the **Image** module. 

.. code-block:: python

    from PIL import Image

The functions can then be accessed as usual.

Loading an image from your computer:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can use the **open()** method.

.. code-block:: python

    from PIL import Image
    img = Image.open("test.png")
    
The variable **img** will now contain information about your image,
and now you can use it to alter your image and work around with it.

.. figure:: http://i.imgur.com/bi69H1L.png

    test.png

If the image isn't in the current working directory, use:

.. code-block:: console

    >>> import os
    >>> os.chdir('<path to image-containing folder>')

By using other methods, you can know other details of your image too.

.. code-block:: console
    
    >>> from PIL import Image
    >>> img=Image.open("test.png")
    >>> img.size
    (824, 616)
    >>> img.filename
    'test.png'
    >>> img.format_description
    'Portable network graphics'

To save the image under a different filename, use the **save** method:

::

    >>>img.save("newtest.png")


Applying effects/filters to Image:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

PIL provides the following set of image filters by default:

    * BLUR
    * CONTOUR
    * DETAIL
    * EDGE_ENHANCE
    * EDGE_ENHANCE_MORE
    * EMBOSS
    * FIND_EDGES
    * SMOOTH
    * SMOOTH_MORE
    * SHARPEN

We use the **ImageFilter** module to use these filters. Let's use Blur!

.. code-block:: python

    from PIL import Image, ImageFilter
    img = Image.open("test.png")
    img = img.filter(ImageFilter.CONTOUR)
    img.save("newtest1.png")
    img.show()

This code saved the blurred version of **test.png** as a file **newtest1.png**.

.. figure:: http://i.imgur.com/anT8XQm.png

    newtest1.png


    












    




