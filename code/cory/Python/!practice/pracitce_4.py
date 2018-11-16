# Problem 1
# Given a the two lists below, combine them into a dictionary.
# -> {'apple':1.2, 'banana':3.3, 'pear':2.1}
'''
def combine(a, b):

    new_dict = {a[i]: b[i] for i in range(len(a))}
    return new_dict

fruits = ['apple', 'banana', 'pear']
prices = [1.2, 3.3, 2.1]
print(combine(fruits, prices))
'''

# Problem 2
# Using the result from the previous problem, iterate through the dictionary and calculate the average price of an item.
'''
def average(d):

    new_list = []
    for key in d:
        new_list.append(d[key])

    avg = 0
    for num in new_list:
        avg += num

    # print(avg)
    avg = round(avg / len(new_list), 2)
    # print(avg)
    return avg

combined = {'apple':1.2, 'banana':3.3, 'pear':2.1}
print(average(combined))
'''

# Problem 3
# Average numbers whose keys start with the same letter. Output a dictionary containing those letters as keys and the averages.

def unify(d):
   
    def key_func_avg(startswith):
        out_list = []

        for key in d:
            if key.startswith(startswith):
                out_list.append(d[key])
        
        out_list = round(sum(out_list) / len(out_list))

        return out_list

    a_avg = key_func_avg('a')
    b_avg = key_func_avg('b')
    c_avg = key_func_avg('c')

    new_dict = {'a': a_avg, 'b': b_avg, 'c': c_avg}

    return new_dict

d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}

print(unify(d))