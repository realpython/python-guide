Command Line Applications
=========================

.. todo:: Explain "Command Line Applications"

Clint
-----

.. todo:: Write about Clint

commando
--------
`commando <https://github.com/lakshmivyas/commando>`_ - argparse in style

A simple wrapper for argparse that allows commands and arguments to be 
defined declaratively using decorators. Note that this does not support 
all the features of argparse yet.

With commando:

.. code-block:: python

    class Engine(Application):

        @command(description='hyde - a python static website generator',
                epilog='Use %(prog)s {command} -h to get help on individual commands')
        @param('-v', '--version', action='version', version='%(prog)s ' + __version__)
        @param('-s', '--sitepath', action='store', default='.', help="Location of the hyde site")
        def main(self, params): pass

        @subcommand('init', help='Create a new hyde site')
        @param('-t', '--template', action='store', default='basic', dest='template',
                help='Overwrite the current site if it exists')
        @param('-f', '--force', action='store_true', default=False, dest='overwrite',
                help='Overwrite the current site if it exists')
        def init(self, params):
            print params.sitepath
            print params.template
            print params.overwrite

