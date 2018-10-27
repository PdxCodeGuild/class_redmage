# lab18_peakvalley.py

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
nums = data.copy()
nums.sort()
topnum = nums[-1]
print(nums)
# prints some Xs
def create_mountains():
    temp1 = []
    for i in data:
        # print(i)
        temp2 = []
        for i in range(i):
            temp2.append("X")
        # print(temp2)
        temp1.append(temp2)
    return temp1

mountains = create_mountains()

# print(mountains)
# for i in mountains:
#     print(i)

for i in mountains:
    for t in range((topnum - len(i))):
        i.append("O")
# print(mountains)
for i in mountains:
    print(i)


new_list = []
for i in mountains:
    inum = mountains.index(i)
    for t in range(len(i)):
        new_list.append(mountains[inum][t])
    
print(new_list)