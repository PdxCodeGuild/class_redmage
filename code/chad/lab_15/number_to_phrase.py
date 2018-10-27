'''
Convert a given number into its english representation. 
For example: 67 becomes 'sixty-seven'. Handle numbers from 0-99.

Hint: you can use modulus to extract the ones and tens digit.
'''
word_to_number = int(input('What Number Would You Like To Convert Into Words'))

def convert(word_to_number):

    dict_lookup_hundreds = {0:'', 1:'one hundred', 2:'two hundred', 3:'three hundred', 4:'four hundred', 
    5:'five hundred', 6:'six hundred', 7:'sev hundred', 8:'eight hundred', 9:'nine hundred'}

    dict_lookup_tens = {0:'', 1:'one', 2:'twenty', 3:'thrirty', 4:'fourty', 5:'fifty', 
    6:'sixty', 7:'seventy', 8:'eighty', 9:'ninty'}

    dict_lookup_ones = {0:'', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',
    8:'eight', 9:'nine'}

    dict_lookup_teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
    16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'ninteen'}
# Evaluate if the number has a floor division of 100, if so process in this if statement
    if word_to_number // 100 != 0:
        ones_digit = word_to_number % 10
        tens_digit = (word_to_number % 100) // 10
        hundreds_digit = word_to_number // 100
# Evaluate if the number has is a teen number, if so process in this if statement
    if word_to_number in dict_lookup_teens:
        return dict_lookup_teens[word_to_number]
# Evaluate if the number is >=, if so process in this if statement
    if word_to_number < 100 and word_to_number >= 20:
        ones_digit = word_to_number % 10
        tens_digit = word_to_number // 10
        hundreds_digit = word_to_number // 100
# Conver to word
    ones_converted = dict_lookup_ones[ones_digit]
    tens_converted = dict_lookup_tens[tens_digit]
    hundreds_digit = dict_lookup_hundreds[hundreds_digit]
    converted = hundreds_digit, tens_converted, ones_converted
    print(converted)
    return converted
    
    
#Call and print the converted numbers to words
converted = convert(word_to_number)
if word_to_number < 20 and word_to_number > 10:
    print(converted)
else:
    print(f'{converted[0]} {converted[1]} {converted[2]}')


