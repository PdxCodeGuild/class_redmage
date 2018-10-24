def check_palindrome(user_input):
    user_input_reversed = user_input[::-1]
    if user_input == user_input_reversed:
        return True
    else:
        return False

user_input = input("Enter an anagram: ")

print(check_palindrome(user_input))