# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 07:48:08 2018

@author: James
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
packagelist = ['webbrowser', 'pyperclip', 'requests', 'bs4']
for x in packagelist:
    install_func(x)

import webbrowser, sys, pyperclip, requests
from bs4 import BeautifulSoup as bs

def main():
    tabs_to_open = input("How many links do you want to open? ")
    try:
        tabs_to_open = int(tabs_to_open)
    except:
        print("Number of tabs must be an integer. Closing the program")
        sleep(3)
        sys.quit()
    if len(sys.argv) > 1:
        keyword = ' '.join(sys.argv[1:])
    else:
        """ if no keyword is entered, the script would search for the keyword
        copied in the clipboard """
        try:
            keyword = input("What do you want to search? ")
        except:
            keyword = pyperclip.paste()
    res=requests.get('http://google.com/search?q='+	keyword)
    res.raise_for_status()
    soup = bs(res.text)
    linkElems = soup.select('.r a')
    numOpen = min(tabs_to_open, len(linkElems)) #opens the first 5 results

    for i in range(numOpen):
        webbrowser.open('http://google.com' + linkElems[i].get('href'))
    print("I hope one of the" + keyword + " tabs shows what you are looking for")
    sleep(3)
    sys.exit

if __name__ == '__main__':
    main()
