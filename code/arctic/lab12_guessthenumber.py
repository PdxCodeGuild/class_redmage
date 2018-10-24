#guessthenumber.py
import random
num1 = random.randint(1,9)
while True:
    user_guess = input(f"I'm thinking of a number from 1-9, What is the number? >")
    user_guess = int(user_guess)
    if user_guess == num1:
        print("Right On!")
        break
    elif user_guess <= 5:
        print("Go Lower!")
        break
    elif user_guess >= 6:
        print("Go Higher!")