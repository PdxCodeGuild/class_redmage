import random
number_guess = random.randint(1,10)
times_tried = 0

istrue = True
while istrue:
    user_guess = int(input('Guess a number between 1 and 10, you will have 10 tries: > '))
    if number_guess == user_guess:
        print('You Won The Game!!')
        istrue = False
    else:
        times_tried += 1
        print(f'You Have Tried {times_tried} Times')
        if user_guess > number_guess:
            print('You Are Too High')
        if user_guess < number_guess:
            print('You Are Too Low')
        continue
  