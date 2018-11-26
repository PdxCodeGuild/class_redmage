# Problem #1
def combine(a, b):
    my_dict = {a[x]: b[x] for x in range(len(a))}
    return my_dict

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
# combine(fruits, prices) -> {'apple':1.2, 'banana':3.3, 'pear':2.1}

print(combine(fruits,prices))

# Problem #2
def average(d):
    ave_price = (sum(d.values()))/len(d)
    return ave_price

# average(combined) -> 2.2

print(round(average(combine(fruits,prices)),2))

# Problem #3
d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

def unify(my_dict):

    new_dict = {}
# for the key (variable) in my dict
    for key in my_dict:
        if key[0] in new_dict:
            new_dict[key[0]].append(my_dict[key])
        else:
            new_dict[key[0]] = [my_dict[key]]
    
    new_dict = {k:round((sum(v)/len(v)),2) for k,v in new_dict.items()}
    
    return new_dict

print(unify(d))