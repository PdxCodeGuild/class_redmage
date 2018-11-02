import random

# # Prolem #1
# fruits = ['apples', 'bananas', 'pears']

# def func1(list_in):
#     x = random.randint(0,(len(list_in))-1)
#     selection = list_in[x]
#     return selection

# print(func1(fruits))

# # Problem #2
# def repl_func():
#     flag = True
#     my_list = []
#     while flag:
#         user_in = input("Enter a number (or 'done'): ")
#         if user_in == "done":
#             flag = False
#         else:
#             my_list.append(user_in)
#     return my_list

# print(repl_func())

# # Problem #3
# nums = [4,5,6,7,8]

# def eveneven(x):
#     n = [i%2 for i in x if i%2 == False]
#     if len(n)%2 == 0:
#         return True
#     else:
#         return False

# print(eveneven(nums))

# # Problem #4
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# def print_every_other_while(x):
#     n = 0
#     my_list = []
#     her_list = []
#     while n < len(x):
#         my_list.append(str(x[n]))
#         n += 2
#     my_list = ', '.join(my_list)

#     for b in range(0, len(x),2):
#         her_list.append(str(b))
#     her_list = ', '.join(her_list)


#     return f"while loop: {my_list} for loop: {her_list}"


# print(print_every_other_while(nums))

# # Problem 5
# my_list = ['chicken','egg']

# def reversed_func(x):
#     x.reverse()
#     return x

# print(reversed_func(my_list))

# # # Problem 6
# my_list = ['chicken','egg']

# def reverse_func(x):
#     truth = list(reversed(x))
#     return truth

# print(reverse_func(my_list))

# # Problem 6
# my_list = list(range(21))

# print(my_list)

# def extract_less_than_ten(x):
#     new_list = []
#     i= 0
#     while i < len(x):
#         if x[i] < 10:
#             new_list.append(x.pop(i))
#         else:
#             i+= 1
#     return new_list

# print(extract_less_than_ten(my_list))
# # Problem 7
# def common_elements(x, y):
#     new_list = []
#     for i in range(len(x)):
#         if x[i] in y and x[i] not in new_list:
#             new_list.append(x[i])
#     return new_list

# nums1 = [random.randrange(1,100,1,_int=int) for _ in range(11)]
# nums2 = [random.randrange(1,100,1,_int=int) for _ in range(11)]
# print(nums1, nums2)
# print(common_elements(nums1,nums2))

# # Problem 8
list1 = [random.randrange(1,100,1,_int=int) for _ in range(3)]
list2 = [random.randrange(1,100,1,_int=int) for _ in range(3)]
print(len(list1), len(list2))

def combine(x,y):
    new_list = []
    i = 0
    if len(x) == len(y):
        while i < len(x):
            new_list.append((x[i]))
            new_list.append((y[i]))
            i+=1
    else:
        return False
    return new_list

print(combine(list1,list2))
