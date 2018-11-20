import random
user_guess = int(input('Guess a number between 1 and 10, you will have 10 tries: > '))
times_tried = 0

istrue = True
while istrue:
    computer_guess = random.randint(1,10)
    if computer_guess == user_guess:
        print('The Computer The Game!!')
        istrue = False
    else:
        times_tried += 1
        print(f'The computer Tried {times_tried} Times')
        if user_guess > computer_guess:
            print('Computer Is Too High')
        if user_guess < computer_guess:
            print('Computer is Too Low')
        continue
  