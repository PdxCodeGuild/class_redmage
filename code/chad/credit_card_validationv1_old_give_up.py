import random

#ask the user to enter a 16 digit number
user_number = 4565454345678765 #input('Input a 16 Digit Number')

#function to double ever other number



def check_number(user_number):
    #make numbers into a list to be able to manipulate
    user_number = list(str(user_number))
    print(user_number)
    #poping the last digit off and storing it for later as check value
    popped_numer = user_number.pop(-1)
    print(user_number)
    user_number.reverse()
    print(user_number)
    user_number = double_num(user_number)
    print(user_number)
    ######
    user_list = []
    print(type(user_number))
    for num in user_number:
        user_list.append(int(num))
   

    print(type(user_list[0]))
    print(user_list)
    user_list2 = []
    for num in user_list:
        if num % 2 == 0:
            user_list2.append(num*2)
        else:
            user_list2.append(num)
    print(user_list2)
    user_list2 = sum(user_list2)
    print(user_list2)
    print((user_list2 % 10) == popped_numer)
       
    

#check to see if the number is valid
if len(str(user_number)) == 16:
    print(f' Your Credit Card {user_number} Validated!')
    check_number(user_number)

else:
    print('You Entered A Invalid Card Number')
    
