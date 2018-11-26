numbers = []


while True:
    number = input('Give me a number to average or type "done" to quit? > ')
    if number == 'done':
        length = len(numbers)
        print(f'The Average For Your {length} Amount Of Numbers is {sum(numbers) / length} ')
        break
    else:
        number = int(number)
        numbers.append(number)
        print(numbers)


