#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:22:47 2018

@author: manveet
"""
import random
import matplotlib.pyplot as plt 

account=0
x=[]
y=[]

#h = int(input("how many days u want to play"))
for i in range(365):
    x.append(i+1)
    bet = random.randint(1,10)
    lucky_draw=random.randint(1,10)
#    print("Bet : ",bet )
#    print("Lucky draw : ",lucky_draw )
    
    if bet == lucky_draw:
        account = account+900-100
    else:
        account = account-100
    y.append(account)
print(account)
plt.plot(x,y)
plt.show()