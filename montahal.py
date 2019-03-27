#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 14:53:05 2018

@author: manveet
"""
import random
doors=[0]*3
goatdoor=[0]*2
swap=0 #Num of swap wins
dont_swap=0 #Num of no swap wins
x=random.randint(0,2) #xth will comprise of BMW
doors[x]="BMW"
j=0
while(j<10):
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]="Goat"
            goatdoor.append(i)
    choice=int(input("Enter your choice "))
    door_open=random.choice(goatdoor) #open a door that comprises of goat
    while(door_open == choice):#door_open should not be equal to choice
        door_open=random.choice(goatdoor)
    ch =input("Do you want to swap? y/n ")
    if(ch == 'y'):
        if(doors[choice] == 'Goat'):
            print("player wins")
            swap=swap+1
        else:
            print("Player lost")
    else:
        if(doors[choice] == 'Goat'):
            print("Player lost")
        else:
            print("Player wins")
            dont_swap = dont_swap+1
    j=j+1
print("swap : ",swap)
print("dontswap : ",dont_swap)    
        

