

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

Algunas herramientas utilizan docstrings para insertar
comportamientos mas allá de la documentación, como pruebas 
unitarias de lógica. Estas pueden ser buenas, pero no 
puede salir mal el "esto es lo que hace" de la versión "vainilla". 

Herramientas como Sphinx_ analizarán tus docstrings 
como un reStructuredTexty lo renderizarán correctamente 
como HTML. Esto hace muy fácil insertar snippets de código de ejemplo en la documentación de un proyecto.

Adicionalmente, Doctest_ leerá todos los docstrings incrustados que parecen un input de 
python en la línea de comandos (con el prefijo ">>>") y los correran, 
verificando que las salidas de los comandos coincidan con el texto de 
la línea siguiente. Esto permite a los desarrolladores insertar ejemplos
reales y uso de funciones junto a su código fuente. Además, esto asegura
que su código es probado y realmente funciona. 

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

Docstrings contra Block comments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No son intercambiables. Para una función o clase, el bloque de 
comentario inicial es una nota del programador. El docstring 
describe la *operación* de la función o clase: 

.. code-block:: python

    # Esta función alenta la ejecución del programa por alguna razón.
    def square_and_rooter(x):
        """Devuelve la raiz cuadrada de sí mismo por sí mismo."""
	...

A diferencia de los bloques de comentario, los docstrings forman parte del 
lenguaje de Python. 
Eso significa que puedes usar todas las poderosas capacidades de instrospección
de python para acceder a los docstrings en la ejecución, comparado con los comentarios 
que están optimizados. 
Los docstrings son accesibles desde el atributo dunder `__doc__` para casi 
cualquier objeto de Python, así como la función `help()`.

Mientras los bloques de comentarios son usados generalmente para explicar *qué*
hace una sección de código, o las especificaciones de un algorítmo, los docstrings
se enfocan en explicar a otros usuarios tu código (o tú 6 meses despues) *cómo*
una función particular puede ser usada y el propósito general de una función, 
clase o módulo. 

Escribiendo Docstrings
~~~~~~~~~~~~~~~~~~

Dependiendo de la complejidad de una función, método o clase siendo escrita, 
un docstring de una línea puede ser perfectamente apropiado. Estos son generalmente
utilizados para situaciones muy obvias como:: 

    def add(a, b):
        """Add two numbers and return the result."""
        return a + b

Los docstrings deben describir la función de forma que sea fácil de entender. 
Para casos simples, como funciones triviales y clases, simplemente 
agregando la firma de la función (por ejemplo `añadir(a, b) -> resultado`) en 
el docstring es innecesario. Esto es porque con el módulo `inspect` de Python, 
ya es suficientemente sencillo encontrar esta información si es necesario, y 
tambien está disponible a la vista al leer el código fuente. 

Sin embargo, en proyectos mas grandes o complejos, usualmente es buena idea 
dar mas información acerca de una función, lo que hace, cualquier excepción 
que pueda dar, los retornos, o detalles importantes acerca de los parámetros.

Para documentación mas detallada código, un estilo popular utilizado es el que 
utiliza el proyecto NumPy, conocido como `NumPy style`_ docstrings. Mientras esto 
puede llevar mas líneas que los ejemplos anteriores, permite al desarrollador
incluir mucha más información acerca de un método, función o clase. ::

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

El plugin `sphinx.ext.napoleon`_ permite a Sphinx analizar este estilo de 
docstrings, haciendo mas fácil incorporar el estilo de Numpy docstrings a 
tu proyecto. 

Al final del día, realmente no importa cual estilo se utilice para escribir
docstrings; su proposito es servir como documentación para cualquiera que 
pueda necesitar leer o hacer cambios en tu código. Mientras este sea correcto,
entendible y tenga puntos relevantes, entonces ha hecho el trabajo para el que
ha sido diseñado. 


Para mas información acerca de docstrings, sientete libre de consultar :pep:`257`

.. _thomas-cokelaer.info: http://thomas-cokelaer.info/tutorials/sphinx/docstring_python.html
.. _sphinx.ext.napoleon: https://sphinxcontrib-napoleon.readthedocs.io/
.. _`NumPy style`: http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html


***********
Otras herramientas
***********

Puedes haber visto las siguientes herramientas. Usa :ref:`sphinx-ref`.

Pycco_
    Pycco is a "generador de documentación de estilo de programación alfabetizada"
    y es portado de Docco, portado de node.js. Convierte el código a código 
    HTML lado a lado, y documentación. 
    
.. _Pycco: https://pycco-docs.github.io/pycco/
.. _Docco: http://jashkenas.github.com/docco

Ronn_
    Ronn construye manuales Unix. Convierte archivos de texto legibles por humanos a
    roff para mostrarse en terminal, así como HTML para la web. 
    
.. _Ronn: https://github.com/rtomayko/ronn

Epydoc_
    Epydoc está descontinuado. Usa :ref:`sphinx-ref` en su lugar.

.. _Epydoc: http://epydoc.sourceforge.net

MkDocs_
    MkDocs es un rápido y simple generador de sitios estaticos enfocado a construir 
    documentación de proyectos con Markdown. 
    
.. _MkDocs: http://www.mkdocs.org/
