#!/usr/bin/env python
"""This program print the multiplication table 1 to 10
Multiplication table 1:
1
2
3
...

------------
Multiplication table 2:
2
4
8
...
-----------
"""
__version__ = '0.1.0'
__author__ = 'Fabiano'

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = list(range(1, 11))


#Itarables
for number in numbers:
    print('Multiplication table:', number) 
    for other_number in numbers:
        print(number * other_number)
    print('-----------')
