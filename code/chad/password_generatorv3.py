import random, string

do_another_password = True
while do_another_password:
    how_lower = int(input('How many lower characters? > '))
    how_upper = int(input('How many upper characters? > '))
    how_numbers = int(input('How many numbers? > '))
    special_char = int(input('How many special characters? > '))
    how_lower = random.choices(string.ascii_lowercase, k = how_lower)
    how_upper = random.choices(string.ascii_uppercase, k = how_upper)
    how_numbers = random.choices(string.digits, k = how_numbers)
    special_char = random.choices(string.punctuation, k = special_char)
    password = how_lower + how_upper + how_numbers + special_char 
    password = random.sample(password, k=(len(password)))
    password = "".join(password)
    print(f'Your Password Is {password}')
    another = int(input('Would You Like To Generate Another Password type "1"?'))
    if another == 1:
        continue
    else:
        do_another_password = False
     