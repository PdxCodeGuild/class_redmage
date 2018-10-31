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