let cash;
let flag;

class Atm {

    // initializes with balance and sets interest rate default
  constructor (balance = 0, int_rate = .001, trans = []) {
      this.balance = balance;
      this.int_rate = int_rate;
      this.trans = trans;
  }

  // returns the account balance
  checkBalance() {
      return this.balance;
  }

  // deposits the given amount in the account
  deposit(amount) {
      this.balance += amount;
      this.trans.push(`$${amount} deposited`);
      return this.balance;
  }

  // returns true if the withdrawn amount won't put the account in the negative
  checkWithdrawal(amount){
      if ((this.balance - amount) >= 0) {
          return true;
      } else {
          return false;
        }
  }

  // withdraws the amount from the account and returns it
  withdraw(amount) {
      if (this.checkWithdrawal(amount) === true) {
        this.balance -= amount;
        this.trans.push(`$${amount} withdrawn`);
        return this.balance;
      } else {
        return ("Error: Not enough money to withdraw that amount.");
      }
  }

  // returns the amount of interest calculated on the account
  calcinterest() {
      return (this.balance * this.int_rate);
  }

  // prints out a history of transactions
  printTransactions() {
    if (this.trans.length == 0) {
      return ("No transactions yet.");
    } else {
      return (`Transactions: ${this.trans.join(", ")}`);
    }
  }
}

cash = new Atm(500);
flag = true;
alert("Thank you for using VERYSECUREDEFINITELYNOTFRAUD ATM\nWhat action would you like to do:\n1 for Deposit\n2 for Withdraw\n3 for Check Balance\n4 for Transaction History\n5 for Finish");

while (flag) {
  user_input = parseInt(prompt('>'));

  if (user_input === 1) {
    amount = parseFloat(prompt("How much would you like to deposit: $"));
    alert(`Account credited with $${amount}.`);
    cash.deposit(amount);
  } else if (user_input === 2) {
      amount = parseFloat(prompt("How much would you like to withdraw: $"));
      if (cash.checkWithdrawal(amount) === false){
        alert("Not enough funds for that withdrawal amount.");
      } else {
        cash.withdraw(amount);
        alert(`Account debited by $${amount}.`)}
  } else if (user_input === 3) {
      alert(`***Your balance on this account is ${cash.checkBalance()}***`);
  } else if (user_input === 4) {
      alert(cash.printTransactions());
  } else if (user_input === 5) {
      flag = false;
  }
}

// *****************deal with NaN*************************