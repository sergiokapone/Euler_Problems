# -*- coding: utf-8 -*-
"""
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
"""
from math import sqrt
def is_prime(number):
    for i in reversed(range(2,int(sqrt(number))+1)):
        if number % i == 0:
               return False
               break
    return True

def max_divider(number):
    get_it = False
    divider = int(sqrt(number))
    while get_it == False:
          if (number % divider == 0) and (is_prime(divider)):
              get_it = True
              return divider
              break
          else:
              divider -= 1

print(is_prime(6857))
print(max_divider(600851475143))

roots = []; product = 1; x = 2; number = 16; y = number
while product != number:
     while (y % x == 0):
       roots.append(x)
       y /= x
       product *= roots[-1]
     x += 1
print(roots)
