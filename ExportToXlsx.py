# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:21:58 2016

@author: James Rocker
"""
import imp
import pip

package = 'xlsxwriter'

def import_func(package):
    try:
        imp.find_module(package)
    except ImportError:
        print ('Error ' + package + ' library is missing ')
        var = input("Do you want to install the " + package + " library? ")
        if var in ['no','n','No','N','NO']:
            print ('Error, '+ package + ' not installed, please install the library before attempting to run this program')
        else:
            pip.main(['install', package])
import_func(package)

import xlsxwriter

workbook = xlsxwriter.Workbook('Example.xlsx')
worksheet = workbook.add_worksheet()

sample = (
['Text Log -', 12220],
['Total Errors in Text -', 561651],
['Format Errors -', 656],
['Limit Errors -', 51651],
['Change Errors -', 5484],
['Adress Error -', 5651561],
)
row = 0
col = 0

for item, cost in (sample):
    worksheet.write(row, col,     item)
    worksheet.write(row, col + 1, cost)
    row += 1

workbook.close()
