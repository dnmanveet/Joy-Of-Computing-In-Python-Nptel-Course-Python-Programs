#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 15:38:13 2018

@author: manveet
"""
import random
year = random.randint(1992,2018)
print(year)
if(year%4 == 0 and year%100 != 0 or year%400 == 0):
    print("Given year is a leap yesr")
else:
    print("Given year is not a leap year")
    
     
    
