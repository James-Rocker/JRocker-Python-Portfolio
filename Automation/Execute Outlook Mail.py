# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:26:46 2018

@author: james
"""

import os
import sys
import time
import pip
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
    attachment1 = "Send Outlook File"

    # newMail.Attachments.Add(Source=attachment1)
    newMail.display()
    newMail.Send()

    time.sleep(5)
    os.system("taskkill /im outlook.exe")
