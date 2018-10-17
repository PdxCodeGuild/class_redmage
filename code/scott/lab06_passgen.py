#lab6_passgen.py

#import random and string to source characters and to randomly choose from them
import random
import string

# generating a ranom string from which to get characters for the password (punctuation added twice to increase likelihood of special characters)
pass_string = string.punctuation + string.ascii_letters + string.punctuation

# priming
input_num = 0
start_num = 0
new_pass = ""

# making sure the user is inputting a valid number
while input_num not in range (10, 21):
    input_num = int(input("How long do you want your password to be? Please choose a number between 10 and 20 :"))

# iterate up to the numbere entered by the user
for i in range(0, input_num):
    new_pass += str(random.choice(pass_string))

print(new_pass)