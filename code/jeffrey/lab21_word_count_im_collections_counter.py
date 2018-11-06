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

# print(word_list)
# print(string.punctuation)

# big_dict = {x:word_list.count(x) for x in set(word_list)}

counter = collections.Counter(word_list)

print(counter.most_common(50))

print(f"My program took {time.time() - start_time} to run")