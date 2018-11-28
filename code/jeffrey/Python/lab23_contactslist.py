import time

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
    
    entry_str = (user_val1.lower(),user_val2.lower(),user_val3.lower())
    
    checker = input(f"Enter 'no if you don't want to add: {entry_str}")
    
    if checker.lower() != 'no':
        entry = dict(zip(keys,entry_str))
        contacts_dict.append(entry)
        time.sleep(.5)
        return contacts_dict
    print('Record created!\n')
    
def retrieve():
    user_val1 = input(f'What is the {keys[0]} of the record that you would like to retrieve? ').lower()

    for i in range(len(contacts_dict)):
        if user_val1 == contacts_dict[i][keys[0]]:
            time.sleep(.5)
            print(f'\nRecord: {contacts_dict[i]}\n')
            time.sleep(.5)
            return

# def update():
def update():
    record = input(f'What is the {keys[0]} of the record that you would like to update?').lower()
    attribute = input(f'What is the attribute that you would like to set: "{keys[0]}", "{keys[1]}", or "{keys[2]}"?').lower()
    new_attribute = input(f'What would you like to change the "{attribute}" to? ')
    if attribute in keys:
        for i in range(len(contacts_dict)):
            if record == contacts_dict[i][keys[0]]:
                contacts_dict[i][attribute] = new_attribute
                time.sleep(.5)
                print("Update complete!\n")
                return contacts_dict

# def delete():
def delete():
    record = input(f'What is the {keys[0]} of the record that you would like to delete?')
    for i in range(len(contacts_dict)):
        if record == contacts_dict[i][keys[0]]:
            contacts_dict.remove(contacts_dict[i])
            time.sleep(.5)
            print("Record deleted.")
            return contacts_dict

while True:
    print(contacts_dict)
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
    elif choice.lower() == 'update':
        update()
    elif  choice.lower() == 'delete':
        delete()
    end_prog = input('Input any key to do another action or "quit" to exit the program:\n')
    if end_prog.lower() == 'quit':
        break

# sending back to csv reverets and prints back the first operation to the csv:
new_data = []
#starts list with the keys 
new_data.append(",".join(keys))
#converts the values from every dict to a list
for i in range(len(contacts_dict)):
    data_list = list(contacts_dict[i].values()) 
    data = ",".join(data_list)
    new_data.append(data)
#formats the list to a string seperated by \n
new_data = "\n".join(new_data)


with open('contact_list.csv', "w") as file:
    file.write(str(new_data))