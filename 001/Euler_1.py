# -*- coding: utf-8 -*-
"""
Задача 1
Числа, кратные 3 или 5
Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел - 23.

Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

"""

# Imperative style

def sum_of_multipliers(n):
    total_sum = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            total_sum += i
    return total_sum
 
print(sum_of_multipliers(1000))

# Semifunctional style (with 'for' for list creation)

n = 1000
list = [i for i in range(n) if (i % 3 == 0) or (i % 5 == 0)]       # list generating
total_sum = sum(list)
print(total_sum)

# Complete functional style

total_sum = sum(filter(lambda x: (x%5==0) or (x%3==0), range(n)))
print(total_sum)
