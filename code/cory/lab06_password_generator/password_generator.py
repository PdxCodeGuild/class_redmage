# Version 3
import random
import string

lower_list = list(string.ascii_lowercase)
upper_list = list(string.ascii_uppercase)
digit_list = list(string.digits)
punct_list = list(string.punctuation)

while True:
    lower_input = int(input("How many lowercase letters would you like? > "))
    upper_input = int(input("How many uppercase letters would you like? > "))
    digit_input = int(input("How many digits would you like? > "))
    punct_input = int(input("How many punctuations would you like? > "))

    out_string = ''
    for x in range(lower_input):
        out_string += random.choice(lower_list)
    for x in range(upper_input):
        out_string += random.choice(upper_list)
    for x in range(digit_input):
        out_string += random.choice(digit_list)
    for x in range(punct_input):
        out_string += random.choice(punct_list)

    out_string = list(out_string)
    random.shuffle(out_string)
    result = ''.join(out_string)
    print(result)