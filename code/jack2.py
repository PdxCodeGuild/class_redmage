import random

sex_list = ['male', 'female']

#jack_list_template = [{'name':'jack', 'age':0, 'sex:'m', 'preg':False}]
jack_list = []
#
def create_new_jack():
    jack_list = [{'name':'jack'+str(random.randint(0,100)), 'age':0, 'sex':random.choice(sex_list), 'preg':False}]
    return jack_list
def preg_funck(i):
    if jack_list[i]['sex'] == 'female':
        if jack_list[i]['age'] in range(4,9) and jack_list[i]['preg'] == False:
            if jack_list[i] != jack_list[0]:
                if jack_list[i-1]['sex'] == 'male' and jack_list[i-1]['age'] in range(4,9):
                    return True
                else:
                    break
            if jack_list[i] != len(jack_list-1):
                if jack_list[i+1]['sex'] == 'male' and jack_list[i+1]['age'] in range(4,9):
                    return True
    
def do_loop():
    for i in len(jack_list):
        #Calls preg_func function above
        if preg_funck(i) is True:

            






#Step 1 call function to create a new jack 
jack_list.append(create_new_jack())
print(jack_list)
#Step 2 is Create The Loop
do_loop()
