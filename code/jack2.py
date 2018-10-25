import random

sex_list = ['male', 'female']

#jack_list_template = [{'name':'jack', 'age':0, 'sex:'m', 'preg':False}]
jack_list = [{'name': 'adam', 'age': 0, 'sex': 'male', 'preg': 0}, {'name': 'eve', 'age': 0, 'sex': 'female', 'preg': 0}]

def create_new_jack():
    jack_list = {'name': 'jack', 'age': 0, 'sex': random.choice(sex_list), 'preg': 0}
    return jack_list

def preg_funck(i):
    if jack_list[i]['sex'] == 'female':
        if jack_list[i]['age'] in range(4,9) and jack_list[i]['preg'] == 0 or 1:
            if jack_list[i] != jack_list[0]:
                if jack_list[i-1]['sex'] == 'male' and jack_list[i-1]['age'] in range(4,9):
                    return True
                # Had lint say 'break not used properly in loop', changed to 'pass'
                else:
                    pass
                    # break
            if jack_list[i] != jack_list[len(jack_list) - 1]:
                if jack_list[i+1]['sex'] == 'male' and jack_list[i+1]['age'] in range(4,9):
                    return True
    
year = 0   

while year <= 6:
    # for i in range(len(jack_list)):
    #     jack_list[i]['preg'] = False

    for i in range(len(jack_list)):
        
        jack_list[i]['age'] += 1

        if preg_funck(i):
            
            jack_list[i]['preg'] += 1

            if jack_list[i]['preg'] == 2:
                
                jack_list.append(create_new_jack())
                jack_list[i]['preg'] = 0

    # random.shuffle(jack_list)

    year += 1

    print(jack_list)

