# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:02:02 2018

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

packagelist = ['requests', 'lxml', 'urllib']
for x in packagelist:
    install_func(x)
    
import requests, os
from lxml import html
import urllib.request

def main():
    try:
        page = requests.get("https://www.xkcd.com") 
    except requests.exceptions.RequestException as e:
        print ("Can't reach the xkcd site")
        sleep(3)
        exit()
    
    # Parses xkcd page
    page = html.fromstring(page.content)
    print(page)
    image_src = "https:" + str(page.xpath(".//*[@id='comic']/img/@src")[0])
    print(image_src)
    
    # Scrape the comic name from the image url
    comic_name = image_src.split('/')[-1]
    comic_location = os.getcwd() + '/XKCD Comics/'
    
    # Checks if comic folder exists else creates it
    if not os.path.exists(comic_location):
        os.makedirs(comic_location)	
        
    # Creates the final comic location and dowloads the comic
    comic_location = comic_location + comic_name
    urllib.request.urlretrieve(image_src, comic_location)
    
    print("The file: " + comic_name + " has been downloaded")
    sleep(3)
if __name__ == "__main__":
    main()
