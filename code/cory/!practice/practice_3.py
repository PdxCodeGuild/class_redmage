# Problem 1

'''
import random

fruits_list = ['Apple', 'Orange', 'Banana']

def randomizer():

    x = random.randint(0,2)
    y = fruits_list[x]

    return y

print(randomizer())
'''

# Problem 2
'''
import string

def number_func():
    
    number_list = list(string.digits)
    number_tally = []
    
    main_flag = True
    while main_flag:
        
        loop_flag = False

        number_input = input("Enter a number or type 'done': > ").lower()
        
        if number_input == 'done':
            main_flag = False
            return number_tally
        
        for char in number_input:
            if char not in number_list:
                print("Needs to be a number")
                break
            else:
                loop_flag = True
                
        while loop_flag == True:
            number_input = int(number_input)
            number_tally.append(number_input)
            break
        
print(number_func())
'''

# Problem 3
'''
def eveneven(list):
    # new_list = []
    # for x in list:
    #     new_list.append(x % 2)
    # x = new_list.count(0)
    # if x % 2 == 0:
    #     return True
    # return False
    
    for x in range(len(list)):
        list[x] = list[x] % 2
    
    x = list.count(0)
    
    if x % 2 == 0:
        return True    
    return False


print(eveneven([5, 6, 2]))
print(eveneven([5, 5, 2]))
'''

# Problem 4 < done 'for loop', need to do 'while loop'
'''
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def print_every_other(nums):
    out_list = []

    for x in nums:
        if x % 2 == 0:
            out_list.append(x)
    
    return out_list

print(print_every_other(nums))


def print_every_other(nums)
    while len(nums) > 4: 
'''

# Problem 5
'''
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def reverse(nums):
 
    nums = nums[::-1]
    return nums

print(reverse(nums))
'''

# Problem 6
'''
nums = [0, 5, 22, 45, 50, 23, 1]
def extract_less_than_ten(nums):

    new_list = []
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < 10:
            x = nums.pop(i)
            new_list.append(x)    
    return new_list

print(nums)
print(extract_less_than_ten(nums))
'''

# Problem 7
# Write a function to find all common elements between two lists.

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
nums2 = [1, 3, 5, 7, 9]

def common_elements(nums1, nums2):
    new_list = []
    for i in nums2:
        for i in nums1:
            if nums2[i] == nums1[i]:
                new_list.append(nums1[i])

    return new_list

print(common_elements(nums1, nums2))
