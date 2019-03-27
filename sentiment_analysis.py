#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 19:43:10 2018

@author: manveet
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file='Facebook_data.xlsx'
xl=pd.ExcelFile(file) #Read From Excel
dfs = xl.parse(xl.sheet_names[0]) #Pasing the sl sheet to data frame
dfs=list(dfs['25/08/2018 19:49:00 + UTC']) #removes blank rows from the data frame
print(dfs)
sid = SentimentIntensityAnalyzer() 
str1='UTC'
for dat in dfs:
    a = dat.find(str1)
    if(a == -1):
        ss=sid.polarity_scores(dat)
        print(dat)
        for k in ss:
            print(k,ss[k])
        
        

