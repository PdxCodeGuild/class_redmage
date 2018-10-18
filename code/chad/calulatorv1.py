opperator = input('What is the operation you\'d like to perform? > ')
first_num = int(input('What is the first number? > '))
second_num = int(input('What is the second number? > '))
run = eval(first_num, opperator, second_num)

print(f'{first_num} {opperator} {second_num} equals {run}')