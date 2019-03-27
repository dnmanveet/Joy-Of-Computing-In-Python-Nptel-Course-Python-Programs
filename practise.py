#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 22:26:16 2018

@author: manveet
"""


N = int(input())
list = []
for i in range(N):
    s = input().split()
    cmd  = s[0]
    if(str(s[1]) != "" or str(s[1]) != " " or s[1] != null ):
        pos = int(s[1])
    if(str(s[2]) != ""):
        ele = int(s[2]) 
    if(cmd == 'insert'):
        list.insert(pos,ele)
    elif(cmd == 'append'):
        list.append(pos)
    elif(cmd == 'remove'):
        list.remove(pos)
    else:
        for i in list:
            print(i)
    print()
        
            
        
        
        