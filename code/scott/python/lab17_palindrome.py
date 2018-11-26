# lab17_palindrome.py

def palindrome_checker(input_string):
    input_string = input("Input a word to check if it's an palindrome. ")
    input_reverse = input_string[::-1]
    if input_string == input_reverse:
        print("It's a palindrome!!")
    else:
        print("Not a palindrome.")

def anagram_checker(input1, input2):
    input1 = "".join(sorted(input1))
    input2 = "".join(sorted(input2))
    input1.upper
    input2.upper
    if input1 == input2:
        print("These words are anagrams")
    else:
        print("These two are not anagrams")
racecar = "racecar"
print(palindrome_checker(racecar))

apple = "apple"
print(anagram_checker(racecar, apple))