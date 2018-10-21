#lab7_rps.py

# preparing for random choices
import random

# supplying weapons
weapon_options = ["rock", "paper", "scissors"]
weapon_dict = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

#priming
weapon_choice = ""
play_again = "y"

# fight! - with confirmation loop and break
while play_again == "y":
    # computer choosing a weapon
    comp_weapon = random.choice(weapon_options)
    # user choosing a weapon
    weapon_choice = input("Choose your weapon! rock, paper, or scissors>")
    # making sure they chose a valid weapon
    if weapon_choice not in weapon_options:
        continue
    # checking who won
    if comp_weapon == weapon_choice:
        result = "tied"
    elif comp_weapon == weapon_dict[weapon_choice]:
        result = "lost"  
    elif comp_weapon != weapon_dict[weapon_choice]:
        result = "won"
    # printing result
    print(f"You {result}! Computer chose {comp_weapon}!")
    # checking if the user wants to play again
    play_again = input("Would you like to play again (y/n)?")
    if play_again == "n":
        break
