#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 13:10:26 2018

@author: manveet
"""

i = int(input())
l=[]

for n in range(i):
    z = input()
    l.append(len(z))

l.sort()
k = max(l)
print(l.count(k))