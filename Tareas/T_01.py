# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 19:47:18 2022

@author: Osval
"""

from random import random
import matplotlib.pyplot as plt
from math import pi
N=1000000
n=0
epsilon=0.001
lx=[]
ly=[]
ls=[]
li=[]
lpi=[]
for i in range(N):
    x=random()
    y=random()
    if x**2+y**2<1:
        n=n+1
        if i %10000==0 and i>0:
            lx.append(i)
            ly.append(4*n/i)
            lpi.append(pi)
            ls.append(pi+epsilon)
            li.append(pi-epsilon)
print(4*n/N)
plt.plot(lx,ly)
plt.plot(lx,lpi)
plt.plot(lx,ls)
plt.plot(lx,li)
plt.xlabel("Número de dardos")
plt.ylabel("aproximacion a pi")       
plt.show()   
