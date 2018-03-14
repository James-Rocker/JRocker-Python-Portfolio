# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 11:24:03 2018

@author: james
"""

import datetime, 

yesterday = date.today() - timedelta(number)

"""Search Text Logs""" 
workbook = xlsxwriter.Workbook(yesterday.strftime('%d-%b-%Y') + " Analysis.xlsx")
worksheet = workbook.add_worksheet()

"""Analyse of text file here"""
try:
    os.chdir("C:\Users\\" + user + "\Documents\Log Files\\"+yesterday.strftime ('%d-%b-%Y'))
    filename="VTSDataImport"+ yesterday.strftime ('%d-%b-%Y')+".txt"
    raised = len(re.findall('Filter test is true so creating incident with available details', file(filename).read()))
    filtered = len(re.findall('Filter test is fail so considering event as false', file(filename).read()))
    inactive = len(re.findall(' is inactive. So discarding all the events with this device id', file(filename).read()))
    accelerometer = len(re.findall('Accelerometer data not available so considering event as false', file(filename).read()))
    
    ITerror1 = len(re.findall('', file(filename).read())) 

    """Change the output to a directory"""
    output1 = (
    ["Intelligent Telematic devices",''],
    ["Sent to DriveGuard", raised + filtered],
    ["Raised in DriveGuard", raised],
    ["Filtered events", filtered],
    ["Filtered due to missing accelerometer data", accelerometer],
    ["Events from inactive devices sent to DriveGuard", inactive],
    )
    row = 0
    col = 0    
    for item, cost in (output1):
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost)
        row += 1
    output1percent = 100-round((raised/filtered)*100,2)
    row = 6
    col = 0
    percent =  workbook.add_format({'num_format': '0.00"%"'})  
    worksheet.write(row, col, "Filtered Percentage")
    worksheet.write(row, col + 1, output1percent, percent)
    
    worksheet2 = workbook.add_worksheet()
    erroroutput = (
        ["Intelligent Telematics Errors",''],
        ["Road Speed Limit Errors", ITerror1],
        ["Verlocity Change Errors",ITerror2],
        ["Date Time Formating Errors",ITerror3],
        ["GPS Errors",ITerror4],
        ["Get New Event Errors",ITerror5],
        ["Location Test Errors",ITerror6],
        ["Address Errors",ITerror7],
        ["Outstanding API Errors", ITerror]
    )
    row = 0
    col = 0
    for item, cost in (erroroutput):
        worksheet2.write(row, col, item)
        worksheet2.write(row, col + 1, cost)
        row += 1    
except:
    pass