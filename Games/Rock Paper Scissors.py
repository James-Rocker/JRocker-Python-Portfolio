# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 06:33:38 2018

@author: James
"""

import sys, random
from time import sleep

wins  = 0
loses = 0

RPS = ['Rock','Paper','Scissors']
confirm = ['Yes', 'Y', 'Okay']

def game(wins, loses):
    Player_RPS = input("Please select either rock, paper or scissors: ")
    player_clean = Player_RPS.capitalize()
    
    def validate(a):
        if Player_RPS.capitalize() in RPS:
            return True
        else: 
            return False
    
    RPS_CPU = (random.choice(RPS))
    
    if validate(player_clean) == False:
        sleep(1)
        sys.exit("Hey! You should have chosen either rock, paper or scissors.")
        
    def win_condition(a, b):
        if (a,b) in (("Rock", "Scissors"), ("Paper", "Scissors"), ("Scissors", "Rock")): 
            return True
    
    def choices():
        sleep(1)
        print("Player chooses - " + player_clean)
        sleep(1)
        print("CPU chooses - " + RPS_CPU)
    
    choices()
        
    if RPS_CPU != player_clean:
        if win_condition(player_clean, RPS_CPU):
            sleep(2)
            print ("Player wins!")
            wins += 1
            score(wins, loses)
        else:
            sleep(2)
            print ("CPU wins")
            loses += 1
            score(wins, loses)
    else:
        sleep(2)
        print("Tie!")
        score(wins, loses)

def score(wins, loses):
    print ("Wins: " + str(wins) + " Loses: " + str(loses))
    print ("Do you want to play again?")
    user_input = input()
    if user_input.capitalize() in confirm:
        game(wins, loses)
    else:
        print("Final score is - " + "Wins: " + str(wins) + " Loses: " + str(loses))
        print("Thanks for playing!")
        sleep(3)

print("Would you like to play, rock, paper, scissors?")
user_input = input()
if user_input.capitalize() in confirm:
    game(wins, loses)
else:
    print("Okay, have a nice day")