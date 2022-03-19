# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 18:33:22 2022

@author: Osval
"""

from random import random
from math import log
def g(x):
    return 1/(3*x+2)
n=1000000
suma=0
for i in range(n):
    x=random()
    suma=suma+g(x)
print(3*suma/n,log(5/2))   
