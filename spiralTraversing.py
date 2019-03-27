#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 17:10:51 2018

@author: manveet
"""
import turtle
turtle.bgcolor("black")
seurat = turtle.Turtle()
from random import randint


dot_distance = 25
width = 5
height = 7

seurat.penup()
list_color = ["white","yellow","brown","red","blue","green","orange","pink","violet","green","grey"," cyan"]

seurat.setpos(-250,250)
def spiral(m,n): #actuall (m,n,a)
    k=0
    l=0
    f = 0
    seurat.color("white")
    '''
    k is index of starting row
    l is index of starting column
    '''
    col = randint(0,10)
    seurat.color(list-color[col])
    while(k<m and l<n):
        
        if (f==1):
            seurat.right(90)
        #Printing the first row from the remanng rows
        for i in range(l,n):
            seurat.dot()
            seurat.forward(dot_distance)
#            print(a[k][i], end=" ")
            
        k += 1
        f=1
        seurat.right(90)
        col = randint(0,10)
        seurat.color(list-color[col])
        #printing the last column from remaining column
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
#            print(a[i][n-1],end=" ")
        
        n -= 1
        seurat.right(90)
        col = randint(0,10)
        seurat.color(list-color[col])
        if(k < m):
            for i in range(n-1, l-1,-1):
#                print(a[m-1][i], end=" ")
                 seurat.forward(dot_distance)
                
            m -= 1
        seurat.right(90)
        col = randint(0,10)
        seurat.color(list-color[col])
        if(l<n):
            for i in range(m-1, k-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
#                print(a[i][l],end=" ")
            l += 1
        
#a = []
#count = 1
#for i in range(4):
#    l =  []
#    for j in range(4):
#        l.append(count) 
#        count += 1
#    a.append(l)
#     
#spiral(4,4,a)   
R=20;C=20
spiral(R,C)
turtle.done()
            
    
