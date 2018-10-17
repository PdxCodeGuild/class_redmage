import random, time

#Word List From PDX Code Guild
list_words = "It is certain,It is decidedly so,Without a doubt,Yes definitely,You may rely on it,As I see it,yes,Most likely,Outlook good,Yes,Signs point to yes,Reply hazy try again,Ask again later,Better not tell you now,Cannot predict now,Concentrate and ask again,Don't count on it,My reply is no,My sources say no,Outlook not so good,Very doubtful"

#In case I missed any spaces at the begining of the answers
answers = list_words.strip()

# Split the string into a list by comma
anwsers = list_words.split(",")

def run(answers):
    print(f'The Magic Eight Ball Says "{random.choice(answers)}"')
    time.sleep(2)
    print('\n' * 200)

while True:
    print('Welcome To The Magic Eightball Game!!!')
    question = input('Ask The Magic Eightball A Question? > ')
    run(anwsers)
    another_question = int(input('Would You like To Ask The Eight Ball Another Questions? Type 1.) for yes and 2.) for no'))
    if another_question == 2:
        break
    elif another_question == 1:
        print('\n' * 200)
        continue
    else:
        print("You Selected an Invalid Character. Quitting Program Anyways")
        break