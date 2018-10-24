# # test
# from turtle import *
# i = 0
# while i < 4:
#     forward(100)
#     left(90)
#     i = i + 1
# speed(5)
# penup()
# forward(50)
# right(90)
# pendown()
# forward(50)
# right(90)
# forward(75)
# x = 0
# while x < 3:
#     left(90)
#     forward(150)
#     x = x +1
# left(90)
# forward(75)
# penup()
# forward(75)
# left(45)
# pendown()
# forward(150)
# penup()
# left(135)
# forward(361)
# pendown()
# left(135)
# forward(150)
# penup()
# left(135)
# forward(150)
# pendown()
# left(45)
# forward(250)
# penup()
# right(135)
# forward(325)
# right(90)
# forward(176)
# pendown()
# left(135)
# forward(250)

# done()

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