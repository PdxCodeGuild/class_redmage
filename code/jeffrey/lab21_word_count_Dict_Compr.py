import string
import re

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

# print(word_list)
# print(string.punctuation)

big_dict = {x:word_list.count(x) for x in set(word_list)}

# word_dict is a dictionary where the key is the word and the value is the count
words = list(big_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

print(f"My program took {time.time() - start_time} to run")