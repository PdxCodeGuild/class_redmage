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

user_name = input(f'What is your {(keys[0])}? \n')

# List of CRUD FUNCTIONS BELOW
def create():
    user_val1 = input(f'Input the {(keys[0])}: ')
    user_val2 = input(f'Input the {(keys[1])}: ')
    user_val3 = input(f'Input the {(keys[2])}: ')
    
    entry_str = (user_val1,user_val2,user_val3)
    
    checker = input(f'Enter "yes" if you want to add: {entry_str}')
    
    if checker.lower() == 'yes':
        entry = dict(zip(keys,entry_str))
        contacts_dict.append(entry)

def retrieve():
    user_val1 = input(f'What is the {(keys[0])} of the record that you would like to retrieve? ').lower()
    for i in range(len(contacts_dict)):
        if user_val1 == contacts_dict[i][(keys[0])]:
            print(f'\n{contacts_dict[i]}\n')
            return contacts_dict

# def update():


# def delete():


while True:
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
    elif choice.lower() == 'retrieve':
        retrieve()
    # elif choice.lower() == 'update':
    #     update()
    # elif  choice.lower() == 'delete':
    #     delete()
    end_prog = input('Input any key to do another action or "quit" to exit the program:\n')
    if end_prog.lower() == 'quit':
        break


