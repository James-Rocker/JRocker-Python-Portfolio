# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 09:51:22 2017

@author: James
"""

input_from_user = input("Enter the numbers to remove odds from (e.g. 2 3 4): ")
string_list = input_from_user.split()
int_list = [int(a) for a in string_list]


def remove_odds_from_list(number_list: list):
    """
    Takes a list of numbers and removes any odds and returns the new list
    """
    list_of_numbers = []
    for number in number_list:
        if number % 2 == 0:
            list_of_numbers.append(number)
    return list_of_numbers


output = remove_odds_from_list(int_list)
print(output)
