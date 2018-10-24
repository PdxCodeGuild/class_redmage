#8ball.py
import random
name = input("What is your name? >")
location = input("Where are you from? >")
print(name + " from " + location  + ',' + ' Welcome to 8-Ball.')
question = input("What is your question? >")
#ask 8ball "Will I win the lottery?"
answer_list = ['yes', 'no', 'ask me later', 'go away!', 'stop asking me stupid questions!', 'I am not sure if I can answer that...', 'sure, why not' , 'HELL NO!' , 'HELL YEAH']
print(random.choice(answer_list) + ', ' + name)
print ('\n')