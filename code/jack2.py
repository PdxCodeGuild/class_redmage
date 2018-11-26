import random

sex_list = ['male', 'female']

#jack_list_template = [{'name':'jack', 'age':0, 'sex:'m', 'preg':False}]
jack_list = [{'name': 'adam', 'age': 0, 'sex': 'male', 'preg': 0}, {'name': 'eve', 'age': 0, 'sex': 'female', 'preg': 0}, {'name': 'adam2', 'age': 0, 'sex': 'male', 'preg': 0}, {'name': 'eve2', 'age': 0, 'sex': 'female', 'preg': 0}]

def create_new_jack():
    jack_list = {'name': 'jack', 'age': 0, 'sex': random.choice(sex_list), 'preg': 0}
    return jack_list

def preg_funck(i):
    if jack_list[i]['sex'] == 'female':
        if jack_list[i]['age'] in range(4,9) and jack_list[i]['preg'] == 0 or 1:
            if jack_list[i] != jack_list[0]:
                if jack_list[i-1]['sex'] == 'male' and jack_list[i-1]['age'] in range(4,9):
                    return True

            if jack_list[i] != jack_list[len(jack_list) - 1]:
                if jack_list[i+1]['sex'] == 'male' and jack_list[i+1]['age'] in range(4,9):
                    return True

            return False

        return False

    return False

year = 0   

while len(jack_list) > 0:
   
    for i in range(len(jack_list)):

        jack_list[i]['age'] += 1
        
        if preg_funck(i):
        
            jack_list[i]['preg'] += 1
        
            if jack_list[i]['preg'] == 2:
        
                jack_list.append(create_new_jack())
                jack_list[i]['preg'] = 0

    new_list = sorted(jack_list, key=lambda k: k['age']) 

    for i in range((len(new_list) - 1), -1 , -1):

        if new_list[i]['age'] == 10:
            new_list.remove(new_list[i])

    jack_list = new_list
    random.shuffle(jack_list)
    year += 1

    # print(len(jack_list))
    # print(year)
    # print('\n')
    print(f"Year {year}, {len(jack_list)} is population.")