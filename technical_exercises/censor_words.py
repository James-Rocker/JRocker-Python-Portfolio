# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:02:27 2018

@author: James Rocker
"""
import time

word_input = input("Please enter a word or list of words \n")
censor_word = input("What word do you want to censor? \n")


def censor(text: str, word: str) -> str:
    """
    Takes 2 args, including a piece of text with a large string and a single word.
    The function then censors that word in the text, replacing it with * symbols for each letter
    """
    text = text.split()
    count = len(word)
    new_text = ""
    for index in text:
        if index == word:
            new_text = new_text + " " + ("*" * count)
        else:
            new_text = new_text + " " + index
    return new_text.lstrip(" ")


print(censor(word_input, censor_word))
time.sleep(5)
