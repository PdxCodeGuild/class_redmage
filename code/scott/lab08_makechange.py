#lab8_makechange.py

# priming
user_input = 0

# getting number of pennies
while user_input <= 0:
    user_input = float(input("How much money do you want to convert to change? (format: #.##)>"))

# convert from dollar form float to integer
user_input *= int(user_input * 100)

# defining a function to make change by removing values in decreasing order
def change(user_input):
    qtrs = user_input // 25
    balance = user_input % 25
    dimes = balance // 10
    balance = balance % 10
    nickels = balance // 5
    balance = balance % 5
    return qtrs, dimes, nickels, balance

# running the function with the user's input
changed = change(user_input)

#printing the results.
print(f"You get back {changed[0]} quarters, {changed[1]} dimes, {changed[2]} nickels, and {changed[3]} pennies")
