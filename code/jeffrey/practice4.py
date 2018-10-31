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
# unify(d) -> {'a':3, 'b':4, 'c':5}

def unify(x):
    new_dict = {sum(x.values())/len(x.values)}
    
    # for keys,values in x if (x.keys())[i][0] == (x.keys())[i][0]}
    return new_dict

print(unify(d))
