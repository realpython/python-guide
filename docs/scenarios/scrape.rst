HTML Scraping
=============

Web Scraping
------------

Web sites are written using HTML, which means that each web page is a
structured document. Sometimes it would be great to obtain some data from 
them and preserve the structure while we're at it, but this isn't always easy.
It's not often that web sites provide their data in comfortable formats
such as ``.csv``. 

This is where web scraping comes in. Web scraping is the practice of using
computer program to sift through a web page and gather the data that you need
in a format most useful to you.

lxml
----

`lxml <http://lxml.de/>`_ is a pretty extensive library written for parsing
XML and HTML documents, which you can easily install using ``pip``. We will 
be using its ``html`` module to get example data from this web page: `econpy.org <http://econpy.pythonanywhere.com/ex/001.html>`_ .

First we shall import the required modules:

.. code-block:: python

    from lxml import html
    from urllib2 import urlopen
    
We will use ``urllib2.urlopen`` to retrieve the web page with our data and
parse it using the ``html`` module:

.. code-block:: python

    page = urlopen('http://econpy.pythonanywhere.com/ex/001.html')
    tree = html.fromstring(page.read())

``tree`` now contains the whole HTML file in a nice tree structure which
we can go over two different ways: XPath and CSSSelect. In this example, I
will focus on the former. 

XPath is a way of locating information in structured documents such as 
HTML or XML pages. A good introduction to XPath is `here <http://www.w3schools.com/xpath/default.asp>`_ .

One can also use various tools for obtaining the XPath of elements such as
FireBug for Firefox or in Chrome you can right click an element, choose 
'Inspect element', highlight the code and the right click again and choose
'Copy XPath'.

After a quick analysis, we see that in our page the data is contained in 
two elements - one is a div with title 'buyer-name' and the other is a 
span with class 'item-price':

::

    <div title="buyer-name">Carson Busses</div>
    <span class="item-price">$29.95</span>

Knowing this we can create the correct XPath query and use the lxml
``xpath`` function like this:

.. code-block:: python

    #This will create a list of buyers:
    buyers = tree.xpath('//div[@title="buyer-name"]/text()')
    #This will create a list of prices
    prices = tree.xpath('//span[@class="item-price"]/text()')

Lets see what we got exactly:

.. code-block:: python

    print 'Buyers: ', buyers
    print 'Prices: ', prices

::

    Buyers:  ['Carson Busses', 'Earl E. Byrd', 'Patty Cakes', 
    'Derri Anne Connecticut', 'Moe Dess', 'Leda Doggslife', 'Dan Druff',
    'Al Fresco', 'Ido Hoe', 'Howie Kisses', 'Len Lease', 'Phil Meup',
    'Ira Pent', 'Ben D. Rules', 'Ave Sectomy', 'Gary Shattire',
    'Bobbi Soks', 'Sheila Takya', 'Rose Tattoo', 'Moe Tell']
    
    Prices:  ['$29.95', '$8.37', '$15.26', '$19.25', '$19.25',
    '$13.99', '$31.57', '$8.49', '$14.47', '$15.86', '$11.11',
    '$15.98', '$16.27', '$7.50', '$50.85', '$14.26', '$5.68',
    '$15.00', '$114.07', '$10.09']

Congratulations! We have successfully scraped all the data we wanted from
a web page using lxml and we have it stored in memory as two lists. Now we
can either continue our work on it, analyzing it using python or we can
export it to a file and share it with friends. 

A cool idea to think about is writing a script to iterate through the rest
of the pages of this example data set or making this application use 
threads to improve its speed.
