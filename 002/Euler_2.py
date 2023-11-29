# -*- coding: utf-8 -*-
"""
Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
"""
from functools import reduce

# Creating Function, which is calculate 'n'th Fibonacci term
fib = lambda n: 1 if (n == 1) else 2 if (n == 2) else fib(n - 1) + fib(n - 2) # Fibonacci 'n'th sequence element



