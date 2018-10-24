# Version 2
import random

end = False
while end == False:
    question = input("\nWhat question do you have for the magic 8 ball? > ")

    ball_ans = [
        'It is certain', 'It is decidedly so', 'Without a doubt', 
        'Ask again later', 'Don\'t count on it', 'My reply is no', 
        'Very doubtful' 
        ]

    print(f"\nYou asked the magic 8 ball \"{question}\". The ball has answered... {random.choice(ball_ans)}.\n\n\n")

    end = input("Would you like to ask another question? (y/n) > ")
    end.lower()
    if end == 'n':
        print("\nThe 8 ball bids you farewell...")
        end = True
        break
    while end != 'y' and end != 'n':
        end = input("You must choose either 'y' or 'n' to continue. Would you like to ask another question? (y/n) > ")
        end = end.lower()
        if end == 'n':
            print("\nThe 8 ball bids you farewell...")
            end = True
            break
