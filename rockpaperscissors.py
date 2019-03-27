#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 15:35:15 2018

@author: manveet
"""
def rock_paper_scissors(num1,num2,bit1,bit2):
    p1=int(num1[bit1])%3
    p2=int(num2[bit2])%3
    if(player_one[p1]==player_two[p2]):
        print("Draw") 
    elif(player_one[p1]=="Rock" and player_two[p2]=="Scissors"):
        print("Player one wins! !")
    elif(player_one[p1]=="Rock" and player_two[p2]=="Paper"):
        print("Player two wins! !")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Rock"):
        print("Player one wins! !")
    elif(player_one[p1]=="Paper" and player_two[p2]=="Scissors"):
        print("Player two wins! !")
    elif(player_one[p1]=="Scissors" and player_two[p2]=="Paper"):
        print("Player one wins! !")
    elif(player_one[p1]=="Scissors" and player_two[p2]=="Rock"):
        print("Player two wins! !")
    
        
    
player_one={0:'Rock',1:'Paper',2:'Scissors'}
player_two={0:'Paper',1:'Rock',2:'Scissors'}
while(1):
    num1=input("player one,enter our choice ")
    num2=input("player two,enter our choice ")
    bit1=int(input("Player one, Enter the secret bit position "))
    bit2=int(input("Player two, Enter the secret bit position "))
    rock_paper_scissors(num1,num2,bit1,bit2)
    ch=input("do u want to contiue? y/n")
    if(ch=='n'):
        break
    
    
