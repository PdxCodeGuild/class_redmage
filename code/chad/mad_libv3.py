import random

while True:
    question = input("Please type three adjectives seperated by a comma > ")
    question = question.strip()
    print(question)
    question = question.split(",")
    print(f'Portland is very {random.choice(question)}, it makes my stomach {random.choice(question)}, the food in Portland tastes like {random.choice(question)}  ')
    ask = int(input('Do you want to play again press the number 1.) for "yes" and 2.) > '))
    if ask == 2:
        break
    elif ask >= 2:
        print('You Typed A Number That is Out Of Range')
        break
    