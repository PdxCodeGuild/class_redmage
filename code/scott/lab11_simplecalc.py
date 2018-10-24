# lab11_simplecalc.py

# introducing
print("This is a simple calculator. Type done at any prompt to exit.")



# placing the non-quittable version in a while loop to allow the user to exit.
# while True:
#     # these lines (minus the done/break lines) were version 1 
#     while operation == "":
#         operation = input("What operation would you like to perform? (+, -, *, /) ")
#     if operation == "done":
#         break

#     while operand == "":
#         operand = input("What is the first number? ")
#     if operand == "done":
#         break

#     while operator == "":
#         operator = input("What is the second number? ")
#     if operator == "done":
#         break
#     break

# maths = operand + operation + operator
# if "done" in maths:
#     quit()

maths_prob = ""
while maths_prob == "":
    maths_prob = input("Enter a math problem to solve. (format: '# + #')(function's available are: +, -, *, /) ")
    if maths_prob == "done":
        break
if maths_prob == "done":
    sys.exit

maths_result = eval(maths_prob)

print(f"{maths_prob} equals {maths_result}")
