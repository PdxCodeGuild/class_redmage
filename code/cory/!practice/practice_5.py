# Problem 1
# Write a comprehension to generate the first 10 powers of two.
# ex > [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
'''
def powers_of_two(power=2):
    powers_of_two = [power ** num for num in range(10)]
    return powers_of_two

print(powers_of_two())
print(powers_of_two(3))
print(powers_of_two(10))
'''

# Problem 2
# Write a comprehension to generate the first 10 even numbers.
# ex > [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''
def first_even_nums(num_range=21):
    first_even_nums = [num for num in range(num_range) if num % 2 == 0]
    return first_even_nums

print(first_even_nums(50))
print(first_even_nums())
'''

# Problem 3
# Write a dictionary comprehension to swap keys and values of a given dictionary. So {'a': 1, 'b': 2} would become {1: 'a', 2: 'b'}.
'''
def key_value_swap():
    dict1 = {'a': 1, 'b': 2} 
    key_value_swap = {value: key for key, value in dict1.items()}
    return key_value_swap

print(key_value_swap())
'''

# Problem 4
# Write a dictionary comprehension to print each letter of the alphabet and its correstponding ASCII code (check out ord)
# {'a': 97, 'b': 98, 'c': 99, 'd': 100...}
'''
import string
def letter_to_ascii():
    letters = string.ascii_lowercase

    out_dict = {letter: ord(letter) for letter in letters}
    return out_dict

print(letter_to_ascii())
'''
