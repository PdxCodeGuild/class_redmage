# lab20_ccval.py

cred_card = input("Please enter a 16 digit credit card number for validation. ")

def cc_valid(cc_num):
    # getting input and priming
    cc = []
    # iterating through each integer and adding it to the list
    for i in cc_num:
        i = int(i)
        cc.append(i)
    # popping the last digit of the CC number (the check digit)
    check_digit = cc.pop(-1)
    # reversing the list
    cc.reverse()
    # doubling every other number
    for i in cc[::2]:
        i *= 2
        if i > 9:
            i -= 9
    # back to string to check the second digit
    cc = str(sum(cc))
    if int(cc[1]) == int(check_digit):
        v = True
        print("This card checks out.")
    else:
        v = False
        print("Invalid card")
    return v

valid = cc_valid(cred_card)