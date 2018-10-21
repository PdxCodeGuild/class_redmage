#lab6_passgen.py

#import random and string to source characters and to randomly choose from them
import random
import string

# priming
usercaps = ""
userlower = ""
usersym = ""
capstring = string.ascii_uppercase
lowerstring = string.ascii_lowercase
symstring = string.punctuation
password = ""

# collecting desired values
while usercaps == "":
    usercaps = input("How many capital letters do you want in your password? (enter a number or 'none'): ")
    if usercaps == "none":
        break
    else:
        usercaps = int(usercaps)

while userlower == "":
    userlower = input("How many lowercase letters do you want in your password? (enter a number or 'none'): ")
    if userlower == "none":
        break
    else:
        userlower = int(userlower)

while usersym == "":
    usersym = input("How many special characters do you want in your password? (enter a number or 'none'): ")
    if usersym == "none":
        break
    else:
        usersym = int(usersym)


# randomly selecting from the right list
if usercaps != "none":
        for i in range(abs(usercaps)):
           password = password + random.choice(capstring)
if userlower != "none":
    for i in range(abs(userlower)):
            password = password + random.choice(lowerstring)
if usersym != "none":
    for i in range(abs(usersym)):
        password = password + random.choice(symstring)

password = list(password)
random.shuffle(password)
pass_string = "".join(password)
print(f"Your new password is {pass_string}")