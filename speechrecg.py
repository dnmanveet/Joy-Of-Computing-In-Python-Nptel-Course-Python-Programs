#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 00:25:54 2018

@author: manveet
"""

import speech_recognition as sr
AUDIO_FILE=("answer.wav")
#use audio file as source

r=sr.Recognizer() #intialize the recogniser
print('Heloo')
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source) 
#reads the audio file
    
try:
    print('hiii')
    print("audio file contains "+r.recognize_google(audio))
except sr.UnknownValueError :
    print("Google Speech Recognition could not understand audio")
except sr.RequestError :
    print("could'nt get the result from Google Speech Recognition")
