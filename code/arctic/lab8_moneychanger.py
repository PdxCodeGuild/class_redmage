#moneychanger.py
while True:
#ask the question 
    money = input("Enter a dollar amount to start with. (ex. $1.36, 45.02, $50) > ")
    #the following "lstrip" removes the "$"
    money = money.lstrip("$")
    #the value added in the question will multiply by 100
    money = int(float(money) * 100)
    #the following changes money
    quarter = money // 25
    money %= 25
    dime = money // 10
    money %= 10
    nickle = money // 5
    money %= 5
    penny = money // 1
    money %= 1

    print(f"You have {quarter} quarters, {dime} dimes, {nickle} nickles, and {penny} pennies.")