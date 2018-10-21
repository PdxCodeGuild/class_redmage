# Version 2

while True:
    money = input("Enter a dollar amount to start with. (ex $1.36, 45.02, $50) > ")
    money = money.lstrip("$")
    money = int(float(money) * 100)

    quarters = money // 25
    money %= 25
    dimes = money // 10
    money %= 10
    nickles = money // 5
    money %= 5
    pennies = money

    print(f"You have {quarters} quarters, {dimes} dimes, {nickles} nickles, and {pennies} pennies.")