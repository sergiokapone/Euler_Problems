# -*- coding: utf-8 -*-
"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13. Очевидно, что 6-ое простое число - 13.

Какое число является 10001-ым простым числом?
"""
from math import sqrt
def is_prime(number):
    for i in reversed(range(2,int(sqrt(number))+1)):
        if number % i == 0: 
               return False
               break
    return True 

number = 1
counter = 1
while (counter <= 10001):
    number += 1
    if is_prime(number):
        counter += 1  
    
print(number)
print(counter-1)
