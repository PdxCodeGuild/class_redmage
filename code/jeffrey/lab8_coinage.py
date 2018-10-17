# conditionals; comparisons; arithmetic

user_input = (input("How much money are you exchanging? I'll only give you the least amount of coins as possible.\n"))

if "$" in user_input:
    user_input = user_input[(user_input.find("$"))+1:]
    user_input = int(float(user_input)*100)
else:
    user_input = int(float(user_input)*100)

quarter = user_input//25
dime = (user_input%25)//10
nickel = ((user_input%25)%10)//5
penny = (((user_input%25)%10)%5)//1

print("That's " + str(quarter) + " quarter[s], " + str(dime) + " dime[s], "+ str(nickel) + " nickel[s], and "+ str(penny) + " penny[ies].")

# print(user_input)