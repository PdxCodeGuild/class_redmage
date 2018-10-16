import random

question = input("Please type three adjectives seperated by a comma > ")
question = question.replace(' ', '')
question = question.split(",")


print(f'Portland is very {random.choice(question)}, it makes my stomach {random.choice(question)}, the food in Portland tastes like {random.choice(question)}  ')