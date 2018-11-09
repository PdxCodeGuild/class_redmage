# Version 3

class Atm:
    '''This class is a mock ATM machine.'''
    # Used for counting each transaction
    transaction_counter = 0

    # Initial account setup
    def __init__(self, interest, balance=0, transactions={}):
        '''Initial setup, including interest and balance'''
        self.interest = interest
        self.balance = balance
        self.transactions = transactions

    # returns the account balance
    def check_balance(self):
        '''Checks current balance'''
        return self.balance

    # deposits the given amount in the account
    def deposit_money(self, amount):
        '''Deposits money'''
        self.balance += amount
        self.transaction_counter += 1
        self.transactions.update({self.transaction_counter: f"User deposited ${amount}."})

    # returns true if the withdrawn amount won't put the account in the negative
    def check_withdrawal(self, amount):
        '''Checks if you can use withdraw method'''
        if self.balance >= amount:
            return f"Your current balane is {self.balance}, you may withdraw {amount}."
        elif self.balance <= amount:
            return f"Your current balane is {self.balance}, you cant withdraw {amount}."

    # withdraws the amount from the account and returns it
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_counter += 1
            self.transactions.update({self.transaction_counter: f"User withdrew ${amount}."})
            return f"Your current balance is {self.balance}, after you withdrew {amount}."
        elif self.balance <= amount:
            return f"You can't withdraw {amount}, you only have {self.balance} in your balance."

    # returns the amount of interest calculated on the account
    def calc_interest(self):
        '''Shows amount of interest gained'''
        return f"Interest gained is ${round(self.interest * self.balance)}."

    def print_transactions(self):
        out_string = '\n'
        for key in self.transactions:
            out_string += f'{key}.) {self.transactions[key]}\n'
        return out_string

start_bal = int(input("What is your starting balance? > "))
user1 = Atm(.01, start_bal)

#Main loop, just control + C to exit
while True:
    
    options_list = ['check balance', 'deposit', 'withdraw', 'history', 'check withdrawal', 'interest gained']

    options = ''
    while options not in options_list:
        options = input("What would you like to do? (check balance, deposit, withdraw, history, check withdrawal, interest gained) > ").lower()
        if options not in options_list:
            print("\nOptions didn't like that answer. Try again.\n")
    
    if options == 'check balance':
        print(user1.check_balance())

    elif options == 'deposit':
        deposit_input = int(input("How much would you like to deposit? > "))
        user1.deposit_money(deposit_input)
    
    elif options == 'withdraw':
        withdraw_input = int(input("How much would you like to withdraw? > "))
        print(user1.withdraw(withdraw_input))
        

    elif options == 'history':
        print(user1.print_transactions())

    elif options == 'check withdrawal':
        check_withdrawl_input = int(input('How much would you like to check? > '))
        print(user1.check_withdrawal(check_withdrawl_input))

    elif options == 'interest gained':
        print(user1.calc_interest())

    else:
        print("\nOptions didn't like that answer. Try again.\n")
