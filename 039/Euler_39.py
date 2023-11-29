# -*- coding: utf-8 -*-
"""
Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, то существует ровно три решения для p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает максимальное число решений?
"""


counter, max_val, lst, count,  = 0, 0, [], {}


                    
for p in range(1, 1000+1):
    for a in range(1, int(p/2)):
        for b in range(a + 1, int( p/2) ):
            if ((p - a - b)**2 == a**2 + b**2):
                counter += 1
    if counter != 0 and counter > max_val:
        max_val = counter
        count[p] = max_val
    counter = 0

import collections
print(collections.OrderedDict(sorted(count.items())))            


