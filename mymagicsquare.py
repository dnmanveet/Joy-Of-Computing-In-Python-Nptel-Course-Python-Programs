#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 13:15:36 2018

@author: manveet
"""
def magic_square(n):
    magicSquare = []
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)
        
# =============================================================================
#     for i in range(n):
# #        l=[]
#         for j in range(n):
#              print(magicSquare[i][j],end=" ")
# #            l.append(0)
#         print()
# =============================================================================
       
    i = int(n/2)
    j = n-1
    count = 1;
    pos = n*n
    while(count<=pos):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(i < 0):
                i = n-1
            
            elif(j == n):
                j = 0
        if(magicSquare[i][j] != 0):
            i = i+1
            j = j-2
            continue
               
        else:
            magicSquare[i][j] = count
            count +=1
            i = i-1
            j = j+1
               
            
            
               
    for i in range(n):
        for j in range(n):
            print(magicSquare[i][j],end=" ")
        print()
    print("Sum of each row/column/diagonal "+str((n*(n**2+1))/2))    
    
magic_square(3)
           
            
        
        
            
            
