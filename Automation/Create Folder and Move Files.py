# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:22:00 2018

@author: james
"""

import datetime

#Create folder, move files
yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-number)
Today = datetime.date.fromordinal(datetime.date.today().toordinal())

TextDoc = ("Text Document" + yesterday.strftime('%d-%b-%Y') + ".txt")
CSVDoc = ("CSV Document" + Today.strftime('%d-%m-%Y') + ".csv")

f = ("C:\Users\\" + user + "\Documents\Log Files\\" + Today.strftime('%d-%b-%Y'))
if not os.path.exists(f):
    os.makedirs(f)
try:
    shutil.move("C:\Users\\" + user + "\Downloads\\" + TextDoc, f)
except:
    os.remove("C:\Users\\" + user + "\Downloads\\" + TextDoc)
    pass
try:
    shutil.move("C:\Users\\" + user + "\Downloads\\" + CSVDoc, f)
except:
    os.remove("C:\Users\\" + user + "\Downloads\\" + CSVDoc)
    pass
