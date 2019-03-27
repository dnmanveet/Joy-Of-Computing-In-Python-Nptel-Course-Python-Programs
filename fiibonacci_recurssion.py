#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 12:06:48 2018

@author: manveet
"""
# =============================================================================
# def fibonnaci(i):
#     first = 0
#     second = 1
#     print(first)
#     print(second)
#     third=first+second
#     while(True):
#         if(third == i):
#             break
#         else:
#             first = second
#             second = third
#             third = first+second
#         print(third)
#         
# =============================================================================
def fibonnaci(n):
    if n<2:
        return n
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
print(fibonnaci(4))
    
  
   
    
    
