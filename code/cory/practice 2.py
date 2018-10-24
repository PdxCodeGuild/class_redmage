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

# Problem 4 < NOT DONE
# '''
def count_hi(letter):
    x = letter.split()
    print(x)
    return letter.count(letter)

print(count_hi('hihihi'))
# '''

# Problem 5


