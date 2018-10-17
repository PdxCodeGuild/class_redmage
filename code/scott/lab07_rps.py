#lab7_rps.py

# preparing for random choices
import random

# supplying weapons
weapon_options = ["rock", "paper", "scissors"]

# computer choosing a weapon
comp_weapon = random.choice(weapon_options)

# getting user input
weapon_choice = ""
while weapon_choice not in weapon_options:
    weapon_choice = input("Choose your weapon! rock, paper, or scissors>")

# fight! - with confirmation loop and break
play_again = "y"
while play_again == "y":
    if weapon_choice == comp_weapon:
        print ("It's a tie!")

    elif weapon_choice == "rock":
        if comp_weapon == "paper":
            print(f"You lose! The computer chose {comp_weapon}")
        elif comp_weapon == "scissors":
            print(f"You win! The computer chose {comp_weapon}.")

    elif weapon_choice == "paper":
        if comp_weapon == "scissors":
            print(f"You lose! The computer chose {comp_weapon}")
        elif comp_weapon == "rock":
            print(f"You win! The computer chose {comp_weapon}.")
    

    elif weapon_choice == "scissors":
        if comp_weapon == "rock":
            print(f"You lose! The computer chose {comp_weapon}")
        elif comp_weapon == "paper":
            print(f"You win! The computer chose {comp_weapon}.")

# checking if the user wants to play again
    play_again = input("Would you like to play again (y/n)?")
    if play_again == "n":
        break