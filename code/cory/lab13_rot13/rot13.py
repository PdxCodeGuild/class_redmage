# Version 2

import string

def rot13_func(rotation):

    # Create list of all letter characters (a - z)
    abc_list = list(string.ascii_lowercase)

    # Create rot13 list to hold rotated alphabet. ex "a == n" for 13
    rot13_list = []

    # Use .extend to pass the values of a list into rot13_list. If using  rot13_list.append(abc_list[x]), it makes a list inside a list.
    rot13_list.extend(abc_list[rotation:len(abc_list)] + abc_list[0:rotation]) 

    # Create an encrypted dictionary, so when we ask the user what string they want to encrypt the dictionary will be ready and set. (a: n, b: o, c: p)
    encryption_dictionary = {}
    for i in range(len(abc_list)):
        encryption_dictionary[abc_list[i]] = rot13_list[i]

    return encryption_dictionary

# Ask user for rot13 rotation, returns the "key: value" encrypted dictionary
encryption_dictionary = rot13_func(int(input("How many digits would you like to shift too? > ")))

# Ask user for a string
user_inp = input("What string of letters would you like to encrypt? > ").lower()

# Change each letter of the string by looking up the key: value in the encrypted dictionary
encrypt_result = ''
for char in user_inp:
    encrypt_result += encryption_dictionary[char]

# Print result
print(f" The word you wanted to encrypt was {user_inp}. Your new ROT13 encrypted word is {encrypt_result}!")