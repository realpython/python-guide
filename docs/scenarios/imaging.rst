==================
Image Manipulation
==================

PythonMagick is the Python binding of the ImageMagick library. 
ImageMagick® is a free software suite to create, edit, and compose bitmap images. It can read, convert and write images in a large variety of formats. Images can be cropped, colors can be changed, various effects can be applied, images can be rotated and combined, and text, lines, polygons, ellipses and Bézier curves can be added to images and stretched and rotated.

ImageMagick is free software: it is delivered with full source code and can be freely used, copied, modified and distributed. Its license is compatible with the GPL. It runs on all major operating systems.

Most of the functionality of ImageMagick can be used interactively from the command line; more often, however, the features are used from programs written in the programming languages C, Ch, C++, Java, Perl, PHP, Python, Ruby, Tcl/Tk, for which ready-made ImageMagick interfaces (PerlMagick, Magick++, PythonMagick, MagickWand for PHP, RMagick, TclMagick, and JMagick) are available. This makes it possible to modify or create images automatically and dynamically.

ImageMagick supports many image formats (over 90 major formats) including formats like GIF, JPEG, JPEG-2000, PNG, PDF, PhotoCD, TIFF, and DPX.

Here are just a few examples of what ImageMagick can do:

* Convert an image from one format to another (e.g. TIFF to JPEG)
* Resize, rotate, sharpen, color reduce, or add special effects to an image
* Create a montage of image thumbnails
* Create a transparent image suitable for use on the Web
* Turn a group of images into a GIF animation sequence
* Create a composite image by combining several separate images
* Draw shapes or text on an image
* Decorate an image with a border or frame
* Describe the format and characteristics of an image

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
