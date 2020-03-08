# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:22:00 2018

@author: james
"""

import datetime
import os
from getpass import getuser
import shutil
user_name = getuser()


# Create folder, move files
yesterday = datetime.date.fromordinal(datetime.date.today().toordinal()-1)
Today = datetime.date.fromordinal(datetime.date.today().toordinal())

TextDoc = ("Text Document" + yesterday.strftime('%d-%b-%Y') + ".txt")
CSVDoc = ("CSV Document" + Today.strftime('%d-%m-%Y') + ".csv")

f = (r"C:\Users\\" + user_name + r"\Documents\Log Files\\" + Today.strftime('%d-%b-%Y'))
if not os.path.exists(f):
    os.makedirs(f)
try:
    shutil.move(r"C:\Users\\" + user_name + r"\Downloads\\" + TextDoc, f)
except:
    os.remove(r"C:\Users\\" + user_name + r"\Downloads\\" + TextDoc)
    pass
try:
    shutil.move(r"C:\Users\\" + user_name + r"\Downloads\\" + CSVDoc, f)
except:
    os.remove(r"C:\Users\\" + user_name + r"\Downloads\\" + CSVDoc)
    pass
