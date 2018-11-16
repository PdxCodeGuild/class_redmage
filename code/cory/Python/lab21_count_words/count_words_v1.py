import string

# Opens and extracts text from file
with open('pg41481.txt', 'r') as textfile:
    main_text_file = textfile.read().lower().strip('\n')
    textfile.close()

# Creates a list out of text file so we can modify 
main_text = list(main_text_file)

# Removes punctuation and occourances of "\n"
def remove_punctuation(list1):

    punct = list(string.punctuation)
    punct.append("\n")

    for y in range(len(punct)):
        for x in range(len(list1) - 1, 0, -1):
            if list1[x] == punct[y]:
                list1.pop(x)

    list1 = ''.join(list1)

    return list1

main_text = remove_punctuation(main_text)

# Splits list up by ' '
def split_list(list1):

    list1 = list1.split(' ')

    return list1

main_text = split_list(main_text) 

# Removes occurances of '' in list
for i in range(len(main_text) - 1, 0, -1):
    if main_text[i] == '':
        main_text.pop(i)

# Number of words in main_text, just curious
num_of_words = len(main_text)

# New dictionary
main_dict = {}

# Takes strings in main text, transfers to key in dictionary with a default value of 1. If the key already exists, it += 1
for key in main_text:
    if key in main_dict:
        main_dict[key] += 1
    else:
        main_dict.update({key: 1})
 
# Sorted by largest. Added if True: to minimize screen space
if True:
    words = list(main_dict.items())

    words.sort(key=lambda tup: tup[1], reverse=True)

    for i in range(min(10, len(words))):
        print(words[i])

    print(f"\nTotal number of words in Astounding Stories of Super-Science January 1930: {num_of_words}.\n")
'''
# Ask Merrit to go over:

# words.sort(key=lambda tup: tup[1], reverse=True) > # sort largest to smallest, based on count

# for i in range(min(10, len(words))) > # print the top 10 words, or all of them, whichever is smaller
'''