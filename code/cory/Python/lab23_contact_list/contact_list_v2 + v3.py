with open('contacts.csv', 'r') as contacts:
    lines = contacts.read().strip('\n').split('\n')
    contacts.close()

# Created a list for keys and a list that holds multiple user values
keys = lines[0].split(',')
user_values = [lines[i].split(',') for i in range(1, len(lines))]

# Function to create tuples, joining keys for each user in the CSV
def tuple_creator(user_values):

    tuple_list = [(keys[i], user_values[i]) for i in range(len(keys))]

    return tuple_list

# Function to take tuple_list, convert the list in to a dictionary, then store it in our main list (list of dictionaries)
def dict_creator(tuple_list): 

    dict_list = {key: value for key, value in tuple_list}

    return dict_list

# Function to use the master contact list
def get_contact_list():
    get_contact_list = [dict_creator(tuple_creator(user_values[i])) for i in range(len(user_values))]
    return get_contact_list

# Function to create new user
def create():

    out_list = []
    create_flag = True
    while create_flag:
        print("\nTo create a new user I'll need some information. Please answer the following questions.\n")
        
        new_name = input("What is the name of the user? > ").lower()
        new_fruit = input("What is the users favorite fruit? > ").lower()
        new_color = input("What is the users favorite color? > ").lower()
        
        out_list.append([new_name, new_fruit, new_color])

        end_flag = True
        while end_flag:
            create_another = input("Would you like to create another user? (y/n) > ").lower()
            
            if create_another == 'n':
                print("\n...")
                end_flag = False
                create_flag = False
            
            elif create_another == 'y':
                print("\n...")
                end_flag = False

            else:
                print("The program doesn't seem to like that input... Let's try that again.")

    return out_list

# Function to retrieve user data
def retrieve():
    retrieve_flag = True
    while retrieve_flag:

        name_list = [user_values[i][0] for i in range(len(user_values))]

        name_input = input("\nWhat is the name of the user that you want to look up? (try 'options') > ")

        if name_input == 'options':
            print("\nYour options are: 'show users', 'quit'.")

        elif name_input == 'show users' or name_input == 'show':
            print()
            for i in range(len(user_values)):
                print(user_values[i][0])

        elif name_input in name_list:
            for i in range(len(user_values)):
                if name_input == user_values[i][0]:
                    
                    print(f"\nThe user you have chosen is {user_values[i][0].capitalize()}. Their favorite fruit is {user_values[i][1]}, and their favorite color is {user_values[i][2]}.")

        elif name_input == 'quit':
            print("\n...")
            retrieve_flag = False

        else:
            print("\nThe program doesn't seem to like that input... Let's try that again.")
    
    return

# Function to update user data < make permission loop for updates
def update():
    update_flag = True
    while update_flag:
        
        name_list = [user_values[i][0] for i in range(len(user_values))]

        update_name = input("\nWhat is the name of the user that you want to update? (try 'options') > ").lower()

        if update_name == 'options':
                print("\nYour options are: 'show users', 'quit'.")

        elif update_name == 'show users' or update_name == 'show':
                print()
                for i in range(len(user_values)):
                    print(user_values[i][0])

        elif update_name in name_list:
                for i in range(len(user_values)):
                    if update_name == user_values[i][0]:
                        
                        which_value = input("\nWhich value would you like to change? 1.) Name 2.) Fruit 3.) Color > ").lower()

                        if which_value == 'name':
                            name_change = input("What would you like the name to be changed to? > ").lower()
                            user_values[i][0] = name_change

                        elif which_value == 'fruit':
                            name_change = input("What would you like their fruit to be changed to? > ").lower()
                            user_values[i][1] = name_change

                        elif which_value == 'color':
                            name_change = input("What would you like their color to be changed to? > ").lower()
                            user_values[i][2] = name_change
                        else:
                            print("\nThe program doesn't seem to like that input... Let's try that again.")

        elif update_name == 'quit':
            print("\n...")
            update_flag = False
        
        else:
            print("\nThe program doesn't seem to like that input... Let's try that again.")
    
    return

# Function to delete user data
def delete():
    delete_flag = True
    while delete_flag:

        name_list = [user_values[i][0] for i in range(len(user_values))]

        name_input = input("\nWhat is the name of the user that you want to delete? (try 'options') > ")

        if name_input == 'options':
            print("\nYour options are: 'show users', 'quit'.")

        elif name_input == 'show users' or name_input == 'show':
            print()
            for i in range(len(user_values)):
                print(user_values[i][0])

        elif name_input in name_list:
            for i in range(len(user_values)):
                if name_input == user_values[i][0]:
                    
                    print(f"\nThe user you have chosen is {user_values[i][0].capitalize()}. Their favorite fruit is {user_values[i][1]}, and their favorite color is {user_values[i][2]}.")
                    
                    del_perm = input(f"Are you sure you want to delete {user_values[i][0]} from this list? (y/n) > ").lower()

                    if del_perm == 'y':
                        user_values.pop(i)
                        break
                    
                    elif del_perm == 'n':
                        print("\nYou can choose to delete this user at any other time, just choose 'delete' from the main menu.")

                    else:
                        print("\nThe program doesn't seem to like that input... Let's try that again.")

        elif name_input == 'quit':
            print("\n...")
            delete_flag = False

        else:
            print("\nThe program doesn't seem to like that input... Let's try that again.")
    
    return

# Function to save user data
def save():
    loop_flag = True
    while loop_flag:
        
        save_input = ''
        while save_input != 'y' and save_input != 'n':
            save_input = input("\nWould you like to save the current changes to the data? (y/n) > ")

            if save_input != 'y' and save_input != 'n':
                print("\nThe program doesn't seem to like that input... Let's try that again.")

        if save_input == 'n':
            print("\n...")

            loop_flag = False

            break

        elif save_input == 'y':
            
            # Compile all user data, change to string so csv can read
            contacts_list = get_contact_list()

            # String for keys
            out_keys = ''
            for i in range(len(keys)):
                out_keys += keys[i] + ','
            out_keys = out_keys.rstrip(',')
            out_keys += "\n"

            # String for user data
            out_data = ''
            for i in range(len(contacts_list)):
                out_data += contacts_list[i]['name'] + ','
                out_data += contacts_list[i]['favorite fruit'] + ','
                out_data += contacts_list[i]['favorite color']
                out_data += "\n"

            with open('contacts.csv', 'w') as contacts:
                contacts.write(out_keys)
                contacts.write(out_data)
                contacts.close()
            
            print("\n...")

            loop_flag = False

            break

# User Interface
interface_flag = True
while interface_flag:
    
    interface_options = ['options', 'create', 'retrieve', 'update', 'delete', 'quit', 'save']

    menu = input("\nWelcome to the main menu. What would you like to do? (try 'options') > ").lower()

    if menu == 'options':

            print("\nThe commands available are: 'Create', 'Retrieve', 'Update', 'Save' or 'Delete'.")
            
            print("\nIf you would like to quit the program, you must type 'quit'.")

    if menu == 'create':
        user_values.extend(create())
        
    if menu == 'retrieve':
        retrieve()
    
    if menu == 'update':
        update()

    if menu == 'save':
        save()

    if menu == 'delete':
        delete()
    
    if menu == 'quit':
        print("\nThank you for using the program! Have a nice day!\n")
        interface_flag = False

    elif menu not in interface_options:
        print("The program doesn't seem to like that input... Let's try that again.")

# Compile all user data, change to string so csv can read
contacts_list = get_contact_list()

# String for keys
out_keys = ''
for i in range(len(keys)):
    out_keys += keys[i] + ','
out_keys = out_keys.rstrip(',')
out_keys += "\n"

# String for user data
out_data = ''
for i in range(len(contacts_list)):
    out_data += contacts_list[i]['name'] + ','
    out_data += contacts_list[i]['favorite fruit'] + ','
    out_data += contacts_list[i]['favorite color']
    out_data += "\n"

with open('contacts.csv', 'w') as contacts:
    contacts.write(out_keys)
    contacts.write(out_data)
    contacts.close()