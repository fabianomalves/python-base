#!/usr/bin/env python3
"""Hello World Multi Languages.

Depending on the language configured in the environment, the program displays the message
corresponding.

How to use:

Have the LANG variable properly set. example:

    export LANG=pt_BR

Acting:

    python3 hello.py
    or
    ./hello.py
"""
__version__ = "0.1.2"
__author__ = "Fabiano Alves"
__license__ = "Unlicense"

import os

current_language = os.getenv('LANG','en_US')[:5]
message = {
    'pt_BR': 'Olá Mundo.',
    'en_US': 'Hello World.',
    'it_IT': 'Ciao Mondo.',
    'es_SP': 'Hola Mundo.',
    'fr_FR': 'Bonjour Monde.',
}

# sets (Hash Table) - O(1) Constant time


print (message[current_language])
