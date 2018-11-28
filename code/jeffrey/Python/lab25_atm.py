class ATM:
    
    # initializes with balance and sets interest rate default
    def __init__ (self, balance = 0, int_rate = .001):
        self.balance= balance
        self.int_rate= int_rate
        self.trans = []

    # returns the account balance
    def check_balance(self):
        return f'{self.balance}'

    # deposits the given amount in the account
    def deposit(self, amount):
        self.balance += amount
        self.trans.append(f'${amount} deposited')
        return self.balance
        
    # returns true if the withdrawn amount won't put the account in the negative 
    def __check_withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            return True
        else:
            return False

    # withdraws the amount from the account and returns it
    def withdraw(self, amount):
        if self.__check_withdrawal(amount):
            self.balance -= amount
            self.trans.append(f'${amount} withdrawn')
            return self.balance
        else:
            return f"Error: Not enough money to withdraw."

    # returns the amount of interest calculated on the account
    def calc_interest(self):
        return (self.balance * self.int_rate)

    # prints out a history of transactions
    def print_transactions(self):
        # for i in range(len(self.trans)):
        #     print(self.trans[i])
        if not self.trans:
            return str('No transactions yet')
        else:
            return ', '.join(self.trans)

cash = ATM(500)
flag = True
print("Thank you for using VERYSECUREDEFINITELYNOTFRAUD ATM\nWhat action would you like to do:\n1 for Deposit\n2 for Withdraw\n3 for Check Balance\n4 for Transaction History\n5 for Finish")

while flag:
    user_input = int(input('>'))

    if user_input == 1:
        try:
            deposit_amount = int(input("How much would you like to deposit: $"))
            cash.deposit(deposit_amount)
        except:
            print('Enter a valid amount.')
    elif user_input == 2:
        withdraw_amount = int(input("How much would you like to withdraw: $"))
        try:
            if "Error" in cash.withdraw(withdraw_amount):
                print(str("Not enough funds for that withdrawal amount."))
        except:
            print(f'Account debited by ${withdraw_amount}.')
    elif user_input == 3:
        print(f'***Your balance on this account is ${cash.check_balance()}***')
    elif user_input ==4:
        print(cash.print_transactions())
    elif user_input ==5:
        flag = False
    