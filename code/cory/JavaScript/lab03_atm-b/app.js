class ATM {

    constructor(interest=.01, balance=0) {
        this.interest = interest;
        this.balance = balance;
        this.transactionCounter = 0;
    }

    getBalance() {
        let parent = document.getElementById("balance-container");
        let elementExists = document.getElementById("balance-p");
        
        if (elementExists === null) {
            var balanceOut = document.createElement("p");
            balanceOut.id = "balance-p"
            balanceOut.textContent = `You currently have: $${this.balance} dollars.`;
            parent.appendChild(balanceOut);
        } else {
            document.getElementById("balance-p").remove();
            var balanceOut = document.createElement("p");
            balanceOut.id = "balance-p"
            balanceOut.textContent = `You currently have: $${this.balance} dollars.`;
            parent.appendChild(balanceOut);
        }
    }

    deposit(num) {
        this.balance += num;
        this.transactionCounter += 1;

        let parent = document.getElementById("transactions");
        let depositOut = document.createElement("p");
        depositOut.textContent = `Transaction number ${this.transactionCounter} : You Deposited $${num}.`;
        parent.appendChild(depositOut);

    }

    withdraw(num) {
        if (num <= this.balance) {
            this.balance -= num;
            this.transactionCounter += 1;

            let parent = document.getElementById("transactions");
            let withdrawOut = document.createElement("p");
            withdrawOut.textContent = `Transaction number ${this.transactionCounter} : You Withdrew $${num}.`;
            parent.appendChild(withdrawOut);

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

let balBtn1 = document.getElementById("bal-btn1");
balBtn1.addEventListener('click', function(e) {
    e.preventDefault();
    atm.getBalance();
});

let balBtn2 = document.getElementById("bal-btn2");
balBtn2.addEventListener('click', function(e) {
    e.preventDefault();
    let elementExists = document.getElementById("balance-p");
    if (elementExists != null) {
        document.getElementById("balance-p").remove();
    }
});


let withdrawBtn = document.getElementById("withdraw-btn");
withdrawBtn.addEventListener('click', function(e) {
    e.preventDefault(); // used to clear default (like submit)
    
    let withdrawAmount = document.getElementById("withdraw-input");
    console.log(withdrawAmount.value)
    atm.withdraw(parseInt(withdrawAmount.value));
    withdrawAmount.value = "";
    
});

let depositBtn = document.getElementById("deposit-btn");
depositBtn.addEventListener("click", function(e) {
    e.preventDefault();

    let depositAmount = document.getElementById("deposit-input");
    console.log(depositAmount.value)
    atm.deposit(parseInt(depositAmount.value));
    depositAmount.value = "";
})

let transactionDiv = document.getElementById("transactions");

let transactionBtn = document.getElementById("transaction-btn");
transactionBtn.addEventListener("click", function(e) {
    if (transactionDiv.style.display === "none") {
        transactionDiv.style.display = "block";
    } else {
        transactionDiv.style.display = "none";
    }
})
    