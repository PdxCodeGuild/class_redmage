def palindrome_funct():
    user_inp = input("Enter a word: > ")
    user_inp = user_inp.capitalize()
    reverse = user_inp[::-1].capitalize()

    if user_inp == reverse:
        return f"{user_inp} and {reverse} are palindromes!"
    return f"{user_inp} and {reverse} are not palindromes!"

def anagram_funct():
    first_input = input("Whats the first word? > ")
    second_input = input("Whats the second word? > ")

    first_word = first_input.lower()
    second_word = second_input.lower()
    
    first_word = first_word.replace(" ", "")
    second_word = second_word.replace(" ", "")

    first_word = ''.join(sorted(first_word))
    second_word = ''.join(sorted(second_word))

    if first_word == second_word:
        return f"{first_input} and {second_input} are anagrams!"
    return f"{first_input} and {second_input} are not anagrams..."

while True:
    function_check = ''
    while function_check != 'P' and function_check != 'A' and function_check != 'E':
        function_check = input("What would you like to do? Palindrome (type 'P'), Anagram (type 'A'), or Exit (type 'E')? > ").upper()
    if function_check == 'P':
        print(palindrome_funct())
    elif function_check == 'A':
        print(anagram_funct())
    elif function_check == 'E':
        print('\nThanks for playing!\n')
        break