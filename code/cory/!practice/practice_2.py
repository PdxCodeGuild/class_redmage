# Problem 1
'''
def hello(letter1, letter2, letter3, letter4, letter5):
    return letter1*2 + letter2*2 + letter3*2 + letter4*2 + letter5*2
print(hello('h', 'e', 'l', 'l', 'o'))
'''

# Problem 2
'''
def missing_char(string):
    out_list = []
    for i in range(len(string)):
        out_list.append(string[0:i] + string[i+1:len(string)])
    return out_list
question = input("What word would you like to slice? > ")
print(missing_char(question))
'''

# Problem 3
'''
def latest_letter(letter1):
    let_list = list(letter1)
    let_list.sort()
    return let_list[-1]

print(latest_letter('pneumonoultramicroscopicsilicovolcanocovniosis'))
'''

# Problem 4 
'''
def count_hi(letter):
    x = letter.count('hi')
    return x

print(count_hi('hihihihihihi'))
'''

# Problem 5
'''
def cat_dog(string):
    cat = string.count('cat')
    dog = string.count('dog')

    if cat == dog:
        return True
    
    return False

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('catdogcatdog'))
'''

# Problem 6
'''
def count_letter(letter, word):

    x = word.count(letter)

    return x

print(count_letter('i', 'antidisestablishmentterianism'))
print(count_letter('p', 'pneumonoultramicroscopicsilicovolcanoconiosis'))
'''

# Problem 7

def lower_case(string):
    string = string.lower()
    string = string.lstrip(' ')
    return string

print(lower_case("SUPER!"))
print(lower_case("        NANNANANANA BATMAN        "))