# Problem 1

'''
import random

fruits_list = ['Apple', 'Orange', 'Banana']

def randomizer():

    x = random.randint(0,2)
    y = fruits_list[x]

    return y

print(randomizer())
'''

# Problem 2
import string

def number_func():
    
    number_list = list(string.digits)
    number_tally = []
    
    main_flag = True
    while main_flag:
        
        loop_flag = False

        number_input = input("Enter a number or type 'done': > ").lower()
        
        if number_input == 'done':
            main_flag = False
            return number_tally
        
        for char in number_input:
            if char not in number_list:
                print("Needs to be a number")
                break
            else:
                loop_flag = True
                
        while loop_flag == True:
            number_input = int(number_input)
            number_tally.append(number_input)
            break
        


print(number_func())