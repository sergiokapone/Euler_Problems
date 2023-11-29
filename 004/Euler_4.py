# -*- coding: utf-8 -*-
"""
Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково. Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.

Найдите самый большой палиндром, полученный умножением двух трёхзначных чисел.
"""

palindrom = 0
palindrom_list = []
for i in range(100,1000):
    for j in range(i,1000):
        number = i*j
        if (str(number) == str(number)[::-1]) and (palindrom < number):
            palindrom = number
            palindrom_list.append(number)
            
print(palindrom) 
print(list(palindrom_list))

#max([x*y for x in range(100,1000) for y in range(100,1000) if str(x*y) == str(x*y)[::-1]])