# -*- coding: utf-8 -*-
"""
Правила записи чисел римскими цифрами позволяют записывать одно и то же число несколькими способами (см. FAQ: Римские числа). Однако, всегда существует "наилучший" способ записи определенного числа.

К примеру, ниже представлены все разрешенные способы записи числа шестнадцать:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

Последнее из них считается наиболее эффективным, поскольку использует наименьшее число римских цифр.

В текстовом файле roman.txt размером 11KБ тысяча чисел записана римскими цифрами правильным, но не обязательно наилучшим способом, т.е. они отсортированы в порядке убывания и подчиняются правилу вычитания пар (для информации об определяющих правилах данной задачи см. FAQ).

Найдите число символов, сэкономленных путем перезаписи каждого числа в его наиболее короткий вид.

Примечание: Можете считать, что все числа в файле содержат не более четырех последовательных одинаковых цифр.

"""
filename = 'p089_roman.txt'
conformity = {
'I': 1, 
'V': 5, 
'X': 10, 
'L': 50, 
'C': 100, 
'D': 500, 
'M': 1000
}

reverted_conformity = dict((y,x) for x,y in conformity.items())
Roman_numbers = [line.strip() for line in open(filename, 'r')]


def roman_to_arabic(num):
    arn = [conformity[Roman]  for Roman in num]
    arn2 = []
    for i in range(0,len(arn)):
        if max(arn[i:]) == arn[i:][0]:
            continue
        else:
            max(arn[i:]) > arn[i:][0]
            arn2.append(arn[i:][0])
    return (sum(arn) - 2*sum(arn2))

    



def arabic_to_roman(num):
    roman_num = []
    digit = lambda d: int(str(num)[::-1][d])
    for order in (range(0,len(str(num)))[::-1]):
        if digit(order) <= 3:
            roman_num.append(digit(order)*reverted_conformity[10**order])
        elif (digit(order) == 4) and (order < 3):
            roman_num.append(reverted_conformity[10**order] + reverted_conformity[5*10**order])
        elif (order == 3):
            roman_num.append(digit(order)*reverted_conformity[10**order])
        elif 5<=digit(order) <=8:
            roman_num.append( reverted_conformity[5*10**order] + (digit(order) - 5) * reverted_conformity[10**order])
        elif (digit(order) <= 9) :
            roman_num.append((10 - digit(order) )*reverted_conformity[10**order] + reverted_conformity[10**(order+1)])
    return (''.join(roman_num))
    


summ = 0   
for number in Roman_numbers:
    summ += len(number) - len(arabic_to_roman(roman_to_arabic(number)))
    print(roman_to_arabic(number))
    print(number, ' ---> ', arabic_to_roman(roman_to_arabic(number)))
print(summ)



#count = 0
#for j in Roman_numbers:
#    if 'IIII' in j:
#        count = count + 2
#for j in Roman_numbers:
#    if 'VIIII' in j:
#        count = count + 1 
#for j in Roman_numbers:
#    if 'XXXX' in j:
#        count = count + 2
#for j in Roman_numbers:
#    if 'LXXXX' in j:
#        count = count + 1
#for j in Roman_numbers:
#    if 'CCCC' in j:
#        count = count + 2
#for j in Roman_numbers:
#    if 'DCCCC' in j:
#        count = count + 1
#print(count)



#import csv
#
#decimal_eq = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
#roman_eq = ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
#roman_decimal_map = zip(decimal_eq, roman_eq)
#
#
#def toRoman(x):                                 
#    result = list()                                                 
#    for decimal_eq, roman_eq in roman_decimal_map:                  
#        count = x // decimal_eq
#        print(count)
#        result.append(roman_eq * count)                             
#        x -= decimal_eq * count
#        print(result)
#        print(count)                                     
#    return ''.join(result)                                          
#
#def toDecimal(romanStr):
#    romanStr = romanStr.upper()
#    i, result = 0, 0
#    for decimal_eq, roman_eq in roman_decimal_map:
#        while romanStr[i:i + len(roman_eq)] == roman_eq:
#            result += decimal_eq
#            print(result)
#            i += len(roman_eq)
#            print(i)
#    return result
#
#
#L = list()
#with open('p089_roman.txt', 'r') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        for item in row:            
#            L.append(item)

    
    
    









    
