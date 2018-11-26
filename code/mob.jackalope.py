#  Version 1

import random

yr_num = 0

def new_jacque_city():
    return "\nWelcome to New Jacque City! A loving town.\n"
    
def aging_growing_jack(jack_list):
    for jack in range(len(jack_list)):
        jack_list[jack] += 1
        if jack_list[jack] in range(4,9):
            jack_list.append(0)
        if jack_list[jack] == 10:
            jack_list.pop(jack)

    # print(jack_list)    
    return jack_list

jack_pop = [0,0]

while len(jack_pop) <= 1000:
    jack_pop = aging_growing_jack(jack_pop)
    yr_num += 1
    # print(yr_num)    
print(new_jacque_city())
print(f"""
{yr_num} years for the population of New Jacque City to reach 1000. 
\n\nMerritt is eternally not permitted to enter the city limits.""")