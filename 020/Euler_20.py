# -*- coding: utf-8 -*-
"""
n! означает n × (n − 1) × ... × 3 × 2 × 1

Найдите сумму цифр в числе 100!.
"""
fac = lambda n: 1 if n == 0 else n*fac(n-1)
sum(map(int, str(fac(100)))) 
        



