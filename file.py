#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 23:38:28 2018

@author: manveet
"""

with open("file1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()