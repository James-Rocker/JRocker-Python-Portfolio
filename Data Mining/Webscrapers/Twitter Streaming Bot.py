# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 10:20:09 2018

@author: james
"""

import imp, pip 
from time import sleep

def install_func(package):
    try:
        imp.find_module(package)
    except ImportError:
        print ('Error ' + package + ' library is missing ')
        var = input("Do you want to download and install the " + package + " library? (Note, this download and install might take a while) ")
        if var in ['no','n','No','N','NO']:
            print ('Error, '+ package + ' not installed, please install the library before attempting to run this program.')
            sleep(5)
            quit()
        else:
            pip.main(['install', package])

packagelist = ['tweepy']
for x in packagelist:
    install_func(x)

import tweepy    
from tweepy import OAuthHandler

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
 
api = tweepy.API(auth)    
    
from tweepy import Stream
from tweepy.streaming import StreamListener
 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('C:\Users\\' + '\Documents\Python Scripts\\python.json', 'a') as f:  #change location here
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())

#change the keyword here
twitter_stream.filter(track=['#FridayFeeling'])
