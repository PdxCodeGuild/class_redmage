# Version 1

# Create list for first digit, and another for second digit (ten, twenty, thirty), (one, two, three)
def conversion(number):

    hundreds_list = ['', 'One Hundred', 'Two Hundred', 'Three Hundred', 'Four Hundred', 'Five Hundred', 'Six Hundred', 'Seven Hundred', 'Eight Hundred', 'Nine Hundred']
    tens_list = ['', 'Ten', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Nienty']
    ones_list = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    teens_list = ['', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    hundreds_digit = number // 100

    # Set number so floor div and mod have a 0 - 9 number for index's 
    number -= (number // 100) * 100

    tens_digit = number // 10
    ones_digit = number % 10

    # If number is a teen number:
    if number >= 11 and number <= 19:
        return ' '.join([hundreds_list[hundreds_digit], teens_list[ones_digit]])
    # If number ends in a whole tens number (ex 150)
    if ones_digit == 0:
        return ' '.join([hundreds_list[hundreds_digit], tens_list[tens_digit]])
    # If number ends in less than 10 (ex 909)
    if number < 10:
        return ' '.join([hundreds_list[hundreds_digit], ones_list[ones_digit]])
    # Else number is above 20, plus the hundreds spot
    return ' '.join([hundreds_list[hundreds_digit], tens_list[tens_digit], ones_list[ones_digit]])

    # Ask for user input

end_flag = False

while end_flag == False:
    number = int(input("What number would you like to convert to english? (0 to 99)> "))
    print(f"The number you chose was {conversion(number)}")

    loop_flag = True
    while loop_flag:
        end_inp = ''
        while end_inp != 'y' and end_inp != 'n':
            end_inp = input('Would you like to run this again? (y/n) > ').lower()
            print("You need to type either 'y' or 'n'")
        if end_inp == 'n':
            print("You're all done!")
            end_flag == True
            loop_flag == False
            break
        else:
            loop_flag == False
            break
