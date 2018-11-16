# Version 1
# import random

# computer_guess = random.randint(1, 10)
# user_guess = int(input("Try to guess the number! It's anywhere between 1 and 10! > "))

# x = 1
# while x < 10:
#     if user_guess == computer_num:
#         break
#     else:
#         user_guess = int(input("Wrong! Guess again! > "))
#         x += + 1

# if user_guess == computer_num:
#     print(f"You guessed the correct number after {x} tries!")
# else:
#     print("You lose!")

# Version 2
# import random

# computer_num = random.randint(1, 10)
# print(computer_num) # Used for testing, delete for final.

# user_guess = int(input("Try to guess the number! It's anywhere between 1 and 10! > "))

# x = 1
# while x:
#     if user_guess == computer_num:
#         break
#     else:
#         user_guess = int(input("Wrong! Guess again! > "))
#         x += + 1

# if user_guess == computer_num:
#     print(f"You guessed the correct number after {x} tries!")
# else:
#     print("You lose!")

# Version 3
# import random

# computer_num = random.randint(1, 10)
# print(computer_num) # Used for testing, delete for final.

# user_guess = int(input("Try to guess the number! It's anywhere between 1 and 10! > "))

# x = 1
# while x:
#     if user_guess == computer_num:
#         break
#     if user_guess > computer_num:
#         user_guess = int(input("Wrong! Your guess is too high! Guess again! > "))
#         x += + 1
#     else:
#         user_guess = int(input("Wrong! Your guess is too low! Guess again! > "))
#         x += + 1

# if user_guess == computer_num:
#     print(f"You guessed the correct number after {x} tries!")
# else:
#     print("You lose!")

# Version 4
# import random
# computer_guess = random.randint(1, 10)
# attempts = 0
# previous_guess = 0
# end = False
# while end == False:
#     attempts += 1
#     user_guess = int(input("Try to guess the number! > "))
    
#     user_abs = abs(user_guess - computer_guess)
#     previous_abs = abs(previous_guess - computer_guess)


#     if user_guess == computer_guess:
#         print(f"You guessed the number after {attempts} tries!")
#         end = True
#         break

#     if user_abs < previous_abs:
#         print("You're getting warmer!")
#     else:
#         print("You're getting colder...")

#     previous_guess = user_guess

# Version 5
import random

end = False
while end == False:
    
    user_input = int(input("Choose a non-zero positive number, the computer will try to guess it! > "))
    value = list(range(user_input + 1))
    counter = 0

    while True:
        computer_guess = random.choice(value)
        print(computer_guess)
        counter += 1
        if computer_guess == user_input:
            break

    print(f"The computer guessed {user_input} after {counter} tries!")

    quit = ''
    while quit != 'y' and quit != 'n':
        quit = input("Would you like to try again? (y/n) > ").lower()
    
    if quit == 'n':
        print("\nThanks for playing!")
        end = True

    





