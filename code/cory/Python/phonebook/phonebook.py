#phonebook.py

with open('phonebook.txt', 'r') as phone_book_file:
    data = phone_book_file.read().strip('\n').split(' ')
    # data = dict(data)
    print(data)