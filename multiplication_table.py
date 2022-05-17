#!/usr/bin/env python
"""This program print the multiplication table 1 to 10
---Multiplication table 1---

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3

...
############################
------------
---Multiplication table 2---

    1 x 2 = 2
    2 x 2 = 4
    3 x 2 = 8

...
############################
"""
__version__ = '0.1.1'
__author__ = 'Fabiano'



#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Iterable
numbers = list(range(1, 11))


#For each number in numbers:
for number1 in numbers:
    print('{:-^28}'.format(f'Multiplication Table {number1}'))
    print()
    for number2 in numbers:
        result = number1 * number2
        print('{:^28}'.format(f'{number1} x {number2} = {result}'))
    
    print('#' * 28)
