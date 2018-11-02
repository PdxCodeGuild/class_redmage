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

# Convert list into touples, word1 + word2 , word2+ word3...
tup_list = []
for i in range(len(main_text)):
    if main_text[i] == main_text[len(main_text) - 1]:
        pass
    else:
        tup_list.append((main_text[i], main_text[i + 1]))

# New dictionary
main_dict = {}

# Takes strings in main text, transfers to key in dictionary with a default value of 1. If the key already exists, it += 1
for key in tup_list:
    if key in main_dict:
        main_dict[key] += 1
    else:
        main_dict.update({key: 1})

num_of_pairs = len(main_dict)

# Sorted by largest. Added if True: to minimize screen space
if True:
    words = list(main_dict.items())

    words.sort(key=lambda tup: tup[1], reverse=True)

    for i in range(min(10, len(words))):
        print(f"The pair {words[i][0]} occured {words[i][1]} times.")

    print(f"\nTotal number of word pairs in Astounding Stories of Super-Science January 1930: {num_of_pairs}.\n")
