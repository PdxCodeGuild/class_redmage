# with open('scrape_data.csv', 'r') as f:
#     data = f.read().strip().split('\n')
# f.close()   


# header = data[0].split(',')
# print(header)

# book_list = []
# for i in range(1, len(data)):
#     book_list.append(data[i] for i in range(1, len(data)))

# book_list = book_list[1].split(',')
# print(book_list)

# import datetime

# now = datetime.datetime.now().strftime("%b-%d-%Y_%H-%M-%S")

# print(now)

# from amazon_reviews_project import tester

# def remove_comma(string):

#     new_string = ''
#     for char in string:
#         if char == ',':
#             new_string += ''
#         else:
#             new_string += char

#     return (new_string)
    
# tester = remove_comma(tester)

# print(tester)

# def punct_checker(sentance):

#     sentance = list(sentance)
#     end_punctuation = ['.', '!', '?', ',']
#     # end_punctuation = ['.', '?']

#     for punct in end_punctuation:
#         for i in range(len(sentance) - 1, -1, -1):
#             print(i)
#             if i != len(sentance) - 1:
#                 if sentance[i] == punct:    
#                     print(punct)
#                     if sentance[i + 1] == ' ':
#                         pass
#                     else:
#                         sentance.insert((i+1), ' ')

#     sentance = ''.join(sentance).strip()
#     return sentance

# test = "It has been three years since the Progerians left their mark of devastation upon Earth. The remaining humans are in a desperate race against time as they do their best to reverse engineer the alien technology they captured+ in an effort to bolster their beleaguered defenses against the oncoming onslaught of Progerians hell-bent on revenge. Revenge against the humans that thwarted their take-over and revenge against the subordinate Genogerians that helped.Michael Talbot once again finds himself at the forefront to protect all that is sacred to him. He will receive help from some unexpected allies but will it be enough?"


# test = punct_checker(test)

# print(test)


# x = input()

# if int(x) in range(1, 11):
#     print('True')
# else:
#     print('False')

from amazon_reviews_project import scifi_dictionaries

test_dict = [scifi_dictionaries[x] for x in range(10)]

for i in range(len(test_dict)):
    author_list = [test_dict[i]['Author'] for i in range(len(test_dict))]

print(author_list)

author_dict = {}
for key in author_list:
    if key in author_dict:
        author_dict[key] += 1
    else:
        author_dict.update({key:1})

words = list(author_dict.items())

words.sort(key=lambda tup: tup[1], reverse=True)

print(words)