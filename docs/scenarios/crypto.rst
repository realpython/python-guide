Cryptography
============

.. image:: https://farm5.staticflickr.com/4220/33907152824_bf91078cc1_k_d.jpg

Cryptography
------------

`Cryptography <https://cryptography.io/en/latest/>`_ is an actively developed
library that provides cryptographic recipes and primitives. It supports 
Python 2.6-2.7, Python 3.3+ and PyPy.


Cryptography is divided into two layers of recipes and hazardous materials
(hazmat).  The recipes layer provides simple API for proper symmetric
encryption and the hazmat layer provides low-level cryptographic primitives.



Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pip install cryptography

Example
~~~~~~~

Example code using high level symmetric encryption recipe:

.. code-block:: python

	from cryptography.fernet import Fernet
	key = Fernet.generate_key()
	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
	plain_text = cipher_suite.decrypt(cipher_text)




PyCrypto
--------

`PyCrypto <https://www.dlitz.net/software/pycrypto/>`_ is another library,
which provides secure hash functions and various encryption algorithms. It
supports Python version 2.1 through 3.3.

Installation
~~~~~~~~~~~~

.. code-block:: console

    $ pip install pycrypto

Example
~~~~~~~

.. code-block:: python

	from Crypto.Cipher import AES
	# Encryption
	encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
	cipher_text = encryption_suite.encrypt("A really secret message. Not for prying eyes.")

	# Decryption
	decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
	plain_text = decryption_suite.decrypt(cipher_text)
