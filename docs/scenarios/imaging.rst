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
the instructions for your platform in the
`Pillow installation instructions <https://pillow.readthedocs.org/en/3.0.0/installation.html>`_.

After that, it's straightforward:

.. code-block:: console

    $ pip install Pillow

Example
~~~~~~~

.. code-block:: python

        from PIL import Image, ImageFilter
        #Read image 
        im = Image.open( 'image.jpg' )
        #Display image
        im.show()

        #Applying a filter to the image
        im_sharp = im.filter( ImageFilter.SHARPEN )
        #Saving the filtered image to a new file
        im_sharp.save( 'image_sharpened.jpg', 'JPEG' ) 

        #Splitting the image into its respective bands, i.e. Red, Green, 
        #and Blue for RGB
        r,g,b = im_sharp.split()

        #Viewing EXIF data embedded in image
        exif_data = im._getexif()
        exif_data

There are more examples of the Pillow library in the
`Pillow tutorial <http://pillow.readthedocs.org/en/3.0.x/handbook/tutorial.html>`_.
