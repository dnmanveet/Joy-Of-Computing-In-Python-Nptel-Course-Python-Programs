#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 22:47:45 2018

@author: manveet
"""
import random

def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition','reverse','water','board']
    pick=random.choice(words)
    return pick

def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(p1n,p2n,p1,p2): 
    print(p1n,' Your score is : ',p1)
    print(p2n,' Your score is : ',p2)
    print('Thanks for playing')
    print('have a nice day')
    
def play():
    p1name=input('player1,plz enter ur name ')
    p2name=input('player 2,Plz enter ur name ')
    pp1=0
    pp2=0
    turn=0
    while(1):
        #computers task
        picked_word = choose()
        #create question
        qn = jumble(picked_word)
        print(qn)
        # player 1
        if turn%2==0 :
            print(p1name,' Your turn, ')
            ans=input('what is on my mind ')
            if ans == picked_word:
                pp1=pp1+1
                print('your score is : ',pp1)
            else:
                print('Better luck next time. I thought : ',picked_word)
            c = int(input('Press 1 to continue and 0 to quit : '))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
            elif c==1:
                continue
        # player 2
        else:
            print(p2name,' Your turn, ')
            ans=input('what is on my mind ')
            if ans == picked_word:
                pp2=pp2+1
                print('your score is : ',pp2)
            else:
                print('Better luck next time. I thought : ',picked_word)
            c = int(input('Press 1 to continue and 0 to quit : '))
            if c==0:
                thank(p1name,p2name,pp1,pp2)
                break
            elif c==1:
                continue
        turn=turn+1
            
play()