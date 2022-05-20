#!/usr/bin/env python3

"""Shows a report of children by activity.

Print a list of children, grouped by activity in classes
"""
__version__ = '0.1.1'

#Data
classroom1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
classroom2 = ['Joao', 'Antonio', 'Carlos',  'Maria', 'Isolda']

english_class = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
music_class = ['Erik', 'Carlos', 'Maria']
dance_class = ['Gustavo', 'Sofia', 'Joana', 'Antonio']

activities = [
    ('English', english_class),
    ('Music', music_class),
    ('Dance', dance_class),
 ]

#List students in activity, by class

for name_activity, activity in activities:

    print(f'Students of the {name_activity} activity \n')
    print('-' * 50)

    #Class 1 have intersection with a activity

    activity_room1 = set(classroom1) & set(activity)
    activity_room2 = set(classroom2) & set(activity)

    
    print('classroom 1', activity_room1)
    print('classroom 2', activity_room2)

    print()
    print('*' * 50)
