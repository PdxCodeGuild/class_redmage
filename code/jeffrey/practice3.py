import random

# Prolem #1
fruits = ['apples', 'bananas', 'pears']

def func1(list_in):
    x = random.randint(0,(len(list_in))-1)
    selection = list_in[x]
    return selection

print(func1(fruits))

# Problem #2
def repl_func():
    flag = True
    my_list = []
    while flag:
        user_in = input("Enter a number (or 'done'): ")
        if user_in == "done":
            flag = False
        else:
            my_list.append(user_in)
    return my_list

print(repl_func())

# Problem #3
nums = [4,5,6,7,8]

def eveneven(x):
    n = [i%2 for i in x if i%2 == False]
    if len(n)%2 == 0:
        return True
    else:
        return False

print(eveneven(nums))

# Problem #4
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_every_other(x):
    pikachu = []
    i = 0
    while i <= len(x):
        pikachu.append(x[i:i+1:2])
        i +=1
    return pikachu

print(print_every_other(nums))

# ^^^ fix this
    