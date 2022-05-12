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
__version__ = "0.0.1"
__author__ = "Fabiano Alves"
__license__ = "Unlicense"

import os

current_language = os.getenv('LANG','en_US')[:5]
message = 'Hello World'

if current_language == 'pt_BR':
    message = 'Olá Mundo'
elif current_language == 'it_IT':
    message = 'Ciao Mondo'
elif current_language == 'es_SP':
    message = 'Hola Mundo'
elif current_language == 'fr.FR':
    message = 'Bonjour Monde'
print (message)
