# -*- coding: utf-8 -*-
"""
Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство

a^2 + b^2 = c^2
Например, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
"""
from math import sqrt
for a in range(1,1001):
    for b in range(a,1001):
        c = sqrt(a**2 + b**2)
        if float(c).is_integer() and (a + b + int(c) == 1000):
            print(a*b*int(c))
            break 
            
            