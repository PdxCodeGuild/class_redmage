

with open('contact_list.csv', 'r+') as file:
    lines = file.read().split('\n')

my_dict = {[k:v ]}

keys = lines[0].split(',')
print(keys)
    
my_dict = {x[0]: x[1:] for x in lines}
print(my_dict)



# for i in range(1,len(lines)):