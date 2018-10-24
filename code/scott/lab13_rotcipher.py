# lab13_rotcipher.py

# importing the string to get an alphabet
import string

# making Englishes
alpha_list = list(string.ascii_uppercase)

# obtaining input message
user_message = input("Enter the string you would like to encode. ")
user_message = user_message.upper()

# obtaining cipher number
cipher_num = int(input("how many numbers would you like to shift the cipher? (valid integers: 0 - 25)>"))

# creating the cipher
rot_cipher = []
rot_cipher.extend(alpha_list[int(cipher_num)::])
rot_cipher.extend(alpha_list[:int(cipher_num):])

# iterating through each letter in the user's message, finding the corresponding index, and creating list of those indeces
encoded_nums = []
for item in user_message:
    encoded_nums.append(alpha_list.index(item))

# iterating through the list of indeces to find the corresponding letter in the ROT cipher created earlier
encoded_msg = []
for item in encoded_nums:
    encoded_msg.append(rot_cipher[item])

encoded_msg = "".join(encoded_msg)

print(f"Your encoded message is: '{encoded_msg}' ")

