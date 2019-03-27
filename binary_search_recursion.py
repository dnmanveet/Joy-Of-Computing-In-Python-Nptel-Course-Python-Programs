#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:44:40 2018

@author: manveet
"""
l=[1,2,3,4,5]
def binary_search(l,x,start,end):
    #Base case is one element in the list
    if start==end:
        if l[start]==x:
            return start
        else:
            return -1
    else:
        mid=int((start+end)/2)
        if(x==l[mid]):
            return mid
        else:
            if(x>l[mid]):
                return binary_search(l,x,mid+1,end)
            elif(x<l[mid]):
                return binary_search(l,x,start,mid-1)
x=int(input("eneter searh key : "))
index=binary_search(l,x,0,len(l)-1)
if(index == x):
    print(x,' Element not found ')
else:
    print(x, ' is found at position ', str(index+1))         
            
        
        
            
            
    
    