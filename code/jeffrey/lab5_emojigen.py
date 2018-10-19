import random

le = [":",";"]
ln = [",",".",">","<","^","`","\'"]
lm = ["(",")","@","#","3","$","%","?","{","}","|"]

i = 0

user_in = int(input("How many emoticons do you want to generate? "))

while i < user_in:
    print(random.choice(le)+random.choice(ln)+random.choice(lm))
    i += 1