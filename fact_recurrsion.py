#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:37:00 2018

@author: manveet
"""
def fact(n):
    if(n==1 or n==0):
        return 1
    elif(n>1):
        return n*fact(n-1)
    else:
        print('Incorrect Number')