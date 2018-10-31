with open('contacts.csv', 'r') as contacts:
    lines = contacts.read().split('\n')

keys = lines[0].split(',')
user_values = [lines[i].split(',') for i in range(1, len(lines))]

def tuple_creator(user_values):
    # Original function, used list comprehension trial and error to get it on one line.
    '''
    for i in range(len(keys)):
        x = keys[i], user_values[i]
        tuple_list.append(x)
    '''
    
    tuple_list = [(keys[i], user_values[i]) for i in range(len(keys))]

    return tuple_list

def dict_creator(tuple_list): 

    dict_list = {key: value for key, value in tuple_list}
    
    return dict_list

contacts_list = [dict_creator(tuple_creator(user_values[i])) for i in range(len(user_values))]

print(f"\n{contacts_list}\n")