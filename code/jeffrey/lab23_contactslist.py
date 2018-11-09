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

# List of CRUD FUNCTIONS BELOW
def create():
    user_val2 = input(f'Input your {(keys[1])}: ')
    user_val3 = input(f'Input your {(keys[2])}: ')
    entry_str = ','.join([user_name,user_val2,user_val3])
    for x in range(len(entry_str.split(','))):
        line = entry_str.split(',')
        entry = dict(zip(keys,line))
        contacts_dict.append(entry)
    print(contacts_dict)

# def retrieve():

# def update():

# def delete():

while True:
    user_name = input(f'What is your {(keys[0])}? \n')
    choice = input(f'''
    Welcome {user_name}, you have four options for actions:
    1. 'create' for making a new record
    2. 'retrieve' for retreiving a record
    3. 'update' for updating a record
    4.  'delete' for deleting a record\n
    What would you like to do? 
    ''')
    if choice.lower() == 'create':
        create()
    # elif choice.lower() == 'retrieve':
    #     retrieve()
    # elif choice.lower() == 'update':
    #     update()
    # elif  choice.lower() == 'delete':
    #     delete()
    end_prog = input('Input any key to do another action or "quit" to exit the program:\n')
    if end_prog.lower() == 'quit':
        break


