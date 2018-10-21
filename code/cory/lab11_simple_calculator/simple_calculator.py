# Version 2

import string
num_permission = list(string.digits)
opr_list = ['+', '-', '*', '/']

# Setting up main program loop permission
end = False
while end == False:

    # Ask for the Operation
    true_permission = True
    while true_permission:
        opr_input = input('What is the operation you would like to preform? (type \'done\' to quit) > ').lower()
        if opr_input == 'done':
            true_permission = False
            break
        for x in opr_input:
            if len(opr_input) >= 2:
                print("The program didn't like that input... Let's try again.")
                break
            while x not in opr_list:
                print('You need to choose an operation! (+, -, *, /)')
                break
            else:
                true_permission = False
    if opr_input == 'done':
        print('\nThanks for using the program!\n')
        end == True
        break

    # Ask for the first number
    true_permission = True
    while true_permission:
        first_num = input('What is the first number? > ')
        for x in first_num:
            while x not in num_permission:
                print('You need to enter a number!')
                break
            else:
                true_permission = False
    first_num = int(first_num)

    # Ask for the second number
    true_permission = True
    while true_permission:
        second_num = input('What is the second number? > ')
        for x in second_num:
            while x not in num_permission:
                print('You need to enter a number!')
                break
            else:
                true_permission = False
    second_num = int(second_num)

    # Calculation Function
    def calculation(first_num, second_num):
        if opr_input == '+':
            return first_num + second_num
        elif opr_input == '-':
            return first_num - second_num
        elif opr_input == '*':
            return first_num * second_num
        elif opr_input == '/':
            return first_num / second_num

    # Calculation string
    print(f'{first_num} {opr_input} {second_num} is {round(calculation(first_num, second_num), 4)} ')   