print('\n#1\n')
def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False

x=6
print(f'{x} is even: {is_even(x)}')
x=7
print(f'{x} is even: {is_even(x)}')

print('\n#2\n')
def both_not_even(x,y):
    if x%2 == 0 and y%2 == 1:
        return True
    elif x%2 == 1 and y%2 ==0:
        return True
    else:
        return False

x=20
y=5

print(both_not_even(x,y))
x=5
y=6
print(both_not_even(x,y))
x = 5
y = 5
print(both_not_even(x,y))

print('\n#3\n')
def num_range_check(x):
    if 9 < int(x) <=100:
        return True
    else:
        return False

x = input("input a number: ")

print(f'Your number is between 10 and 100: {num_range_check(x)}')

print('\n#4\n')
def max_of_three(a,b,c):
    my_list = sorted([a,b,c])
    return my_list[-1]

a =10
b = 50
c = 15

print(f'the max number of the three is: {max_of_three(a,b,c)}')



print('\n#5\n')
def two_powers(x):
    i = 0
    my_list = []
    while i <=20:
        my_list.append(str(x**i))
        i+=1
    my_list = ','.join(my_list)
    return my_list
x = 2

print(two_powers(x))