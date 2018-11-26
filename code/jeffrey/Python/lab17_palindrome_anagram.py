def check_palindrome(user_input):
    user_input_reversed = user_input[::-1]
    if user_input == user_input_reversed:
        return True
    else:
        return False

user_input = input("Enter a palindrome: ")

print(check_palindrome(user_input))

def check_anagram(ui2, ui3):
    ui2 = ui2.lower()
    ui3 = ui3.lower()
    ui2 = ui2.replace(" ","")
    ui3 = ui3.replace(" ","")
    ui2 = list(map(str,ui2))
    ui3 = list(map(str,ui3))
    ui2 = ui2.sort()
    ui3 = ui3.sort()
    if ui2 == ui3:
        return True
    else:
        return False

ui2 = input("Enter a word or phrase: ")
ui3 = input("Enter a second word or phrase: ")

if check_anagram(ui2,ui3) == True:
    print("The last two inputs are anagrams.")
else:
    print("The last two inputs are NOT anagrams.")