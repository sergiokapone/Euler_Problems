# -*- coding: utf-8 -*-
"""
Задача 18
Максимальная сумма пути 1
http://euler.jakumo.org/problems/view/18.html
"""

# %% Source data
trinum = [
[75],
[95, 64],
[17, 47, 82],
#[18, 35, 87, 10],
#[20,  4, 82, 47, 65],
#[19,  1, 23, 75,  3, 34],
#[88,  2, 77, 73,  7, 63, 67],
#[99, 65,  4, 28,  6, 16, 70, 92],
#[41, 41, 26, 56, 83, 40, 80, 70, 33],
#[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#[63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
]


# %% brute force

"""
Каждый шаг вниз кодировать '0', а вправо — '1', путь будет кодироваться последовательностью нулей и единиц.
Генереруем пути как размещение из '0' и '1' по 14 (2^14 = 16 348 путей) и перебираем.
"""
# def path_integral(path, trinum):
#     i, j = 0, 0
#     summ = trinum[0][0]
#     for index in path:
#         if index == 0 and i + 1 <= len(trinum) - 1:
#             i += 1
#             summ += trinum[i][j]
#         elif index == 1 and i + 1 <= len(trinum) - 1:
#             j += 1
#             i += 1
#             summ += trinum[i][j]
#     return summ
#
# from itertools import product
# result = 0
# the_path = ()
# for path in product((0,1),repeat = len(trinum)):
#     if result < path_integral(path, trinum):
#         result = path_integral(path, trinum)
#         the_path = path
#==============================================================================

# %% Least Action Principle
ms=0 # maxsum
def sub( r, c, s ): # row, column, sum
    r+=1
    if r==len(trinum):
        global ms
        if s>ms: ms=s
        return 0
    for i in [0,1]: 
        sub( r, c+i, s+trinum[r][c+i] )

sub( 0, 0, trinum[0][0] )
print(ms)
    
#from functools import reduce
#print(reduce(lambda p,n:map(lambda i:n[i]+max(p[i],p[i+1]),range(len(n))),\
#  reversed(trinum)))



