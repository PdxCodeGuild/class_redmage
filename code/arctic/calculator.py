#calculator.py
print("This is a simple calculator.")
while True:
    operation = " "
    operation = input("What operation would you like to perform? > Please choose between '+', '-', '*', '/' ")
    while operation not in ['+','-', '*', '/']:
        print("invalid, please try again")
        operation = input("What operation would you like to perform? > Please choose between '+', '-', '*', '/' ") 
    operation in ['+', '-', '*', '/']
    num1 = float(input("What is the first number? >"))
    num2 = float(input("What is the second number? >")) 
            
    if operation == "+":
        print (num1 + num2)
    elif operation == "-":
        print (num1 - num2)
    elif operation == "*":
        print (num1 * num2)
    elif operation == "/":
        print (num1 / num2)
    else:
        pass
    # while end != 'y' or  end != 'n':
        # This loop will ensure you choose y or n
    # print("You must choose either y or n to continue!")
    end = input("Would you like to continue? > (y/n)") 
    if end == 'y':
        continue
    elif end == 'n':
        print("Thank you" + ',' + "goodbye " + '!' )
        break