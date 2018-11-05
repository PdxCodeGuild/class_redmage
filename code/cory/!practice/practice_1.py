# Problem 1
'''
def is_even(num1):
    return num1 % 2
while True: 
    x = is_even(int(input("Type a number > ")))
    print(x)
    if x == 0:
        print('The number is even!')
    else:
        print('The number is odd!')
'''

# Problem 2
'''
def opp_var(num1, num2):
    if num1 > 0 and num2 < 0:
        return True
    elif num1 < 0 and num2 > 0:
        return True
    else:
        return False
while True:
    x = opp_var(int(input("Choose a number > ")), int(input("Choose a second number number > ")))

    print(x)
'''

# Problem 3
'''
def near_100(num1):
    if num1 in range(90,101):
        return True
    else:
        return False
while True:
    x = near_100(int(input("Choose a number: > ")))
    print(x)
'''

# Problem 4
'''
def max_of_three(num1, num2, num3):
    return max(num1, num2, num3)

while True:
    x = max_of_three(
        int(input("Choose the first number: > ")),
        int(input("Choose the second number: > ")),
        int(input("Choose the third number: > "))
    )

    print(x)
'''

# Problem 5

def expo(base, repeat):
    counter = 0
    for x in range(repeat):
        counter += 1
        # print(counter)
        print(base ** x)
    return 'You\'re done!'

print(expo(2, 20))

# print(expo(
#     int(input("Choose the base number: > ")),
#     int(input("Choose the repeat number: > ")),
# ))

