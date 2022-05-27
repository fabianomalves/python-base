#!/usr/bin/env python3
"""Product registration"""
__version__ = '0.1.0'

from pprint import pprint #Pretty print for best print debug

product =  {
'name' : 'Pen',
'colors' : ['blue', 'white'],
'price' : 3.23,
'dimension' : {
    'height' : 12.1,
   'weight' : 0.8
},
'in_stock' : True,
'code' : 45678,
'barcode' : None,
}

client = {
    'name': 'Fabiano'
}

purchase = {
    'client': client,
    'product': product,
    'quantity': 3
}

#pprint(purchase)

total_purchase = purchase['quantity'] * purchase['product'] ['price']

print(
    f"The client {purchase['client']['name']} "
    f"bought {purchase['quantity']} {purchase['product'] ['name']} units"
    f" and pay the total cost of {total_purchase}"
)
