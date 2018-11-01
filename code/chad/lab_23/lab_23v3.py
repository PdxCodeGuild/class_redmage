import time, string

# Contact template To Be Used For File Operations
contact_template = ('name','address','address 2','city','state','zip','phone','email')

# Final List is the list that the program runs off of, it is the current contact list util it gets saved
final_list = []

#Open File and close after saving as contact_list variable, return contact list to the call
def open_file():
    with open('contact_list.csv', 'r') as contacts:
        contact_list = contacts.read().split('\n')
    contacts.close()
    return  contact_list


#From the open file we get a contact list with a list of long string line including commas such as
#'name, address, address 2, city, state, zip, phone, email', com',.... new string
#even though there are commas seperating name, address, ect it is one string
#Need to split each element in the list of long strings a new list based on the ',' commas
def parse_file(contact_list):
    split_list = []
    for element in contact_list:
        element = split_list.append(element.split(','))


#For each element (which each element is a list of elements), itterate through top level element in the list
# and for each top level element iterate through each subelement and create a temp dictionary called start_dict,
# then append that whole dictionary to the list final_list
    for element in split_list[1:]:
        start_dict = {}
        for i in range(len(element)):
            start_dict.update(({split_list[0][i]: element[i]}))
        final_list.append(start_dict)


def save_file():
    write_list = ''
    #Write the template back to the top of the csv
    write_list += ','.join(contact_template)
    write_list += '\n'
    for element in final_list:
        element_list = element.values()
        write_list += ','.join(element_list)
        write_list += '\n'
    print(f'Here is the final list to write \n{write_list}')
    with open('contact_list.csv','w') as contacts:
        contacts.write(write_list)
    contacts.close()

def add_new_contact():
    #Decided to use a count instead of length since appending immediatly and not storing in a list to count first
    count = 0
    while True:
        ask_another = input('Would You Like To Add A New Contact?').lower()
        if ask_another in ('end', 'quit', 'q', 'exit', 'done', 'no', 'n'):
            print('You Have Finished Entering Contacts!!')
            break
            if count == 0:
                return print('You Have Not Added Any Contacts')
        else:
            add_name = input('Please Enter The Full Name Of Your Contact: > ').capitalize()
            add_address1 = input('Please Enter The First Address Line Of Your Contact: > ').capitalize()
            add_address2 = input('Please Enter The Second Address Line Of Your Contact: > ').capitalize()
            add_city = input('Please Enter The City Of Your Contact: > ').capitalize()
            add_state = input('Please Enter The State Abbreviation Of Your Contact: > ').capitalize()
            add_zip = input('Please Enter The Zip Of Your Contact: > ')
            add_phone = input('Please Enter The Phone Of Your Contact: > ')
            add_email = input('Please Enter The Email Of Your Contact: > ')
            final_list.append({contact_template[0]: add_name,
                               contact_template[1]: add_address1,
                               contact_template[2]: add_address2,
                               contact_template[3]: add_city,
                               contact_template[4]: add_state,
                               contact_template[5]: add_zip,
                               contact_template[6]: add_phone,
                               contact_template[7]: add_email
                               })
            #If else runs and user types intput increase count so begining of loop doesnt kick you out
            count += 1
    save_file()

def retrieve_contact():
    #Setup A Temporary List To Return Back To Call Once Completed
    temp_list = []
    user_input = input('\n\n\n\n\nType The Name Of The Person You Would Like To Retrieve.\n'
                       'You Can Also Choose To Type a few Characters Of A Name To Grab All \n'
                       'Names That Start With That Sequence: > ').capitalize()
    for index in final_list:
        if user_input in index['name']:
            pre_list = []
            for i in index:
                pre_list.append(index[i])
            temp_list.append(pre_list)
    if len(temp_list) == 0:
        print('There Were No Matches')
    if len(temp_list) > 0:
        return [elem for i in temp_list for elem in i]

def update_contact():
    print(print_all_contacts())
    print('\n\n\n')
    contact_input = input('Which Contact Number Would You Like To Edit? '
          'Please Give The Number Only > ')
    if contact_input in string.digits:
            print(final_list[int(contact_input)])
            update_element = input('Type Which Key You Would Like To Change The Value Of.'
                                   'Such as "name" To Change The Name')
            value_change = input('What Is The Updated Value?')
            final_list[int(contact_input)][update_element] = value_change
            print(f'\n\n\nHere Is The Changed Contact: \n {(final_list[int(contact_input)])}')
    save_file()

def delete_contact():
    print(print_all_contacts())
    print('\n\n\n')
    contact_input = int(input('Which Contact Number Would You Like To Delete? '
                          'Please Give The Number Only > '))
    if str(contact_input) in string.digits:
        print(final_list[(contact_input)])
        final_ask = input('Is This The Contact That You Would Like To Delete? Type "Y" or "Yes" To Confirm').lower()
        if final_ask in ('y', 'yes'):
            popped_contact = final_list.pop(contact_input)
            print(f'\n\nYou Deleted {popped_contact}\n From Your Contacts')
    save_file()
def print_all_contacts():
    temp_list = []
    contact_number = 0
    for element in final_list:
        print('')
        print(f'Contact Number #{contact_number}: ')
        for i in element:
            print(f'{element[i]} | ', end='')
        contact_number += 1

def menu():
    while True:
        user_input = input('\n\nWelcome To Chads Contact List Program\n'
              '\n'
              'Type the Number Below For The Function That You Would Like To Do\n'
              '\n'
              'Would You like to:\n'
              '\t 1. Create A New Contact?\n'
              '\t 2. Retrieve A Contact Record?\n'
              '\t 3. Update An Existing Record?\n'
              '\t 4. Delete A Existing Record?\n'
              '\t 5. Print All Contact Records?\n'
              '\t 6. Save and Quit Program!!!!?\n'
              "Type 'end', 'quit', 'q', 'exit', 'done' To Exit This Program")
        if user_input == '1':
            add_new_contact()
        elif user_input == '2':

            print(retrieve_contact())
        elif user_input == '3':
            update_contact()
        elif user_input == '4':
            delete_contact()
        elif user_input == '5':
            print_all_contacts()
        elif user_input == '6':
            save_file()
            quit()
        else:
            if user_input != ('1', '2', '3', '4', '5'):
                print(f'\n\n\n\nYou Typed An Invalid Number\n')
                time.sleep(3)

# Step 1 open the file, read, store in variable return and close.
contact_list = open_file()
# Step 2 parse the file into a list of dictionaries to be used by the program
contact_list = parse_file(contact_list)
# Step 3 Run the program and startup the menu
menu()






