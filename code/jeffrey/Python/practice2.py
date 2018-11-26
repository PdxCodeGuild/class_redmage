# print('Problem 1')
# def input_double():
#     user_input = input("Input a string: \n")
#     user_input = ''.join(2*x for x in user_input)
#     return user_input

# print(input_double())

# print('\nProblem 2')
# def input_cut_random():
#     user_input = input('Input a string: \n')
#     my_list = []
#     for char in user_input:
#         my_list.append(''.join(user_input.split(char,1)))
#     return my_list

# print(input_cut_random())

print('\nProblem 3')
word = 'word'

def latest_letter(word):
    my_list = sorted(word)
    return f"The last letter is : {str(my_list[-1])}"

print(latest_letter(word))

print('\nProblem 4')
string_ = 'hihihihinonohi'
def count_hi(string_):
    counter =  string_.count('hi')
    return counter
print(count_hi(string_))

print('\nProblem 5')
humane_society = 'catdogcat'
humane_society1 = 'dogcatdog'
humane_society2 = 'catdog'

def animal_equality(x):
    cat_counter = x.count('cat')
    dog_counter = x.count('dog')
    if cat_counter == dog_counter:
        return True
    else:
        return False

print(animal_equality(humane_society))
print(animal_equality(humane_society1))
print(animal_equality(humane_society2))

print('\nProblem 6')
item = 'mississippi'

def letter_in_word_counter(letter, word):
    frequency = word.count(letter)
    return f'{letter} is in {word} {frequency} times'
print(letter_in_word_counter('p',item))

print('\nProblem 7')
def make_little_no_whitespace(x):
    my_string = x.lower().strip()
    return my_string

x = '      WADU HEKKKKK    '

print(make_little_no_whitespace(x))

