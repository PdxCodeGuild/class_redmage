# Version 2

import random

guess_range = range(10)

i = 0

computer_pick = (random.randint(1,9))

# user_input  = int(input(f"Guess a number within 0-10: "))

# print(computer_pick)

while True:
    user_input  = (input(f"Guess a number between 0-10: "))
    i += 1
    if int(user_input) < computer_pick:
        print("Your guess was too low!")
    elif int(user_input) > computer_pick:
        print("Your guess was too high!")
    elif int(user_input) not in guess_range:
        print("Please guess a number between 0-10.")
    elif int(user_input) == computer_pick:
        break



if int(user_input) == computer_pick:
    print(f"You guessed it in {i} guesses!")
# else:
#     print("You were unable to guess the number the computer chose!")