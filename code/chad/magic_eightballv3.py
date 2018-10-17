import random

list_words = "It is certain,It is decidedly so,Without a doubt,Yes definitely,You may rely on it,As I see it,yes,Most likely,Outlook good,Yes,Signs point to yes,Reply hazy try again,Ask again later,Better not tell you now,Cannot predict now,Concentrate and ask again,Don't count on it,My reply is no,My sources say no,Outlook not so good,Very doubtful"
#In case I missed any spaces at the begining of the answers
answers = list_words.strip()
anwsers = list_words.split(",")

def run(answers):
    print('Welcome To The Magic Eightball Game!!!')
    question = input('Ask The Magic Eightball A Question? > ')
    print(f'The Magic Eight Ball Says "{random.choice(answers)}"')

run(anwsers)