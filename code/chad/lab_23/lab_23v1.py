#Open File and close after saving as contact_list
with open('/home/chad/Documents/git_hub/class_redmage/code/chad/lab_23/contact_list.csv', 'r') as contacts:
    contact_list = contacts.read()
contacts.close()

new_list = {}





print(contact_list)
print(new_list)
#contact_list = contact_list.split(',')
#contact_dict = {name:contact_list[] for name, address, address2, city, state, zip, phone, email in contact_list}
#contact_dict = {contact[x]:}



