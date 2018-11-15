result = 0

operators = ["+","-","*","/"]

while True:
    oper = input("what operation would you like to perform [+,-,*,/] or 'done'?: ")
    if oper == "done":
        break
    elif oper not in operators:
        print("Enter a correct operator character.")

    opera1 = input("1st number to operate on: ")
    opera2 = input("2nd number to operate on: ")
        
    if oper == "+":
        result = float(opera1) + float(opera2)
    elif oper == "-":
        result = float(opera1) - float(opera2)
    elif oper == "*":
        result = float(opera1) * float(opera2)
    elif oper == "/":
        result = float(opera1) / float(opera2)
    else:
        print("Try again later.")
    print(f"{opera1} {oper} {opera2} = {(round(result,2))}")

print("Thanks for math.")
    

