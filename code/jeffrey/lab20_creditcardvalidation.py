while True:
    try:
        cred_input = input("Enter your credit card number: ")
        cred_input = list(cred_input)
        cc_num = list(map(int, cred_input))
    except ValueError:
        print("Please enter a valid credit card #!")
        continue
    else:
        break

while True:
    last_dig = cc_num[-1]

    cc_num = cc_num[:len(cc_num)-1]

    cc_num = cc_num[::-1]

    for i in cc_num(range(0,len(cc_num-1),2)):
        i*=2
    #need to do the double every other here.
    # either use a range and then only double on the "i"s or index's from the range that I created, can use range parameters
    # or use enumerate and then the % to see if the number is divisible by 2
    
