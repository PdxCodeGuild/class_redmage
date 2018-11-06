import string
import re
import collections
import os
import time
import inspect

start_time = time.time()

moby_dick = open(r'C:\Users\jeffr\Documents\Projects\class_redmage\moby_dick.txt', 'r', encoding='utf8')

# base_name = os.path.basename(moby_dick)

book_open = moby_dick.read()

file_base_name = (os.path.basename(moby_dick.name))

moby_dick.close()

punct = string.punctuation 

word_list = book_open.lower().split()

input_text = ' '.join(word_list)
input_text = re.sub(r'[!"#$%&\'""()*+,-./:;<=>?@[\]^_`{|}~]', ' ', input_text)

word_list = input_text.split()

big_dict = {}


# dictionary maker; for the index in the range of the length of the word_list, if the tuple of the word at 'i' index and the following word are not in the keys of the dictionary, then add them and set them equal to 1. If they are in the keys then set them equal to +1 of whatever the value currently is:
for i in range(len(word_list)-1):
    if (word_list[i],word_list[i+1]) not in big_dict.keys():
        big_dict[(word_list[i],word_list[i+1])] = 1
    elif (word_list[i],word_list[i+1]) in big_dict.keys():
        big_dict[(word_list[i],word_list[i+1])] += 1

user_in = input(f"Input a string to see it's pairs in {file_base_name}: ")

small_dict = {key:big_dict[key] for key in big_dict if key[0] == user_in}

words = list(small_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])

print(f"My program took {time.time() - start_time} to run")