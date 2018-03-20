# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 15:52:23 2016

@author: James Rocker
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

packagelist = ['requests', 'json']
for x in packagelist:
    install_func(x)

import requests, json

payload = {'inUserName': '', 'inUserPass': ''}
url = ''
requests.post(url, data=payload)

url = ''
r = requests.get(url)

#status code 200 is what we want, this means that the HTTP Status code is working as intended

header = {'': ''}
t = requests.get(url, headers=True)
newDictionary=json.loads(t)
