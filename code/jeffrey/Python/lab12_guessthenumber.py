# Version 1 and 3

import random

i = 0
c = 11
b = 1

computer_pick = int(random.choice(range(10)))

user_input  = int(input(f"Guess a number within 0-10, [{c - b} guesses remain]: "))

print(computer_pick)

while user_input != computer_pick and i < 9:
    b += 1
    user_input  = int(input(f"Guess a number within 0-10, [{c - b} guesses remain]: "))
    i += 1
    if user_input < computer_pick:
        print("Your guess was too low!")
    elif user_input > computer_pick:
        print("Your guess was too high!")
    elif user_input == computer_pick:
        print("You win!")
    else:
        print("You lose!")
