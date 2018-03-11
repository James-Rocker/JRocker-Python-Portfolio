# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:53:10 2018

@author: James
"""

import random, time

reroll = True
valid_dice = [2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 24, 30, 34, 48, 50, 60, 100, 120]
run_true = ['yes','y','yeah']
run_false = ['no','n','nope']
print("Welcome to the dice roll application")
time.sleep(1)
roll_confirm = input("Would you like to roll a dice? ")

if roll_confirm in run_true:
    time.sleep(1)
    while reroll == True:
        dice_roll = input("How many times do you want to roll a dice? ")
        def dice_validation():
            try:
                int(dice_roll)
                return True
            except:
                print("Please enter a number for the number of rolls")
        die_type = input("What kind of die do you want to roll? D")
        def dice_type():
            try:
                int(die_type)
                if int(die_type) in valid_dice:
                   return True
                elif int(die_type) not in valid_dice: 
                   print("This is not a valid dice")
            except ValueError:
                print("Please enter a number for the dice type input")
        def die():
            die = list(range(1, int(die_type) + 1))
            return(die)
        if dice_validation() == True and dice_type() == True:
            for i in range(int(dice_roll)):
                print(random.choice(die()))
        time.sleep(3)
        rerun = input("Do you want another roll? ").lower()
        if rerun in run_true:
            reroll = True
            print("Okay, restarting the program.")
            time.sleep(3)
        elif rerun in run_false:
            reroll = False
            print("Okay, thank you for using the dice program.")
            time.sleep(3)
        else:
            reroll = False
            print("Sorry, I don't understand what you said. The dice program is shutting down.")
            time.sleep(3)
else:
    print("Okay, have a nice day.")
    time.sleep(5)
    