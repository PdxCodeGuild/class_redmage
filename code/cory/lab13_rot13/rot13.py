# Version 2

import string

def rot13_encrypt(rotation):

    # Create list of all letter characters (a - z)
    abc_list = list(string.ascii_lowercase)

    # Create rot13 list to hold rotated alphabet. ex "a == n" for 13
    rot13_list = []

    # Use .extend to pass the values of a list into rot13_list. If using  rot13_list.append(abc_list[x]), it makes a list inside a list.
    rot13_list.extend(abc_list[rotation:len(abc_list)] + abc_list[0:rotation]) 

    # Create an encrypted/decrypted dictionaries, so when we ask the user what string they want to encrypt the dictionary will be ready and set. (a: n, b: o, c: p)

    encryption_dictionary = {}
    for i in range(len(abc_list)):
        encryption_dictionary[abc_list[i]] = rot13_list[i]

    return encryption_dictionary

def rot13_decrypt(rotation):

    # Create list of all letter characters (a - z)
    abc_list = list(string.ascii_lowercase)

    # Create rot13 list to hold rotated alphabet. ex "a == n" for 13
    rot13_list = []

    # Use .extend to pass the values of a list into rot13_list. If using  rot13_list.append(abc_list[x]), it makes a list inside a list.
    rot13_list.extend(abc_list[rotation:len(abc_list)] + abc_list[0:rotation]) 

    # Create an encrypted dictionary, so when we ask the user what string they want to encrypt the dictionary will be ready and set. (a: n, b: o, c: p)
    decryption_dictionary = {}
    for i in range(len(abc_list)):
        decryption_dictionary[rot13_list[i]] = abc_list[i]
    
    return decryption_dictionary


# Ask user for rot13 rotation, returns the "key: value" encrypt/decrypt dictionary
rotation = int(input("How much would you like to rotate the codex? > "))

# Sets both dictionaries you need for the rest of the program
encryption_dictionary = rot13_encrypt(rotation)
decryption_dictionary = rot13_decrypt(rotation)

# Ask user for a string
user_inp = input("What string of letters would you like to encrypt? > ").lower()

# Change each letter of the string by looking up the key: value in the encrypted dictionary
encrypt_result = ''
for char in user_inp:
    encrypt_result += encryption_dictionary[char]

# Print result
print(f" The word you wanted to encrypt was {user_inp}. Your new ROT13 encrypted word is {encrypt_result}!")

# Ask user if they would like to decript, copy pasted with minor changes
user_decrypt = input(f"Would you like to decrypt {user_inp}? (y/n) > ")

if user_decrypt == 'y':
    decrypt_result = ''
    for char in encrypt_result:
        decrypt_result += decryption_dictionary[char]

    # Print result
    print(f" The word you encrypted was {encrypt_result}. The decrpyted string is {decrypt_result}!")
else:
    print("\nYou're done!\n")