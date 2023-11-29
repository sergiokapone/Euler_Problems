# -*- coding: utf-8 -*-
"""
Consider the number 142857. We can right-rotate this number by moving the last digit (7) to the front of it, giving us 714285.
It can be verified that 714285=5×142857.
This demonstrates an unusual property of 142857: it is a divisor of its right-rotation.

Find the last 5 digits of the sum of all integers n, 10 < n < 10^100, that have this property.
"""
summa  = 0
for num in range(10,10**6):
    for k in range(2,10):
        p = str(num)[-1] + str(num)[:-1]
        if divmod(int(p), num) == (k , 0):
            print(num)
            summa += int(num)


#==============================================================================
# sum([n for n in range(10,10**8) if int(str(n)[-1] + str(n)[:-1]) % n == 0 and int(str(n)[-1] + str(n)[:-1]) / n == int(str(n)[-2]) and int(str(n)[-2]) != 1])
#==============================================================================


sum2 = summa
for i in range(2,101):
    num = int(i * '1')
    sum2 += sum([num * i for i in range(1,10)])

