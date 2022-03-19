# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 21:40:18 2022

@author: Osval
"""

from random import random
from math import sqrt,log,cos,pi
import matplotlib.pyplot as plt
def gen():
    u1=random()
    u2=random()
    return sqrt(-2*log(u1))*cos(2*pi*u2)
l=[]
n=1000000
for i in range(n):
    l.append(gen())
plt.hist(l,bins=50,density=1,color='grey',edgecolor='black')
plt.show()
