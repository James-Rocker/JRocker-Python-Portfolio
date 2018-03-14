# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:26:46 2018

@author: james
"""

import os, sys, time, imp, pip


package = 'pypiwin32'
def install_func(package):
    try:
        imp.find_module(package)
    except ImportError:
        print ('Error ' + package + ' library is missing ')
        var = input("Do you want to download and install the " + package + " library? (Note, this download and install might take a while) ")
        if var in ['no','n','No','N','NO']:
            print ('Error, '+ package + ' not installed, please install the library before attempting to run this program.')
            time.sleep(5)
            quit()
        else:
            pip.main(['install', package])
install_func(package)

import win32com.client

To = input("Who do you want to send the automated email to? \n")

try:
    os.startfile("outlook")
except:
    print("error")
    sys.exit()
        
    olMailItem = 0x0
    obj = win32com.client.Dispatch("Outlook.Application")
    newMail = obj.CreateItem(olMailItem)
    newMail.Subject = "Text Log Results -"
    newMail.Body = """Hello!
                    This is an automatically generated email, please do not reply. 
                    Please find attached a sample file with attached.
                        
                    Kind regards, 
                    Autobot"""
    newMail.To = To
    attachment1 = 'Send Outlook File'
    
    #newMail.Attachments.Add(Source=attachment1)
    newMail.display()
    newMail.Send()
    
    time.sleep(5)
    os.system("taskkill /im outlook.exe")