import string
user_input = str(input('Enter A Word To See If It Is A Palindrome? > '))

#1. Reverse Word and Check To See If Palindrome
def check_pal(word):
    reversed_word = list(reversed(word))
    join_word = ''.join(reversed_word)
    return (join_word == word)

#Call Function To Reverse Word and Check if Palindrome
print(f'Your Word is a Palindrome? {check_pal(user_input)}')


