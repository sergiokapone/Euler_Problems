# -*- coding: utf-8 -*-
"""
Сумма простых чисел меньше 10 - это 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов...
"""

from math import sqrt
def is_prime(number):
    for i in reversed(range(2,int(sqrt(number))+1)):
        if number % i == 0: 
               return False
               break
    return True
              
sum = 2
for i in range(3,2000000,2):
    if is_prime(i):
        sum +=i

print(sum)
            
            