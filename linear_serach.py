#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 21:35:43 2018

@author: manveet
"""
def linear_search(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    count=0
    flag = 0
    for i in element:
        count+=1
        if(i==x):
            print("Yes!! I Found mynumber at position:"+str(i))
            flag = 1
            break
            
    if(flag==0):
        print("Number is not found")
        
        
    print("Number of Iteratons : "+str(count))
    


    
    