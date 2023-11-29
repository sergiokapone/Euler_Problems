# -*- coding: utf-8 -*-
"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""
from math import sqrt
from decimal import*
getcontext().prec = 1000

# Binet's Formulae
# https://en.wikipedia.org/wiki/Fibonacci_number
# phi = Decimal((1 + sqrt(5))/2.)     
# fib = lambda n: int((Decimal(phi**n) - Decimal((-phi)**(-n)) )/Decimal(2*phi - 1))
# 
# n = 1
# while True:
#     if len(str(fib(n))) == 1000:
#         print(n)
#         break
#     n += 1


# Good algorithm
x = 1
y = 1
u = 0
i = 2
while u < 1000:
    i += 1
    F = x + y
    x = y
    y = F
    u = len(str(y))
    if u == 1000:
        print(i)
        print(y)


