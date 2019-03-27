#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 13:38:23 2018

@author: manveet
"""
# =============================================================================
# import csv
# with open('route.csv','r+') as f:
#     reader = csv.reader(f)
#     
#     for row in reader:
#         lat = row[0]
#         long = row[1]
#         print(lat) 
#         print(long)
#         print(float(lat)+float(long))
#     
# =============================================================================

import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(28.689169, 77.324448, 17)

gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"

with open('route.csv', 'r') as f:
    reader = csv.reader(f)
    k = 0
    
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        if(k == 0):
            gmap.marker(lat,long, 'yellow')
            k = 1
        else:
            gmap.marker(lat,long, 'blue')
            
gmap.marker(lat,long, 'red')

gmap.draw("mymap.html")

