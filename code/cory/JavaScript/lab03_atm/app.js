class ATM {

    constructor(interest=.01, balance=0) {
        this.interest = interest;
        this.balance = balance;
        this.transactionDict = {};
        this.transactionCounter = 0;
    }

    getBalance() {
        return this.balance;
    }

    deposit(num) {
        this.balance += num;
        this.transactionCounter += 1;
        this.transactionDict[`Transaction number ${this.transactionCounter} : `] = `You Deposited ${num}.`
    }

    withdraw(num) {
        if (num <= this.balance) {
            this.balance -= num;
            this.transactionCounter += 1;
            this.transactionDict[`Transaction number ${this.transactionCounter} : `] = `You withdrew ${num}.`
        } else if (num > this.balance) {
            alert(`You have ${this.balance} available, you cannot withdraw ${num}!`)
        }
        
    }

    transaction() {
        for (let x in this.transactionDict) {
            alert(x + " " + this.transactionDict[x]);
        }
    }

}

var atm = new ATM(.01, 100);
var loopPerm = true;

while (loopPerm) {

    permList = ["balance", "deposit", "withdraw", "transactions", "quit"]

    userInput = prompt("What would you like to do: Balance, Deposit, Withdraw, Transactions, or Quit: ").toLowerCase()

    console.log(userInput)

    if (permList.indexOf(userInput) >= 0) {

        if (userInput == permList[0]) {
            alert(atm.getBalance());
        }

        else if (userInput == permList[1]) {
            depositAmount = prompt("How much would you like to deposit?");
            atm.deposit(parseInt(depositAmount));
        }

        else if (userInput == permList[2]) {
            withdrawAmount = prompt("How much would you like to withdraw?");
            atm.withdraw(parseInt(withdrawAmount));
        }

        else if (userInput == permList[3]) {
            atm.transaction();
        }

        else if (userInput == permList[4]) {
            var loopPerm = false;
        }
        
    }

    else {
        alert("The computer didn't like that input... Please try again.");
    }
    

}