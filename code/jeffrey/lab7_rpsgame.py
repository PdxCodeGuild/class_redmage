import random as ran

g_choices = ["rock","paper","scissors"]

p_start = input("Do you want to play a game? ")

while p_start != "no":
    user_choice = input("Do you plan to throw rock, paper, or scissors? ")
    computer_choice = ran.choice(g_choices)
    if user_choice == computer_choice:
        print("tie!") 