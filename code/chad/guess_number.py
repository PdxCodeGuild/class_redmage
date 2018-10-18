import random
number_guess = random.randint(1,10)
x = 0
while x < 11:
    print (number_guess)
    user_guess = int(input('Guess a number between 1 and 10, you will have 10 tries: > '))
    if number_guess == user_guess:
        print('You Won The Game!!')
        break
    else:
        x += 1
        print('you got here')
        continue
  