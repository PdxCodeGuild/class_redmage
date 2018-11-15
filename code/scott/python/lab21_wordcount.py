# lab21_wordcount.py
import string
import sys
# Open the file.
# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the code below.

try:
    user_file = sys.argv[1]
except IndexError:
    user_file = input("You forgot to enter a file to process (python lab21_wordcount.py 'file_to_process'). Enter the filename to process now > ")

with open('user_file', 'r') as file:
    words = file.read().split()

for i in range(len(words)):
    words[i] = words[i].lower()

words = [''.join(letter for letter in word if letter not in string.punctuation) for word in words]

print(len(words))

# dict of individual words and counts
word_dict = {word: words.count(word) for word in words}

# dict of consecutive word pairs and counts
pairs = []
for i in range(len(words)-1):
    pair = words[i] + " " + words[i+1]
    pairs.append((pair))
pairs_dict = {pair: pairs.count(pair) for pair in pairs}

pairs = list(pairs_dict.items())
words = list(word_dict.items())  # .items() returns a list of tuples

# sort largest to smallest, based on count

words.sort(key=lambda tup: tup[1], reverse=True)
pairs.sort(key=lambda tup: tup[1], reverse=True)

for i in range(min(10, len(words))):
    print(words[i])

for i in range(min(10, len(pairs))):
    print(pairs[i])

# Version 2
# Count how often each unique pair of words is used, then print the top 10 most common pairs with their counts.

# Version 3 (optional)
# Let the user enter a word, then show the words which most frequently follow it.
