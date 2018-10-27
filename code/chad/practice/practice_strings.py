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
'''
import random
user_input = input('Give Me A String? >')

def remove(x):
    new_list = []
    for num in range(5):
        old_list = list(x)
        old_list.pop(random.sample(old_list, 3))
        print(old_list)
        join_list = ''.join(old_list)
        new_list.append(join_list)
    print(new_list)
    return new_list

print(remove(user_input))
