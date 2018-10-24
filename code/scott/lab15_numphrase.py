# lab15_numphrase.py


def conv(number):
    

    conv_dict = {
        0: ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"],
        1: ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"],
        2: "twenty",
        3: "thirty",
        4: "forty",
        5: "fifty",
        6: "sixty",
        7: "seventy",
        8: "eighty",
        9: "ninety"
    } 
    
    hundreds = number // 100
    tens = number % 100 // 10
    ones = number % 100 % 10
    ones_conv = conv_dict[0]

    new_string = ""
    if hundreds > 0:
        new_string += f"{ones_conv[hundreds]} hundred and "
    else:
        pass

    if tens == 1:
        tens_conv = conv_dict[tens]
        new_string += f"{tens_conv[ones]}"
        
        
    elif tens > 1:
        new_string += f"{conv_dict[tens]}"
        new_string += f" {ones_conv[ones]}"
    return new_string

    print(hundreds)
    print(tens)
    print(ones)


   
user_num = int(input("enter a number: "))
print(conv(user_num))
