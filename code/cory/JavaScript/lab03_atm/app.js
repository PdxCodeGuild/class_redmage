class ATM {

    constructor(interest=.01, balance=0) {
        this.interest = interest;
        this.balance = balance;
        this.transactionList = [];
        this.transactionCounter = 0;
    }

    getBalance() {
        // alert(transactionCounter)
        return this.balance;
    }

    deposit(num) {
        this.balance += num;
        this.transactionCounter += 1;
        this.transactionList.push(`You Deposited ${this.balance}.`)
    }

    withdraw(num) {
        if (num <= this.balance) {
            this.balance -= num;
            this.transactionCounter += 1;
            this.transactionList.push(`You withdrew ${this.balance}.`)
        } else if (num > this.balance) {
            alert(`You have ${this.balance} available, you cannot withdraw ${num}!`)
        }
        
    }

    transaction() {
        // alert("test")
        return this.transactionList;
    }

}

var atm = new ATM(.01, 100);
var loopPerm = true;

while (loopPerm) {

    permList = ["Balance", "Deposit", "Withdraw", "Transactions", "Quit"]

    userInput = prompt("What would you like to do: Balance, Deposit, Withdraw, Transactions, or Quit: ")

    for (let i = 0; i < permList.length; ++i) {

        if (userInput == permList[i].toLowerCase()) {
        
            if (userInput == permList[0].toLowerCase()) {
                alert(atm.getBalance());
            }

            if (userInput == permList[1].toLowerCase()) {
                depositAmount = prompt("How much would you like to deposit?");
                atm.deposit(parseInt(depositAmount));
            }

            if (userInput == permList[2].toLowerCase()) {
                withdrawAmount = prompt("How much would you like to withdraw?");
                atm.withdraw(parseInt(withdrawAmount));
            }

            if (userInput == permList[3].toLowerCase()) {
                atm.transaction()
            }
            
        }

    }

    if (userInput == permList[4].toLowerCase()) {
        var loopPerm = false;
    }

}


// else {
//     alert("The computer didn't like that answer... Please try again.")
// }