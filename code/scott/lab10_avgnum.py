#lab10_avgnum.py

#priming
nums = []
user_input = ""
#getting user input
while user_input != "done":
    user_input = input("Enter a number or type 'done' to get your average. >")
    nums.append(user_input)
    #letting them leave
    if user_input == "done":
        nums.remove(nums[-1])
        break
#priming
amt = 0
# adding the numbers
for num in nums:
    amt = int(amt) + int(num)
# averaging
amt = amt / len(nums)
# printing the result
print(f"The average of your numbers is {amt}")