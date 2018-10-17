import random, time

lookup = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}

user_input = input('Choose Rock, Paper, Scissors')
user_input = user_input.lower()
print(f'You Chose {user_input}')
print('\n' * 5)
time.sleep(1)

computer_values = ['rock', 'paper', 'scissors']
computer_choice = random.choice(computer_values)
print(f'Computer Chooses {computer_choice}')
time.sleep(1)
print('\n' * 5)



for key in lookup.values():
    if user_input == key:
        if user_input == key and computer_choice == lookup[key]:
            print('Computer Won')
        elif user_input == computer_choice:
            print('You Have A Tie')
        else:
            print('user won')



