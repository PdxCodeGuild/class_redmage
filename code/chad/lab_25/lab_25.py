

class Atm():
    def __init__(self, balance, interest):
        self.account_balance = balance
        self.account_interest = interest
    def check_balance(self):
        print(self.account_balance)
    def deposit(self, amount):
        self.account_balance = self.account_balance + amount
    def check_withdrawal(self, amount):
        if amount >= self.account_balance:
            print('You Have Enough To Make A WithDrawl')
        if amount < self.account_balance:
            print('You DO NOT Have Enough To Make A WithDrawl')
    def withdraw(self, amount):
        self.account_balance -= amount
    def calc_interest(self):
        return_interest = self.account_balance * self.account_interest
        return return_interest
account1 = Atm(0,.001)
while True:
    print('Welcome To Chads ATM Machine'
                '\n1. Check Account Balance'
                '\n2. Deposit Money Into Your Acount'
                '\n3. Check Withdrawl To Make Sure Will Not Overdraft Account'
                '\n4. Withdraw money From Your Account'
                '\n5. Calculate Interest On Your Account'
                '\n6. Quit Program'
                )
    menu_option = int(input('Type The Number Of The Function You Would Like To Do: > '))
    if menu_option == 6:
        break
    if menu_option == 1:
        account.check_balance()
    if menu_option == 2:
        ask_deposit = int(input('How Much Would You Like TO Deposit? > '))
        account.deposit(ask_deposit)
    if menu_option == 3:
        check_withdraw = int(input('How Much Would You Like To See If Your Account Balance Has Enough To Withdrawl? > '))
        account.check_withdrawal(check_withdraw)
    if menu_option == 4:
        ask_withdraw = int(input('How Much Would You Like To Withdraw? > '))
        account.withdraw(ask_withdraw)
    if menu_option == 5:
        calculated_interest = account.calc_interest()
        print(calculated_interest)


