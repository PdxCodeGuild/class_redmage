import string, time
with open('text.txt', 'r') as book:
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
def find10(new_book):
    new_book = sorted(new_book)
    
    #Store the finds from the loop below in a temp dictionary before returning
    temp_dic = []

    #Count Instances of Words and Append to list
    for i in new_book:
        count = new_book.count(i)
        temp_dic.append((count, i))

    make_list = list(temp_dic)
    
    make_set = set((make_list))
    make_set = sorted(make_set, reverse=True)

    # Loop Through Last 10 Items and return
    print('\n\nHere is the Top words:\n')
    for item in make_set[0:10]:
        print(item)

#Function TO Find Unique Pairs:

def unique_pairs(data):
    unique_list = []
    #create new list with word pairs
    for i in range(len(data)):
        try:
            unique_list.append((data[i], data[i+1]))
        except:
            pass
    filtered_list = []
    for i in unique_list:
        count = unique_list.count(i)
        filtered_list.append((count, (i)))
    sorted_list = sorted(filtered_list)
    sorted_sort = set(sorted_list)
    sorted_sort = sorted(sorted_sort)
    
    #Print The top 10 counted word pairs
    print('\n\nHere are the top counted word pairs\n')
    for i in sorted_sort[-1:-11:-1]:
        print(i)
        
#Call function rem_puc to lowercase and remove puctuation and return into a list
new_book = rem_punc(data)

#Remove \n new lines
new_book = rem_newlines(new_book)

#Recursivly check and delete blanks
new_book = remove_blanks_check(new_book)

#Take words Sort and put in dictionary with value how many times they appear
make_dictionary = find10(new_book)

#Find Unique Pairs Of Words:
unique_pairs(new_book)

print(f'You popped {len(count_popped_blanks)} Blanks')