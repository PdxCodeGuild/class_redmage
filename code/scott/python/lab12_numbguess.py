# lab12_numbguess.py

import random

user_guess = "0"
guess_count = 0
rand_num = random.randint(1, 10)
prev_guesses = []

while True:
    user_guess = input("I'm thinking of a number between 1 and 10. Guess!> ")

    if int(user_guess) < rand_num:
        print("Too low! Guess again!")
        if guess_count > 0:
            if abs(int(user_guess) - rand_num) > abs(int(prev_guesses[-1]) - rand_num):
                print(f"You were closer with {prev_guesses[-1]}")
            elif prev_guesses[-1] < user_guess:
                print("Closer...")
        prev_guesses.append(user_guess)
        guess_count += 1

    elif int(user_guess) > rand_num:
        print("Too high! Guess again!")
        if guess_count > 0:
            if abs(int(user_guess) - rand_num) > abs(int(prev_guesses[-1]) - rand_num):
                print(f"You were closer with {prev_guesses[-1]}")
            elif prev_guesses[-1] > user_guess:
                print("Closer...")
        prev_guesses.append(user_guess)
        guess_count += 1

    elif int(user_guess) == rand_num:
        print("You got it!")
        guess_count += 1
        print(f"It took you {guess_count} tries to guess the number!")
        break