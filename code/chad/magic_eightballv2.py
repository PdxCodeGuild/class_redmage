import random

list_words = "It is certain,It is decidedly so, Without a doubt,Yes definitely,You may rely on it,As I see it, yes,Most likely,Outlook good,Yes,Signs point to yes,Reply hazy try again,Ask again later,Better not tell you now,Cannot predict now,Concentrate and ask again,Don't count on it,My reply is no,My sources say no,Outlook not so good,Very doubtful"
anwsers = list_words.split(",")

while True:
    print('Welcome To The Magic Eightball Game!!!')
    question = input('Ask The Magic Eightball A Question? > ')
    print(f'The Magic Eight Ball Says \n"{random.choice(anwsers)}"" \nIs The Answer To Your Question of \n"{question}""')
    another_question = int(input('Would You like To Ask The Eight Ball Another Questions? Type 1.) for yes and 2.) for no'))
    if another_question == 2:
        break
    elif another_question > 2:
        print('You Typed An Invalid Argument')
        break
