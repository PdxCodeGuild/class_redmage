# practices.py

# Practice 1: Fundamentals

# Problem 1
# def is_even(a):
#     if a % 2 == 1:
#         return False
#     if a % 2 == 0:
#         return True

# print(is_even(5))
# print(is_even(6))

# Problem 2
# def opposite(a, b):
#     if a > 0 and b > 0:
#         return False
#     elif a < 0 and b < 0:
#         return False
#     else:
#         return True

# print(opposite(10, -1))
# print(opposite(2, 3))
# print(opposite(-1, -1))

#Problem 3
# def near_100(num):
#     if abs(100 - num) <= 10:
#         return True
#     if abs(100 - num) >= 10:
#         return False

# print(near_100(50))
# print(near_100(99))
# print(near_100(105))

# Problem 4
# def maximum_of_three(a, b, c):
#     num_list = [a,b, c]
#     num_list.sort()
#     return num_list[-1]

# print(maximum_of_three(5, 6, 2))
# print(maximum_of_three(-4, 3, 10))

# Problem 5
# for i in range(20):
#     print(2 ** i)