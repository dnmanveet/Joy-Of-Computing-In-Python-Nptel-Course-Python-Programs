#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:47:40 2018

@author: manveet
"""

import numpy
board=numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1s='X'
p2s='O'
turn = 0
def place(symbol):
    print(numpy.matrix(board))
    row = int(input("Enter row - 1 or 2 or 3: "))
    col = int(input("Enter column - 1 or 2 or 3: "))
    while(row>3 or col>3 or board[row-1][col-1] != '-'):
        print("Invalid input. Please enter again")
        row = int(input("Enter row - 1 or 2 or 3: "))
        col = int(input("Enter column - 1 or 2 or 3: "))
        
    board[row-1][col-1]=symbol
        
    
        
def won(symbol):
    return check_rows(symbol) or check_col(symbol) or check_dia(symbol)
    
def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if( board[r][c] == symbol):
                count += 1
        if count == 3:
            print(symbol,' won')
            return True
    return False

def check_col(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if( board[r][c] == symbol):
                count += 1
        if count == 3:
            print(symbol,' won')
            return True
    return False

def check_dia(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        print(symbol, 'won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        print(symbol, 'won')
        return True
    return False  
  
def play():
    for turn in range(9):
        if turn%2==0:
            print("X turn")
            place(p1s)
            if won(p1s):
                break
        else:
            print("O turn")
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)):
        print("Draw")
               
    
    
play()