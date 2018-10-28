import string
with open('text.txt', 'r') as book:
    data = book.read()
book.close()

#Make Book Lowercase
book_lowercase = data.lower()

#Strip Puctuation
#list_punc = list(string.punctuation)
#tr = str.maketrans("", "", string.punctuation)

#Why does replace only work once and then, when you list another acharcter to split it reverts back.
#ask about this in class

#string_test = string_test.replace('.', "")


#book_lowercase.replace(puct_list[13], '')


transtable = str.maketrans('', '', string.punctuation)

new_book = book_lowercase.translate(transtable)

words = list(new_book.
print(words)

