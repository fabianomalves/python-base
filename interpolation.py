#!/usr/bin/env python3
"""Script with a template. Using for automatizing an email response.
"""
__version__ = "0.0.1"
__author__ = "Fabiano Alves"


email_template = """
Hello, %(name)s!

Do you want to buy this %(product)s?

This %(product)s is a great product to %(text)s.

Click here to buy %(link)s

Only %(quantity)d available.

Promotional price %(price).2f

"""

clients = ['Fabiano', 'Bruno', 'Maiara']

for client in clients:
    print(
        email_template
        % {
            'name': client,
            'product': 'pen',
            'text': 'write beautiful colored lines',
            'link': 'https://nicepen.com',
            'quantity': 1,
            'price': 50.5
          }
        )

