import string, time
with open('/home/chad/Documents/git_hub/class_redmage/code/chad/lab_21/text.txt', 'r') as book:
    data = book.read()
book.close()

count_popped_blanks = []

#Remove Puctuation, make lowercase, strip blanks, split into list and return list
def rem_punc(data):
    book_lowercase = data.lower()

    transtable = str.maketrans('', '', string.punctuation)
    new_book = book_lowercase.translate(transtable)

    transtable = str.maketrans(' ', ' ')
    new_book = new_book.translate(transtable)


    transtable = str.maketrans(' ', ',')
    new_book = new_book.translate(transtable)

    return new_book.split(',')

#REmove all the new \n lines
def rem_newlines(new_book):
    for i in range(len(new_book)):
        if '\n' in new_book[i]:
            new_book[i] = new_book[i].replace('\n', '')
    return new_book 


#Remove all empty lists
def remove_blanks_action():
    num_popped = 0
    for i in range(len(new_book)):
        if i == len(new_book):
            print('done with list')
            print(f'you are at index {i}')
            print(f' The length of book is now {len(new_book)}')
            return num_popped
        if '' == new_book[i]:
            count_popped_blanks.append(new_book.pop(i))
            num_popped += 1
    
def remove_blanks_check(new_book):     
    while True:
        check_for_blanks = remove_blanks_action()
        try:
            if check_for_blanks > 0:
                continue
        except TypeError: 
            print('you caught a typeerror returned so no more blanks, break')
            break
        if check_for_blanks == 0:
            break
    return new_book

#Sort List and make into dictionary with how many words exist
def make_dict(new_book):
    new_book = sorted(new_book)
    for i in new_book:
        print(f'You found {new_book.count(i)} of {i}')
        input()

    #for i in range(len(new_book)):
     #   if 

#Call function rem_puc to lowercase and remove puctuation and return into a list
new_book = rem_punc(data)

#Remove \n new lines
new_book = rem_newlines(new_book)

#Recursivly check and delete blanks
new_book = remove_blanks_check(new_book)

#Take words Sort and put in dictionary with value how many times they appear
make_dictionary = make_dict(new_book)

#Print List Of Words
#print(new_book)

#Print Dictionary Word COunt
#print(make_dictionary)

#Print How Many BLanks Popped out
print(f'You popped {len(count_popped_blanks)} Blanks')
