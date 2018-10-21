nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# for num in nums:
#     print(num)

math = 0

# loop over the indices
for i in range(len(nums)):
    math += nums[i]
    
    # print(nums[i])
print(round(math/len(nums),2))

# Version 2

nums1 = []

u_nums = (input("Enter an integer, or 'done': "))

math2 = 0

while u_nums != "done":
    nums1.append(u_nums)
    u_nums = (input("Enter an integer, or 'done': "))

for i in range(len(nums1)):
    math2 += int(nums1[i])

print("For your "+ str(len(nums1))+" numbers the average is "+str(round(math2/len(nums1),2)))