#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:23:26 2018

@author: manveet
"""
#The commneted code also works but for different one
# =============================================================================
# from PIL import Image
# 
#  #opening the image
# img = Image.open('/home/manveet/Python/tobe.jpg')
# 
# #transposing
# trasposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# 
# #save it to file in ahuman understandable format
# 
# trasposed_img.save('Afterusingpython.jpg' )
# =============================================================================

#Image enhancement CLAHE
import cv2
#read the image
img = cv2.imread('tobe.jpeg')
#Preparation for CLAHE

clahe = cv2.createCLAHE()

#Convert to gray scale image

gray_img = cv2.cvtColor(img, cv2.COLR_BGR2GRAY)

#Apply enchancement

enh_img = clahe.apply(gray_img)

#save it to a file
cv2.imwrite('enhance.jpeg', enh_img)
print('Done enhancing')

