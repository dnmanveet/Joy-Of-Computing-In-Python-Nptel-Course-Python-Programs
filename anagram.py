#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 15:18:24 2018

@author: manveet
"""

str1 = input("Enter the first string ")
str2=input("enter the second string ")
count1 = 0
i=0
while(i<len(str1)):
    count1 = count1+ord(str1[i])
    i = i+1
count2 = 0
i=0
while(i<len(str2)):
    count2 = count2+ord(str2[i])
    i = i+1
if(count1 == count2):
    print("These are Anagrams")
else:
    print("These are not Anagrams")
    
    
 