
num = float(input("Give a Number To Convert Quarters, Nickles, and Dimes"))


def calculate(num):
    quarters = num // .25
    left = (num - (num // .25) * .25)
    dimes = left // .10
    left = (left - (left // .10) * .10)
    nickles = left // .05
    left = (left - (left // .05) * .05)
    pennies = left // .01
    num = [quarters, dimes, nickles, pennies]
    return num

result = calculate(num)

print(f'You Have {result[0]} Quarters\n'
      f'You Have {result[1]} Dimes\n'
      f'You have {result[2]} Nickles\n'
      f'You have {result[3]} Pennies'
      )

