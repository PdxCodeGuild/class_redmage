# x = 67
# tens_digit = x//10
# ones_digit = x%10

# print(tens_digit)
# print(ones_digit)

numbers = ("zero","one","two","three","four","five","six","seven","eight","nine")
tens_names = ("ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen")
bigger_ten_names = ("","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety")
hundred_names = ("","one-hundred", "two-hundred","three-hundred","four-hundred","five-hundred","six-hundred","seven-hundred","eight-hundred","nine-hundred")

numbers = {v: k for v,k in enumerate(numbers)}
tens_names = {v: k for v,k in enumerate(tens_names)}
bigger_ten_names = {v: k for v,k in enumerate(bigger_ten_names)}
hundred_names = {v: k for v,k in enumerate(hundred_names)}
# print(hundred_names)
# print(numbers)

def magic(x):
    return numbers[x]

def tens_magic(x):
    return tens_names[x]

def bigger_ten_magic(x):
    return bigger_ten_names[x]

def hundred_names_magic(x):
    return hundred_names[x]

def tens_digit(x):
    if x > 99:
        return int((x/10)%10)
    else:
        return x//10

def ones_digit(x):
    return x%10

def hundred_digit(x):
    return (x//100)%10

x = int(input("Enter a number to receive the word version [range 0-99]: \n"))

gramma = int(hundred_digit(x))
mom = int(tens_digit(x))
dad = int(ones_digit(x))

# print(gramma)
# print(mom)
# print(dad)

if hundred_digit(x) >= 1 and tens_digit(x) > 1:
    print(hundred_names_magic(gramma)+" "+bigger_ten_magic(mom)+"-"+magic(dad))
elif hundred_digit(x) >=1 and tens_digit(x) == 1:
    print(hundred_names_magic(gramma)+" "+tens_magic(dad))
elif hundred_digit(x) >=1 and tens_digit(x) < 1:
    print(hundred_names_magic(gramma)+" "+magic(dad))
elif tens_digit(x) < 1:
    print(magic(dad))
elif tens_digit(x) == 1:
    print(tens_magic(dad))
elif tens_digit(x) > 1:
    print(bigger_ten_magic(mom)+"-"+magic(dad))
else:
    print("Houston we have a problem!")