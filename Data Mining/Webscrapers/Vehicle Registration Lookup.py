# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:15:17 2017

@author: James Rocker
"""
import urllib
import urllib2
import os
import xlsxwriter
import getpass
from bs4 import BeautifulSoup
import datetime
from csv import DictReader
from mechanize import ParseResponse, urlopen

now = datetime.datetime.now()
now = now.strftime("%d-%b-%Y")
user = getpass.getuser()

filename = ''
workbook = xlsxwriter.Workbook(filename + ' Output.xlsx')
sheet1 = workbook.add_worksheet("Output")

sheet1.write('A1', "Registration")
sheet1.write('B1', "Make")
sheet1.write('C1', "Model")
sheet1.write('D1', "Depot")
sheet1.write('E1', "Colour")
sheet1.write('F1', "Cylinder Capacity")
sheet1.write('G1', "Fuel Type")
sheet1.write('H1', "Transmission")

import_file = filename + ".csv"
import_location = "C:\Users\\"+ user + "\Documents\Importing Data\Reg Lookup Folder\\"
import_file = os.path.join(import_location,import_file)

with open(import_file) as f:
    o1 = [row["Vehicle_Registration"] for row in DictReader(f)]

reglist = o1
for reg,e in enumerate(reglist):
    sheet1.write(1 + reg,0,e)

row = 1
for reg in reglist:
    req = urllib2.Request('https://www.vehiclecheck.co.uk/', urllib.urlencode({'vrm' : reg}))
    response = urllib2.urlopen(req)
    the_page = response.read()
    soup = BeautifulSoup(the_page,"lxml")

    VehicleModel = soup.find('input',{'id':'VehicleModel'}).get('value')
    VehicleMake = soup.find('input',{'id':'VehicleMake'}).get('value')
    try:
        VehicleColour = soup.find('input',{'id':'VehicleColour'}).get('value')
    except:
        pass
    RegistrationYear = soup.find('input',{'id':'RegistrationYear'}).get('value')

    response = urlopen('https://www.check-mot.service.gov.uk/')
    forms = ParseResponse(response, backwards_compat=False)
    form = forms[0]
    form['registration'] = reg
    form['manufacturer'] = VehicleMake

    soup = BeautifulSoup(urlopen(form.click()).read(),"lxml")
    try:
        fueltype = soup.find('strong',{'id':'FuelTypeShown'}).string
    except:
        pass
    try:
        cylindercapacity = str(soup.find('li',{'id':'CylinderCapacity'}).text.replace("Cylinder capacity (cc) ","").replace("\n","")).replace("cc","")
    except:
        pass

    sheet1.write(row,1,VehicleMake)
    sheet1.write(row,2,VehicleModel)
    sheet1.write(row,3,'')
    sheet1.write(row,4,VehicleColour)
    try:
        sheet1.write(row,5,cylindercapacity)
    except:
        pass
    try:
        sheet1.write(row,6,str(fueltype.replace("DIESEL","D")))
    except:
        pass
    sheet1.write(row,7,'M')
    row += 1

workbook.close()
