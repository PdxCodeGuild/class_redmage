import string
import re
import collections

import time
start_time = time.time()

moby_dick = open(r'C:\Users\jeffr\Documents\Projects\class_redmage\moby_dick.txt', 'r', encoding='utf8')

book_open = moby_dick.read()

moby_dick.close()

punct = string.punctuation 

word_list = book_open.lower().split()

input_text = ' '.join(word_list)
input_text = re.sub(r'[!"#$%&\'""()*+,-./:;<=>?@[\]^_`{|}~]', ' ', input_text)

word_list = input_text.split()

big_dict = {}

for i in range(len(word_list)-1):
    if (word_list[i],word_list[i+1]) not in big_dict.keys():
        big_dict[(word_list[i],word_list[i+1])] = 1
    elif (word_list[i],word_list[i+1]) in big_dict.keys():
        big_dict[(word_list[i],word_list[i+1])] += 1

print(big_dict)

words = list(big_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])

print(f"My program took {time.time() - start_time} to run")