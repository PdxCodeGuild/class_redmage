data = [1, 2, 3, 4, 5, 4, 3, 2, 3, 4]
new_set = ['xx', 'xxx', 'xxxx', 'xxxxx', 'xxxx', 'xxxxx', 'xxxx', 'xxx', 'xxxx', 'xxxxx']
print(len(new_set))
for i in data:
    new_set.append(data[i]*'x')

#for num in range(len(new_set)):
for x in new_set:
    print(x+',\t',sep='', end='')



import string
string.ascii_lette