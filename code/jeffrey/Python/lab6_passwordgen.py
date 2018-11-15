import random
import string

pv_upper = string.ascii_uppercase
pv_lower = string.ascii_lowercase
pv_number = string.digits
pv_punct = string.punctuation

print("These characters below are your options:\n",pv_upper,pv_lower,pv_number,pv_punct,"\n")

i = 0
o = 0
u = 0
b = 0

password = ""

user_in = input("Do you want to create a new password[y/n]? \n")

if user_in == "y":
    print("\nI'll now ask you how many of each character type you want in your password.\n")

    u_length = int(input("Uppercase letters: "))
    l_length = int(input("Lowercase letters: "))
    n_length = int(input("Numbers: "))
    p_length = int(input("Punctuation: "))

    while i < u_length:
        password += random.choice(pv_upper)
        i += 1
    while o < l_length:
        password += random.choice(pv_lower)
        o += 1
    while u < l_length:
        password += random.choice(pv_number)
        u += 1
    while b < l_length:
        password += random.choice(pv_punct)
        b += 1
    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    print("Your new password: "+ str(password))
elif user_in =="n":
    print("When you want to create a new password, I'll be waiting.")
else:
    print("Try again later.")