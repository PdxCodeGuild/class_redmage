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
trackList = []
def remove(x):
    new_list = []
    while True:
        old_list = list(x)
        random_number = random.randint(0, len(old_list)-1)
        print(f'Current Tracklist is {trackList}')
        print(random_number)
        if random_number not in trackList:
            print(random_number)
            trackList.append(random_number)
            old_list[random_number] = old_list.pop()
        if random_number in trackList:
            continue
        print(old_list)
        join_list = ''.join(old_list)
        new_list.append(join_list)
        if len(trackList) == len(old_list):
            break
    print(new_list)
    return new_list

print(remove(user_input))
