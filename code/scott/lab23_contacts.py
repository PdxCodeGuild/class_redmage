# lab23_contacts.py

# Version 1
with open('contacts.csv', 'r') as file:
    lines = file.read().splitlines() # parses the doc by lines with each line being a comma-separated string
lines = [line.split(",") for line in lines] # parses lines into lists by comma
# iterates through contact entries, adds them as a dict to a master contacts list
contacts = [ {
    lines[0][0]: lines[i][0],
    lines[0][1]: lines[i][1],
    lines[0][2]: lines[i][2]} for i in range(1, len(lines)) ]


# Version 2
# function to return a formatted entry - can be called by create or edit functions
def create_contact(contacts):
    """
    HowToCall: contacts = create_contact(contacts)
    Pass this function the primary contacts list.\n  it will walk the user through creating a new contact and return the appended contacts list 
    """
    while True:
        input_name = input("Please enter the name of the contact to create. ")
        fav_color = input("Enter the favorite color. ")
        fav_fruit = input("Enter the favorite fruit. ")
        create_conf = input(f"Your entry shows {input_name} loves {fav_fruit} and the color {fav_color}. Correct('Y' or 'N')? ")
        if create_conf.upper() == "Y":
            contact = {
                "name": input_name,
                "favorite color": fav_color,
                "favorite fruit": fav_fruit
            }
            contacts.append(contact)
            return contacts
        elif create_conf.upper() == "N":
            return contacts


# function to find a contact entry by name and return that entry's dictionary
def find_contact(contacts):
    """
    HowToCall: contact, index_num = find_contact(contacts)
    Pass this function the main contacts list.\nIt prompts the user to enter a name to search, then returns the dictionary and its index
    """
    contact = ""
    while contact == "":
        input_name = input("Enter the name of the contact you wish to find. ")
        try:
            index_num = [i if input_name in contacts[i]["name"] else "" for i in range(len(contacts))]
            index_num = index_num[0]
            contact = contacts[index_num]
            input_name = contact["name"]
            fav_color = contact["favorite color"]
            fav_fruit = contact["favorite fruit"]
            print(f"An entry was found for {input_name} who loves {fav_fruit} and the color {fav_color}")
            modify = input("would you like to modify this entry('Y' or 'N')? ")
            if modify.upper() == "Y":
                contacts = edit_contact(contacts, index_num)
            else:
                break
        except TypeError:
            print("No entry was found under that name.")
    return contact, index_num

# contact, index_num = find_contact(contacts)
# print(contact)
# print(index_num)

def edit_contact(contacts, index_num):
    """
    HowToCall: contacts = edit_contact(contacts)
    Returns: contacts
    This function requires you to pass it the found contact and index number.\nIt will call the find_contact function, use the returned library to walk the user through changes, and use the returned index to modify the contacts list.\nModified contacts list is returned
    """
    contact = contacts[index_num]
    old_contact = contacts[index_num].copy()
    old_name = old_contact["name"]
    old_color = old_contact["favorite color"]
    old_fruit = old_contact["favorite fruit"]
    input_name = contact["name"]
    fav_color = contact["favorite color"]
    fav_fruit = contact["favorite fruit"]
    while True:
        change_opt = input(f"Entry found for {input_name} who loves {fav_fruit} and the color {fav_color}. Would you like to modify this entry? Enter 'Y' to edit, 'D' to delete, or 'N' to abort. ")
        if change_opt.upper() == "Y":
            change_cat = input(f"{input_name} loves {fav_fruit} and the color {fav_color}. Enter 'name', 'fruit' or 'color' to change a category, or 'cancel' to abort editing.")
            if change_cat.upper() == "CANCEL":
                break
            elif change_cat.upper() == "NAME":
                new_name = input("Enter the new name for this entry. ")
                name_conf = input(f"Set the name to {new_name}('Y' or 'N')? ")
                if name_conf.upper() == "Y":
                    input_name = new_name
                    continue
            elif change_cat.upper() == "FRUIT":
                new_fruit = input("Enter the new favorite fruit for this entry. ")
                fruit_conf = input(f"Set favorite fruit to {new_fruit}('Y' or 'N')? ")
                if fruit_conf.upper() == "Y":
                    fav_fruit = new_fruit
                    continue
            elif change_cat.upper() == "COLOR":
                new_color = input("Enter the new favorite color for this entry. ")
                color_conf = input(f"Set favorite color to {new_color}('Y' or 'N')? ")
                if color_conf.upper() == "Y":
                    fav_color = new_color
                    continue
            else:
                break
            
            change_conf = input(f"This entry was for {old_name} who loved {old_fruit} and the color {old_color}.\n Would you like to change this to show {input_name} loves {fav_fruit} and the color {fav_color}('Y' or 'N')? ")
            if change_conf.upper() == "Y":
                contact["name"] = input_name
                contact["favorite fruit"] = fav_fruit
                contact["favorite color"] = fav_color
                contacts[index_num] = contact
                return contacts
            else:
                break
        elif change_opt.upper() == "D":
            contacts = delete_contact(contacts, index_num)
        else:
            break

def delete_contact(contacts, index_num):
    """
    HowToCall: contacts = delete_contact(contacts, index_num)
    Pass this function the master contacts list and the index number you wish to delete.
    Returns contacts
    """
    contacts.pop(index_num)
    return contacts

def save_contacts(contacts):
    """
    HowToCall: save_contacts(contacts)
    This function converts the list of dictionaries into a csv format.
    """
    user_info = "name, favorite fruit, favorite color\n"
    for i in range(len(contacts)):
            name = contacts[i]["name"]
            fav_fruit = contacts[i]["favorite fruit"]
            fav_color = contacts[i]["favorite color"]
            user_info = user_info + f"{name}, {fav_fruit}, {fav_color}\n"
    with open('contacts.csv', 'w') as file:
        file.write(user_info)

while True:
    main_choice = input("Welcome to the main menu of your contact list of people and their favorite color/fruit, for whatever reason.\nEnter 'find' to view or modify a contact, 'new' to enter a new contact, 'save' to save changes made, or 'quit' to quit.")
    if main_choice.upper() == "FIND":
        contact, index_num = find_contact(contacts)
    elif main_choice.upper() == "NEW":
        contacts = create_contact(contacts)
    elif main_choice.upper() == "QUIT":
        break
    elif main_choice.upper() == "SAVE":
        save_contacts(contacts)
        break