

istrue = True
while istrue:
    opperator = input('What is the operation you\'d like to perform? > ')
    first_num = int(input('What is the first number? > '))
    second_num = int(input('What is the second number? > '))
    if opperator == '+':
        print(f'{first_num + second_num}')
    elif opperator == '-':
        print(f'{first_num - second_num}')
    elif opperator == '*':
        print(f'{first_num * second_num}')
    elif opperator == '/':
        print(f'{first_num / second_num}')
    again = int(input('Do Another Calculation? Type "1" for yes and another other key for no'))
    if again == 1:
        continue
    else:
        istrue = False
