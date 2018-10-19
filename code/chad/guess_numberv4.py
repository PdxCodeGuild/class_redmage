import random
number_guess = random.randint(1,10)
times_tried = 0
previous_guess = 0


while True:
    user_guess = int(input('Guess a number between 1 and 10, you will have 10 tries: > '))
    previous_closer = abs(previous_guess-number_guess)
    if number_guess == user_guess:
        print('You Won The Game!!')
        break
        
    elif times_tried == 0:
        times_tried += 1
        print(f'You Have Tried {times_tried} Times')

        continue
    else:
        previous_guess = user_guess     
        times_tried += 1
        print(f'You Have Tried {times_tried} Times')
        if (abs(user_guess-number_guess)) >= previous_closer:
            print('You Were Closer The Previous Time You Played')
        else:
            print('You were Closer This Time Than Last time')
        
        continue
  