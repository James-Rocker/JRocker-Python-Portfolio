# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:02:27 2018

@author: James Rocker
"""
import time

wordinput = input("Please enter a word or list of words \n")
censorword = input("What word do you want to censor? \n")

def censor(text, word):
    text = text.split()
    count = len(word)
    new_text = ''
    for index in text:
        if index == word:
            new_text = new_text + " " + ("*" * count) 
        else: 
            new_text = new_text + " " + index 
    return new_text.lstrip(" ")

print(censor(wordinput, censorword))
time.sleep(5)
