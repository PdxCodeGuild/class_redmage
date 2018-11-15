while True:
    try:
        cred_input = input("Enter your credit card number: ")
        # print(f"The cc# you entered is: {cred_input}")
        cred_in = list(cred_input)
        cc_num = list(map(int, cred_in))
    except ValueError:
        print("Please enter a valid credit card #!")
        continue
    else:
        break

def cc_valid(credit_number):
    flag = True
    while flag:
        last_dig = credit_number[-1]
        credit_number = credit_number[:len(credit_number)-1]
        credit_number = credit_number[::-1]
        for i in range(0,len(credit_number),2):
            credit_number[i] *= 2
        for i in credit_number:
            if i > 9:
                i -= 9
        sum_val = sum(credit_number)
        sum_val_list = str(sum_val)
        sum_val_list_dig2 = sum_val_list[1]
        flag = False
    if sum_val_list_dig2 == last_dig:
        return True
    else:
        return False
        
if cc_valid(cc_num) == True:
    print("Valid!")
else:
    print("Invalid!")
