let cash;
let flag;
let user_input;

class Atm {

    // initializes with balance and sets interest rate default
  constructor (self, balance = 0, int_rate = .001) {
      this.balance= balance;
      this.int_rate= int_rate;
      this.trans = [];
  }

  // returns the account balance
  check_balance() {
      return this.balance;
  }

  // deposits the given amount in the account
  deposit() {
      this.balance += amount;
      this.trans.push(`${amount} deposited`);
      return this.balance;
  }

  // returns true if the withdrawn amount won't put the account in the negative
  __check_withdrawal(){
      if ((this.balance - amount) >= 0) {
          return True;
      } else {
          return False;
        }
  }

  // withdraws the amount from the account and returns it
  withdraw() {
      if (this.__check_withdrawal(amount)) {
        this.balance -= amount;
        this.trans.push(`${amount} withdrawn`);
        return self.balance;
      } else {
        return "Error: Not enough money to withdraw.";
      }
  }

  // returns the amount of interest calculated on the account
  calc_interest() {
      return (this.balance * this.int_rate);
  }

  // prints out a history of transactions
  print_transactions() {
      return `Transactions: ${self.trans.join(", ")}`;
      }
}


cash = ATM(500);
flag = True;
alert("Thank you for using VERYSECUREDEFINITELYNOTFRAUD ATM\nWhat action would you like to do:\n1 for Deposit\n2 for Withdraw\n3 for Check Balance\n4 for Transaction History\n5 for Finish");

while (flag) {
  user_input = int(prompt('>'));

  if (user_input == 1) {
    try {
      deposit_amount = int(prompt("How much would you like to deposit: $"));
      cash.deposit(deposit_amount);
    }
    catch {
      alert('Enter a valid amount.');
    }
  }else if (user_input == 2) {   withdraw_amount = int(prompt("How much would you like to withdraw: $"))
    try{
      if ("Error" in cash.withdraw(withdraw_amount)){
        alert("Not enough funds for that withdrawal amount.");
    }
  } catch {
    alert(`Account debited by ${withdraw_amount}.`)
    }
    } else if (user_input == 3) {
      alert(`***Your balance on this account is ${cash.check_balance()}***`)
    } else if (user_input == 4) {
      alert(cash.print_transactions())
    } else if (user_input == 5) {
      flag = False;
    }
  }