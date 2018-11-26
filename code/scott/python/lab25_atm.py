# lab25_atm
import random
import string
import os
# balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account

# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new function print_transactions() to your class for printing out the list of transactions.

# Allow the user to enter commands into a REPL.

class Account:
        
    def __init__(self, name):
        self.acc_num = random.randint(1,10000)
        self.username = name
        self.balance = 0
        self.interest_rate = .1
        self.trans_list = []

    def balance_check(self):
        super().__init__()
        return self.balance
    
    def deposit(self, amount):
        super().__init__()
        self.balance += amount
        self.trans_list.append(f"Deposit of ${amount}.")
    
    def check_withrawal(self, amount):
        super().__init__()
        if amount >= self.balance:
            self.balance -= amount
            return True

    def withdrawal(self, amount):
        super().__init__()
        self.balance -= amount
        self.trans_list.append(f"Withdrawal for ${amount}.")
    
    def print_transactions(self):
        for i in self.trans_list:
            print(i)
        print(self.balance)




while True:
    user_input = input("ATM main menu. Please enter 'new' to create a new account, 'b' to see your balance, 'w' to withdrawal money, 'd' to deposit, or 't' to see previous transactions.")
    if user_input.upper() == "NEW":
        user_name = input("What is your name?")
        new_account = Account(user_name)
        print(f"Ok, {user_name}, we have created your account. Account number is {new_account.acc_num}. You may now deposit or withdraw.")
    elif user_input.upper() == "D":
        deposit = int(input(f"Please enter the amount you would like to deposit."))
        new_account.deposit(deposit)
        print(f"We have deposited ${deposit} into {new_account.acc_num}. Your balance is now ${new_account.balance}.")
    elif user_input.upper() == "W":
        withdrawal = int(input(f"Please enter the amount you would like to withdrawal."))
        if new_account.check_withrawal(withdrawal) == True:
            new_account.withdrawal(withdrawal)
        else:
            print("Insufficient Funds")
    elif user_input.upper() == "T":
        print("The following transactions have occurred: ")
        new_account.print_transactions()
    elif user_input.upper() == "B":
        print(new_account.balance)

