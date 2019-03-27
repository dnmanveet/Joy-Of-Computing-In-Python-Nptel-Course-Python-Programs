#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 12:40:07 2018

@author: manveet
"""

def magic_square(n):
    magicSquare = []
    for i in range(n):
        l = []
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
#    for i in range(n):
#        #l = []
#        for j in range(n):
#            print(magicSquare[i][j],end=" ")
#            #l.append(0)
#        print()
            
    i=int(n/2)
    j=n-1
    num = n*n
    count = 1
    
    while(count<=num):
        if(i==-1 and j==n): #condition 4
            j = n-2
            i = 0
        else:
            if(j==n):  #if column exceeeding
                j = 0
            if(i<0):   #row is becoming -1
                i = n-1
        if(magicSquare[i][j] != 0):
            j = j-2
            i = i+1
            continue
        
        else:
             magicSquare[i][j] = count
             count += 1
             i = i-1
             j = j+1 
       
               #CONDITION 1
    
    for i in range(n):
        #l = []
        for j in range(n):
             print(magicSquare[i][j],end=" ")
           #l.append(0)
        print()
          
        
       
        
    
                
    
            