# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 10:29:16 2017

@author: James Rocker
"""

from __future__ import division
import os, time, getpass, win32com.client, sys, re, xlsxwriter, datetime, shutil, schedule
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import date, timedelta

def Autobot(self):
    user = getpass.getuser()
    yesterday = date.today() - timedelta(number)
    
    chromedriver = "C:\Users\\" + user + "\Documents\Log Files\Chromedriver\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    browser = webdriver.Chrome(chromedriver)
    browser.get("")
    
    emailElem = browser.find_element_by_id("txtUserName")
    emailElem.send_keys("")
    passwordElem = browser.find_element_by_id("txtPassword")
    passwordElem.send_keys("")
    
    htmlElem = browser.find_element_by_id('btnLogin')
    htmlElem.send_keys(Keys.ENTER)
    
    linkElem = browser.find_element_by_link_text('SERVICE LOGS')
    type(linkElem)
    linkElem.click() 
    #selects the Intelligent Telematics Logs from yesterday
    try:
        dropdown = browser.find_element_by_id("MainContent_ddlServiceName")    
        select = Select(dropdown)
        select.select_by_value("5")
        menudate = browser.find_element_by_id("MainContent_txtDate")
        menudate.send_keys(yesterday.strftime('%d/%m/%Y'))
        download = browser.find_element_by_name("ctl00$MainContent$btnDownload")
        download.send_keys(Keys.ENTER)
    except: 
        pass
    #selects the CTrack Logs from yesterday
    try:
        dropdown = browser.find_element_by_id("MainContent_ddlServiceName")    
        select = Select(dropdown)
        select.select_by_value("4")
        download = browser.find_element_by_name("ctl00$MainContent$btnDownload")
        download.send_keys(Keys.ENTER)
    except:
        pass
    #selects the email Logs from yesterday
    try:
        dropdown = browser.find_element_by_id("MainContent_ddlServiceName")    
        select = Select(dropdown)
        select.select_by_value("1")    
        download = browser.find_element_by_name("ctl00$MainContent$btnDownload")
        download.send_keys(Keys.ENTER)
    except:
        pass
    #selects the video logs from yesterday
    try:   
        dropdown = browser.find_element_by_id("MainContent_ddlServiceName")    
        select = Select(dropdown)
        select.select_by_value("2")   
        download = browser.find_element_by_name("ctl00$MainContent$btnDownload")
        download.send_keys(Keys.ENTER)
    except: 
        pass
    #selects the Azure logs from yesterday
    try:
        dropdown = browser.find_element_by_id("MainContent_ddlServiceName")    
        select = Select(dropdown)
        select.select_by_value("3")
        download = browser.find_element_by_name("ctl00$MainContent$btnDownload")
        download.send_keys(Keys.ENTER)
    except: 
        pass
    #Download device report
    try:
        htmlElem = browser.find_element_by_link_text('DEVICE REPORT')
        htmlElem.send_keys(Keys.ENTER) 
        htmlElem = browser.find_element_by_id('MainContent_btExportToCSV')
        htmlElem.send_keys(Keys.ENTER)
    except: 
        pass
    time.sleep(60)
    browser.close()
    os.system("taskkill /im Chromedriver.exe")

Autobot()