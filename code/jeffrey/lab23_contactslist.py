# opens a CSV file with write capability and reads it to variable: lines while splitting it on each line
with open('contact_list.csv', 'r+') as file:
    lines = file.read().split('\n')

# create a new dict to append to later
contacts_dict = []

# user the first line as header to create the keys for the dict
keys = lines[0].split(',')

# loop through the lines adding the them to the dict under their appropriate keys starting after the header line (row)
for i in range(1,len(lines)):
    # splits each line based off the commas
    line = lines[i].split(',')
    # creates a dict out of the keys and the line items so that the items at the index fit into the keys at the same index (it makes them friends and then they are added into a dict)
    entry = dict(zip(keys,line))
    # add those mini-dict entries to the list
    contacts_dict.append(entry)

print(contacts_dict)

def create(choice):

def retrieve(choice):

def update(choice):

def delete(choice):

while True:
    choice = input(f'''
    You have four options for actions:
    \n1. 'create' for making a new record
    \n2. 'retrieve' for retreiving a record
    \n3. 'update' for updating a record
    \n4.  'delete' for deleting a record
    \nWhat would you like to do? 
    ''')
    if choice ==
user_val1 = input(f'Input your {(keys[0])}:')
user_val2 = input(f'Input your {(keys[1])}:')
user_val3 = input(f'Input your {(keys[2])}:')
