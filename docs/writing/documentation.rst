

#############
Documentation
#############

.. image:: /_static/photos/35620636012_f66aa88f93_k_d.jpg

La legibilidad es el enfoque primario para los desarrolladores en Python,
tanto en proyectos como en la documentación del código. Seguir algunas 
buenas prácticas puede ahorrarte y a los demás mucho tiempo. 


*********************
Documentación de proyectos
*********************

Un archivo :file:`README` en el directorio raiz debería dar información general
tanto a los usuarios como a los mantenedores de un proyecto. Debe ser un texto 
plano o escrito en un lenguaje de marcas ligero como :ref:`reStructuredText-ref`
o Markdown. Debe contener pocas líneas explicando el proposito del proyecto o 
librería (sin asumir que el usuario sabe algo acerca del proyecto), la dirección URL 
de la fuente principal del software, y alguna información básica sobre los créditos. 
Este archivo es el punto de entrada principal para quienes leen el código. 

Un archivo :file:`INSTALL` es menos necesario con Python. Las instrucciones
de instalación se reducen normalmente a un solo comando como ``pip install
module`` o ``python setup.py install``, y añadidos al archivo :file:`README`

Un archivo :file:`LICENSE` siempre debe estar presente y especificar la licencia 
bajo la cual el software se hace disponible al público.

Un archivo :file:`TODO` file o sección ``TODO`` en un archivo :file:`README` debe 
contener la lista del desarrollo planeado para el código. 

Un archivo :file:`CHANGELOG` o una sección :file:`README` debe compilar una visión 
general de los cambios en el código base para las últimas versiones. 


*******************
Publicación del proyecto
*******************

Dependiendo del proyecto, tu documentación puede incluir alguno o todos 
los siguientes componentes: 
- Una *introducción* debe dar un resumen de lo que se puede hacer con el producto,
  usando uno o dos ejemplos sobresimplificados. Este es el discurso de 30 segundos de tu proyecto.
  
- Un *tutorial* debe mostrar algunos casos primarios de uso con mayor detalle. 
  El lector seguirá paso a paso el procedimiento para establecer un prototipo funcional. 

- Una *referencia del API* es generada tipicamente desde el código (consulta
  :ref:`docstrings <docstring-ref>`). Esta enlista todas las interfaces disponibles publicamente,
  parametros y valores de retorno. 

- La *Documentación para desarrolladores* está destinada para contribuidores potenciales. 
  Esta puede incluir convenciones de código y una estrategia general del proyecto.

.. _sphinx-ref:

Sphinx
~~~~~~

Sphinx_ es por mucho la herramienta de documentación mas popular de Python. 
**Usala.**  Convierte lenguaje de marcas ligero :ref:`restructuredtext-ref` 
en diversos formatos de salida, incluidos HTML, LaTex (para versiones 
imprimibles en PDF), páginas de manual y texto plano

Existe además un hospedaje **grandioso** y **gratuito** para tus documentos Sphinx_:
`Read The Docs`_. Usalo. Puedes configurarlo commit hooks a tu repositorio fuente, 
de forma que reconstruir tu documentación ocurrirá automáticamente. 

Cuando se ejecuta, Sphinx_ importará tu código y usando las características de 
introspección de python, extraerá todas las funciones, métodos y classes signature. 
Tambien extraerá los docstrings que lo acompañan, y compilará todo en documentación
bien estructurada y fácil de leer para tu proyecto.

.. nota::

    Sphinx es famoso por su generación de API, pero tambien funciona bien 
    para documentación general de proyectos. Esta guía fue construida con
    Sphinx_ y alojada en `Read The Docs`_

.. _Sphinx: https://www.sphinx-doc.org
.. _Read The Docs: http://readthedocs.org

.. _restructuredtext-ref:

reStructuredText
~~~~~~~~~~~~~~~~

La mayoría de la documentación de Python es escrita con reStructuredText_. 
Es como Markdown, pero con todas las extensiones opcionales incorporadas. 

El `reStructuredText Primer`_ y la `referencia rápida a reStructuredText`_ 
debería ayudarte a familiarizarte con su sintaxis.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _reStructuredText Primer (inglés): https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _reStructuredText Referencia rápida (inglés): http://docutils.sourceforge.net/docs/user/rst/quickref.html


*************************
Consejo para documentar código
*************************

Los comentarios aclaran el código y son añadidos para hacer el código más fácil de entender. En Python, los comentarios empiezan con un signo numeral (``#``).

.. _docstring-ref:

En Python, los *docstrings* describen módulos, clases y funciones: 

.. code-block:: python

    def square_and_rooter(x):
        """Regresa la raiz cuadrada de self multiplicado por si mismo."""
        ...

En general, sigue sigue la seccion de comentarios de 
:pep:`8#comments` (la "guia de estilo de Python"). Para mas información acerca de docstrings: 
:pep:`0257#specification` (The Docstring Conventions Guide).

Comentando secciones de código.
~~~~~~~~~~~~~~~~~~~~~~~~~~~

*No uses cadenas con comillas triples para comentar código* 
No es una buena práctica, porque las herramientas orientadas a lineas de 
las líneas de comando, como grep, no notarán que el código comentado está inactivo. 
Es mejor añadir signos numerales (``#``) al nivel adecuado de indentación para cada línea comentada. 
Tu editor probablemente tenga la habilidad de hacerlo fácilmente, 
y vale la pena aprender aprender a comentar y descomentar.

Docstrings and Magic
~~~~~~~~~~~~~~~~~~~~

Algunas herramientas utilizan docstrings para insertar comportamientos mas allá de la documentación, como pruebas unitarias de lógica. 
Estas pueden ser buenas, pero no puede salir mal el "esto es lo que hace" de la versión "vainilla". 

Herramientas como Sphinx_ analizarán tus docstrings como un reStructuredText y lo renderizarán correctamente como HTML. Esto hace muy fácil insertar snippets de código de ejemplo en la documentación de un proyecto.

Additionally, Doctest_ will read all embedded docstrings that look like input
from the Python commandline (prefixed with ">>>") and run them, checking to see
if the output of the command matches the text on the following line. This
allows developers to embed real examples and usage of functions alongside
their source code. As a side effect, it also ensures that their code is
tested and works.

::

    def my_function(a, b):
        """
        >>> my_function(2, 3)
        6
        >>> my_function('a', 3)
        'aaa'
        """
        return a * b

.. _Doctest: https://docs.python.org/3/library/doctest.html

Docstrings versus Block comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These aren't interchangeable. For a function or class, the leading
comment block is a programmer's note. The docstring describes the
*operation* of the function or class:

.. code-block:: python

    # This function slows down program execution for some reason.
    def square_and_rooter(x):
        """Returns the square root of self times self."""
	...

Unlike block comments, docstrings are built into the Python language itself.
This means you can use all of Python's powerful introspection capabilities to
access docstrings at runtime, compared with comments which are optimized out.
Docstrings are accessible from both the `__doc__` dunder attribute for almost
every Python object, as well as with the built in `help()` function.

While block comments are usually used to explain *what* a section of code is
doing, or the specifics of an algorithm, docstrings are more intended towards
explaining other users of your code (or you in 6 months time) *how* a
particular function can be used and the general purpose of a function, class,
or module.

Writing Docstrings
~~~~~~~~~~~~~~~~~~

Depending on the complexity of the function, method, or class being written, a
one-line docstring may be perfectly appropriate. These are generally used for
really obvious cases, such as::

    def add(a, b):
        """Add two numbers and return the result."""
        return a + b

The docstring should describe the function in a way that is easy to understand.
For simple cases like trivial functions and classes, simply embedding the
function's signature (i.e. `add(a, b) -> result`) in the docstring is
unnecessary. This is because with Python's `inspect` module, it is already
quite easy to find this information if needed, and it is also readily available
by reading the source code.

In larger or more complex projects however, it is often a good idea to give
more information about a function, what it does, any exceptions it may raise,
what it returns, or relevant details about the parameters.

For more detailed documentation of code a popular style used, is the one used by the
NumPy project, often called `NumPy style`_ docstrings. While it can take up more
lines than the previous example, it allows the developer to include a lot
more information about a method, function, or class. ::

    def random_number_generator(arg1, arg2):
        """
        Summary line.

        Extended description of function.

        Parameters
        ----------
        arg1 : int
            Description of arg1
        arg2 : str
            Description of arg2

        Returns
        -------
        int
            Description of return value

        """
        return 42

The `sphinx.ext.napoleon`_ plugin allows Sphinx to parse this style of
docstrings, making it easy to incorporate NumPy style docstrings into your
project.

At the end of the day, it doesn't really matter what style is used for writing
docstrings; their purpose is to serve as documentation for anyone who may need
to read or make changes to your code. As long as it is correct, understandable,
and gets the relevant points across then it has done the job it was designed to
do.


For further reading on docstrings, feel free to consult :pep:`257`

.. _thomas-cokelaer.info: http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
.. _sphinx.ext.napoleon: https://sphinxcontrib-napoleon.readthedocs.io/
.. _`NumPy style`: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html


***********
Other Tools
***********

You might see these in the wild. Use :ref:`sphinx-ref`.

Pycco_
    Pycco is a "literate-programming-style documentation generator"
    and is a port of the node.js Docco_. It makes code into a
    side-by-side HTML code and documentation.

.. _Pycco: https://pycco-docs.github.io/pycco/
.. _Docco: http://jashkenas.github.com/docco

Ronn_
    Ronn builds Unix manuals. It converts human readable textfiles to roff
    for terminal display, and also to HTML for the web.

.. _Ronn: https://github.com/rtomayko/ronn

Epydoc_
    Epydoc is discontinued. Use :ref:`sphinx-ref` instead.

.. _Epydoc: http://epydoc.sourceforge.net

MkDocs_
    MkDocs is a fast and simple static site generator that's geared towards
    building project documentation with Markdown.

.. _MkDocs: http://www.mkdocs.org/
