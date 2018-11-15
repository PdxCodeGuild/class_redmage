card_number_in = input('What is the credit card number that you would like to evaluate? > ')

if len(card_number_in) != 16:
    print('You Entered a invalid amount of numbers or characters')
    quit()

def convert_string(a):
    print(a)
    x = list(a)
    for i in range(len(a)):
        x[i] = int(a[i])
    return x

def double_element(b):
    tempList = []
    for i in range(0, len(b)):
        if i % 2 == 0:
            tempList.append(b[i] * 2)

        else:
            tempList.append(b[i])
    return tempList

def find_second_digit(c):
    into_list = list(str(c))
    out_list = int(into_list[1])
    return out_list


# Calling Function convert_string(card_number_in) to conver string to integer
converted_card_intList = convert_string(card_number_in)
print(f'Converted Card Numbers Into Integers {converted_card_intList}')
#slice off last number and store it into a vairable
popoff1 = converted_card_intList.pop(-1)
print(f'You popped off number {popoff1}')
#Reversing the digists of list in place
converted_card_intList.reverse()
print(f'Reversed The Card Numbers {converted_card_intList}')
#Calling Function To Double Ever Other Element in List
double_list = double_element(converted_card_intList)
print(f'Doubled The List Every Other Index {double_list}')
#Sum all the digits in the list
sum_list = sum(double_list)
print(sum_list)
#Call function to find second digit
found_second_digit = find_second_digit(sum_list)
print(f'The Second Digit In the number is {found_second_digit}')
#print evaluation to find if True or False
print(popoff1 == found_second_digit)