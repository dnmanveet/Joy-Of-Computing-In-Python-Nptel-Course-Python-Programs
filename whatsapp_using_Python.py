#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 20:37:49 2018

@author: manveet
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
driver.get("https://web.whatsapp.com")
wait = WebDriverWait(driver,10000)
target = '"Divya IT"' #Enete rv your friend's name

string = "Message sending HI!!" #type the msg u want to send
x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
if(wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))):
    print("found")
    target.click()
    input_box=driver.find_element_by_class_name('_1Plpp')
    for i in range(50):
        input_box.send_keys(string+Keys.ENTER)
    




