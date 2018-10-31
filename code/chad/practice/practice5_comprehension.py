'''
Problem 1

Write a comprehension to generate the first 10 powers of two.
prac_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]




prac_list = [2**num for num in range(10)]
print(prac_list)

Problem 2

Write a comprehension to generate the first 10 even numbers.
prac_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


prac_list = [num*2 for num in range(1,11)]

print(prac_list)


Write a dictionary comprehension to swap keys and values of a given dictionary. 
So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.


dict = {'a': 1, 'b': 2} 
prac_dict = {value:key for key, value in dict.items()}
print(prac_dict)

Problem 4

Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code (check out ord)

{'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, ...}


import string
pract_dict = {key:ord(key) for key in string.ascii_lowercase }

print(pract_dict)

'''