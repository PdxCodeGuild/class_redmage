#password Generator
# this step will import the strings
import random
import string

#password will use these charecters
pw_string = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation

#setting up
input_pw = 0
start_num = 0
new_pass = ""

#ask the question how long do you want your password to be within so many charecters the user must choose
while input_pw not in range (10, 17):
    input_pw = int(input("How long do you want your password to be? Please choose a number between 10 and 16 :"))

# iterate up to the number entered by the user
for i in range(0, input_pw):
    new_pass += str(random.choice(pw_string))

print(new_pass)