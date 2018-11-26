# practice03.py
import random
# Problem 1

# fruits = ['apples', 'bananas', 'pears']

# def rand_rem(list_to_change):
#     list_to_change.pop(random.randint(0, len(list_to_change)-1))
#     return list_to_change

# print(rand_rem(fruits))


# Problem 2

# number_list = []
# while True:
#     number = input("Enter a numer(or 'done'): ")
#     if number == "done":
#         print(number_list)
#     elif number != "done":
#         try:
#             number = int(number)
#             number_list.append(number)
#         except TypeError:
#             print("You must enter a number or 'done'.")
#             break


# Problem 3

# true_list = [1, 2, 3, 4, 5, 6, 7, 8]
# false_list = [1, 2, 3, 4, 5, 6, 7]
# def even_counter(user_list):
#     evens = 0
#     for num in user_list:
#         if num % 2 == 0:
#             evens += 1
#     if evens % 2 == 0:
#         return True
#     else:
#         return False
# print(even_counter(true_list))
# print(even_counter(false_list))


# Problem 4

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def print_every_other(user_list):
#     nums_list = []
#     for i in range(0, len(user_list), 2):
#        nums_list.append(i)
#     return nums_list
# print(print_every_other(nums))


# Problem 5

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def reverse(user_list):
#     new_list = []
#     for i in range(len(user_list)-1, 0, -1):
#         new_list.append(user_list[i])
#     return new_list
# print(reverse(nums))


# Problem 6

# nums = [1, 6, 10, 33, 9, 45, 13, 20, 4, 7, 20]
# def extract_less_than_ten(user_list):
#     new_list = []
#     for num in user_list:
#         if num < 10:
#             new_list.append(num)
#     return new_list

# print(extract_less_than_ten(nums))


# Problem 7

# nums1 = [1, 3, 4, 5, 6, 7, 8]
# nums2 = [2, 5, 4, 7, 9]
# def common_elements(nums1, nums2):
#     common = []
#     for num in nums1:
#         if num in nums2:
#             common.append(num)
#     return common

# print(common_elements(nums1, nums2))


# Problem 8
# Write a function to combine two lists of equal length into one, alternating elements.


# def combine(nums1, nums2):
#     ...


# combine(['a', 'b', 'c'], [1, 2, 3]) → ['a', 1, 'b', 2, 'c', 3]
# Problem 9
# Given a list of numbers, and a target number, find a pair of numbers from the list that sum to a target number

# nums = [5, 6, 2, 3]
# target = 7
# find_pair(nums, target) → [5, 2]
# Optional: return a list of all pairs of numbers that sum to a target value.

# Problem 10
# Write a function that merges two lists into a single list, where each element of the output list is a list containing two elements, one from each of the input lists.

# merge([5, 2, 1], [6, 8, 2]) → [[5, 6], [2, 8], [1, 2]]
# Problem 11
# Write a function combine_all that takes a list of lists, and returns a list containing each element from each of the lists.

# nums = [[5, 2, 3], [4, 5, 1], [7, 6, 3]]
# combine_all(nums) → [5, 2, 3, 4, 5, 1, 7, 6, 3]
# Problem 12
# Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.

# fibonacci(8) → [1, 1, 2, 3, 5, 8, 13, 21]
# Problem 13
# Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.


# def minimum(nums):
#     ...


# def maxmimum(nums):
#     ...


# def mean(nums):
#     ...


# def mode(nums):  # (OPTIONAL)
#     ...


# Problem 14
# Write a function which takes a list as a parameter and returns a new list with any duplicates removed.


# def find_unique(nums):
#     ...


# nums = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
# unique_nums = find_unique(nums) → [12, 24, 35, 88, 120, 155]
