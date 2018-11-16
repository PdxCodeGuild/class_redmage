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
'''
nums1 = [1, 2, 3, 4, 5]
nums2 = [1, 3, 5, 7, 9]

def common_elements(nums1, nums2):

    # Long, but works. See bottom for original.
    new_list = [nums1[i] for i in range(len(nums1)) for n in range(len(nums2)) if nums1[i] == nums2[n]]

    
    # for i in range(len(nums1)):
    #     for n in range(len(nums2)):
    #         if nums1[i] == nums2[n]:
    #             new_list.append(nums1[i])

    return new_list
    
print(common_elements(nums1, nums2))
'''

# Problem 8
# Write a function to combine two lists of equal length into one, alternating elements.
# combine(['a','b','c'],[1,2,3]) → ['a', 1, 'b', 2, 'c', 3]
'''
def combine(nums1, nums2):

    # new_list = [nums1[i] + nums2[i] for i in range(len(nums1))]
    new_list = []

    for i in range(len(nums1)):
        new_list.append(nums1[i])
        new_list.append(nums2[i])
    return new_list

print(combine(['a','b','c'],[1,2,3]))
'''

# Problem 9
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number
# Optional: return a list of all pairs of numbers that sum to a target value.
'''
nums = [5, 6, 2, 3]
target = 7

def find_pair(nums, target):

    # new_list = []

    # for i in range(len(nums)):
    #     if nums[i] + nums[0] == target:
    #         new_list.append(nums[i])
    #     if nums[i] + nums[1] == target:
    #         new_list.append(nums[i])
    #     if nums[i] + nums[2] == target:
    #         new_list.append(nums[i])
    #     if nums[i] + nums[3] == target:
    #         new_list.append(nums[i])
    
    # for x in range(len(nums)):
    #     for y in range(len(nums)):
    #         if nums[x] + nums[y] == target:
    #             new_list.append(nums[x])

    new_list = [nums[x] for x in range(len(nums)) for y in range(len(nums)) if nums[x] + nums[y] == target]

    return new_list

print(find_pair(nums, target))
'''

# Problem 10
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.
# merge([5,2,1], [6,8,2]) → [[5,6],[2,8],[1,2]]
'''
def merge(list1, list2):

    new_list = [[list1[i], list2[i]] for i in range(len(list1))]

    return new_list

print(merge([5,2,1], [6,8,2]))
'''

# Problem 11
# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.
# combine_all(nums) → [5,2,3,4,5,1,7,6,3]
'''
nums = [[5,2,3],[4,5,1],[7,6,3]]
def combine_all(nums):

    new_list = [nums[x][y] for x in range(len(nums)) for y in range(len(nums[x]))]

    return new_list

print(combine_all(nums))
'''

# Problem 12
# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.
'''
def fibonacci(num):

    new_list = []

    for x in range(num):
        if len(new_list) < 2:
            new_list.append(1)
        else:
            new_list.append(new_list[x - 1] + new_list[x - 2])

    return new_list

print(fibonacci(8))
'''

# Problem 13
# Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.
'''
def minimum(nums):
    
    nums.sort()
    
    minimum = nums[0]
    return minimum

# print(minimum([1, 2, 3, 4, 5]))

def maximum(nums):
    
    nums.sort()
    nums.reverse()
    maximum = nums[0]
    return maximum

# print(maximum([1, 2, 3, 4, 5]))

def mean(nums):
    import statistics

    mean = statistics.mean(nums)
    return mean

# print(mean([1, 2, 3, 4, 5]))

def mode(nums):
    import statistics

    mode = statistics.mode(nums)
    return mode

print(mode([1, 2, 3, 4, 4, 5]))
'''

# Problem 14
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.
# unique_nums = find_unique(nums) → [12, 24, 35, 88, 120, 155]

def find_unique(nums):
    nums.sort()
    for i in range((len(nums) - 1), 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
    
    return nums

nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
unique_nums = find_unique(nums)

print(unique_nums)