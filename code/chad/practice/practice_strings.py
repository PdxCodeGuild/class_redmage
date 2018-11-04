import string

'''
PROBLEM 1
1. Get a string from the user, print out another string, doubling every letter.
user_input = input('Give Me A String? >')
def double(x):
    double_letter = []
    for num in x:
        double_letter.append(num*2)
    double_letter = ''.join(double_letter)
    return double_letter
print(double(user_input))

PROBLEM 2
2. Write a function that takes a string, and returns a list of strings, each missing a different character.

import random
user_input = input('Give Me A String? >')
<<<<<<< HEAD
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
=======
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

PROBLEM 3:

def latest():
    latest = 'fjdhshzrhtnvnv'
    latest_list = list(latest)
    latest_list = sorted(latest_list)
    print(latest_list)
    print(latest_list[-1])

latest()

Problem 4

Write a function that returns the number of occurances of 'hi' in a given string.

count_hi('hihi') → 2

string_hi = 'hihigfhigfihihihgfhi'

#ill cheat and use count method of string :)
def count_hi():
     print(string_hi.count('hi'))

count_hi()


Problem 4 (using slicing)

string_hi = 'hihigfhigfihihihgfhi'


def count_hi():
        start = 0
        stop = 2
        count = 0
        for i in range(len(string_hi)):
                print(string_hi[start:stop])
                if string_hi[start:stop] == 'hi':
                        print('found one')
                        count += 1
                start += 1
                stop += 1
        print(count)
count_hi()

PROBLEM 5:
Write a function that returns True if a given string contains the same number of 'cat' as it does 'dog'

'''
test_string = 'catdogcat'
test_string2 = 'catdogcatdog'

def catdog(cats, dogs):
        print(cats)
        print(dogs)
        same = cats == dogs
        return same

#Count How Many Dogs
def count_cat(test):
        start = 0
        stop = 3
        count = 0
        for i in range(len(test)):
                print(test[start:stop])
                if test[start:stop] == 'cat':
                        print('found one')
                        count += 1
                start += 1
                stop += 1
        return count
# Count How Many Dogs in the string
def count_dog(test):
        start = 0
        stop = 3
        count = 0
        for i in range(len(test)):
                print(test[start:stop])
                if test[start:stop] == 'dog':
                        print('found one')
                        count += 1
                start += 1
                stop += 1
        return count
#switch test_string or test_string2
found_cats = count_cat(test_string2)
found_dogs = count_dog(test_string2)
print(catdog(found_cats, found_dogs))

>>>>>>> 24732261e3cd8f37d118556fd94faa08d6e09515
