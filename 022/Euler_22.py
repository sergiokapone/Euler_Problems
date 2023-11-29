# -*- coding: utf-8 -*-
"""
Используйте names.txt, текстовый файл размером 46 КБ, содержащий более пяти тысяч имён. Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.

Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-ым в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.

Какова сумма очков имён в файле?
"""
# Read data from file
#import string
#abc = list(string.ascii_uppercase)

filename = 'Euler_22_.dat'
#data = [line.strip() for line in open(filename, 'r')]
#data.sort()
#codes = dict(  zip(list(string.ascii_uppercase), range(1,len(string.ascii_uppercase)+1)))
#
#
#
#total_score = sum( [(word + 1)*sum([codes[char] for char in data[word]]) for word in range(len(data))] )
#
#print(total_score)

with open(filename) as f:
    datas = sorted(map(lambda s: str.upper(s[1:-1]),f.read().split(",")))
    print(sum(  [(i+1)*sum([(ord(x)-64) for x in datas[i]]) for i in range(len(datas))]  ))