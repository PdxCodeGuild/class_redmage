#rockpaperscissors.py
import random
name = input('What is your name? >')
print("Hi " + name + ',' + " Welcome to Rock, Paper, Scissors!")
hand_motion = ['rock', 'paper', 'scissors']
end = 'y'
while end == 'y':
    #this loop will start the game
    user_choice = input(f"What do you choose of {hand_motion}? >")
    # while user_choice not in comp_motion:
    #     user_choice = random.choice(comp_motion)
    comp_choice = random.choice(hand_motion)
    if comp_choice == 'rock':
        if user_choice == 'rock':
            print("Tie!")
        if user_choice == 'paper':
            print("You Win!")
        if user_choice == 'scissors':
            print("You Lost!")
    if comp_choice == 'paper':
        if user_choice == 'paper':
            print("Tie!")
        if user_choice == 'scissors':
            print("You Win!")
        if user_choice == 'rock':
            print("You Lost!")
    if comp_choice == 'scissors':
        if user_choice == 'scissors':
            print("Tie!")
        if user_choice == 'rock':
            print("You Win!")
        if user_choice == 'paper':
            print("You Lost!")
    while end != 'y' or  end != 'n':
        # This loop will ensure you choose y or n
        end = input("Would you like to continue? > (y/n)")
        print("You must choose either y or n to continue!") 
        if end == 'y':
            break
        if end == 'n':
            print("Thank you" + ',' + "goodbye " + name + '!' )
            break
    

        #     while end != 'y' or  != 'n':
#         end = input("You must choose either y or n to continue > ")