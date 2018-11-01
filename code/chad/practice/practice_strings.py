import string

'''
1. Get a string from the user, print out another string, doubling every letter.
user_input = input('Give Me A String? >')
def double(x):
    double_letter = []
    for num in x:
        double_letter.append(num*2)
    double_letter = ''.join(double_letter)
    return double_letter
print(double(user_input))
2. Write a function that takes a string, and returns a list of strings, each missing a different character.

import random
user_input = input('Give Me A String? >')
old_list = list(user_input)
random_index = random.sample(range(0,len(old_list)), k=len(old_list))
print(random_index)
def remove(user_input):
    for num in random_index:
        print(num)
        old_list = list(user_input)
        old_list.pop(num)
        print(''.join(old_list))


remove(user_input)

def latest():
    latest = 'fjdhshzrhtnvnv'
    latest_list = list(latest)
    latest_list = sorted(latest_list)
    print(latest_list)
    print(latest_list[-1])

latest()


'''