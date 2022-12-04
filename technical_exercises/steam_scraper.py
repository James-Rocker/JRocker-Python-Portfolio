# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 12:49:56 2017

@author: James Rocker
"""
import requests
from bs4 import BeautifulSoup
import re

items_to_find_reviews_for = ["Half Life 2"]
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}
for item in items_to_find_reviews_for:
    # Search string on steam, get first result
    resp = requests.get(f"http://store.steampowered.com/search/?term={item}", headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    review_objects = soup.find_all('div', {'class': 'search_reviewscore'})
    reviews = re.findall("(\d+%)|(\d+,\d+)", str(review_objects[0]))
    review_score, _ = reviews[0]
    _, reviewers = reviews[1]
    print("Current review score:", review_score, "number of reviewers", reviewers)
