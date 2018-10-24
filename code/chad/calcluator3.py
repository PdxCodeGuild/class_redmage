import ast

istrue = True
while istrue:
    opperator = input('Type In a Math Expression To Evaluate')
    math_calc = eval(opperator)
    print(math_calc)
    again = int(input('Do Another Calculation? Type "1" for yes and another other key for no'))
    if again == 1:
        continue
    else:
        istrue = False
