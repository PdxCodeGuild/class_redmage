import random as ran

print("""Welcome to the Ol' Rock, Paper, Scissors Saloon!\n\n
As a reminder, rock beats scissors, paper covers rock, and scissors cuts paper!\n\n
You'll be engaged in mortal kombat with our world-famous champion Glorath!\n\n
The safe word is 'no'\n
Game on!""")

g_choices = ["rock","paper","scissors"]

human_score = 0
computer_score = 0

p_start = input("Do you want to play a game? \n").lower()

while p_start != "no":

    user_choice = input("Do you plan to throw rock, paper, or scissors? \n").lower()
    computer_choice = ran.choice(g_choices)

    if user_choice == computer_choice:

        print("\nYou and Glorath tie!")
        p_start = input("Do you want to continue?\n").lower()
    
    elif user_choice == g_choices[0] and computer_choice == g_choices[1]:
        
        print("Glorath's paper covered your rock, oh no!\n")
        computer_score += 1
        print("Glorath's score: "+str(computer_score)+" vs. your score: "+str(human_score))
        p_start = input("Do you want to continue?\n").lower()
    
    elif user_choice == g_choices[1] and computer_choice == g_choices[2]:
        
        print("Glorath's scissors cut your paper, oh no!\n")
        computer_score += 1
        print("Glorath's score: "+str(computer_score)+" vs. your score: "+str(human_score))
        p_start = input("Do you want to continue?\n").lower()
    
    elif user_choice == g_choices [2] and computer_choice == g_choices[0]:
        
        print("Glorath's rock smashed your scissors, oh no!\n")
        computer_score += 1
        print("Glorath's score: "+str(computer_score)+" vs. your score: "+str(human_score))
        p_start = input("Do you want to continue?\n").lower()
    
    elif user_choice == g_choices[0] and computer_choice == g_choices[2]:
        
        print("You smashed Glorath's scissors, you're very lucky!\n")
        human_score += 1
        print("Glorath's score: "+str(computer_score)+" vs. your score: "+str(human_score))
        p_start = input("Do you want to continue?\n").lower()
    
    elif user_choice == g_choices[1] and computer_choice == g_choices[0]:
        
        print("You covered Glorath's rock, you're very lucky!\n")
        human_score += 1
        print("Glorath's score: "+str(computer_score)+" vs. your score: "+str(human_score))
        p_start = input("Do you want to continue?\n").lower()
    
    elif user_choice == g_choices[2] and computer_choice == g_choices[1]:
        
        print("You cut Glorath's paper, you're very lucky!\n")
        human_score += 1
        print("Glorath's score: "+str(computer_score)+" vs. your score: "+str(human_score))
        p_start = input("Do you want to continue?\n").lower()
    
    else:
        
        print("Please choose: rock, paper, or scissors\n")

print(f"Glorath scored {computer_score} while you scored {human_score}")
print("\nThanks for playing!")
    