# Problem #1
def comp1():
    gen = [2**x for x in range(10)]
    return gen

print(comp1())

# Problem #2
def comp2():
    jen = [((i+1)*2) for i in range(10)]
    return jen

print(comp2())

# Problem #3
old_dict = {'a': 1, 'b': 2}

def comp3(x):
    new_dict = {v: k for k, v in x.items()}
    return new_dict

print(comp3(old_dict))

# Problem #4
import string
def func1():
    my_dict = {x:ord(x) for x in string.ascii_lowercase}
    return my_dict

print(func1())