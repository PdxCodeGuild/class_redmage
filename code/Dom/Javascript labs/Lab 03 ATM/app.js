// #ATM
// class for ATM functions//
class ATM{
    constructor(balance=0, intRate= .01, trans= []) {
        this.balance = balance;
        this.intRate = intRate;
        this.trans = trans;
    }
    checkBalance() {
        return this.balance
    }
    deposit(amount) {
        this.trans.push(`Deposit ${amount}`);
       return (this.balance += amount);(t)
    }
    withdrawl(amount) {
        if ((this.balance - amount) >= 0 ){
            this.trans.push(`Withdrawl ${amount}`);
            alert(`You have withdrawn ${amount}`)
            return(this.balance -= amount);
        }else if ((this.balance- amount) < 0){
            return alert("insufficient funds")
        }
    }
    calcIntrest(){
        return (this.balance * this.intRate);
    }
    printTrans() {
        return(this.trans)
    }
}

// #REPL //
let atm = new ATM();
let session=true;
while (session) {
    command = prompt("Choose: deposit, withdrawl, check balance, history or exit:");{
        if (command === "deposit") {
            amount = parseFloat(prompt("Deposit amount:"));
            while (isNaN(amount)) {
                alert("that is not a valid amount");
                amount = parseFloat(prompt("Deposit amount:"));
            }alert(`You have deposited ${amount}`);
            atm.deposit(amount);          
        }else if (command === "withdrawl"){
            amount =parseFloat(prompt("Withdrawl amount:"));
            while (isNaN(amount)) {
                alert("that is not a valid amount");
                amount = parseFloat(prompt("Withdrawl amount"));
            }atm.withdrawl(amount);
        }else if (command == "check balance") {
            alert(atm.checkBalance());
        }else if (command == "history"){
            alert(atm.printTrans());
        }else if (command == "exit") {
            alert("Have a great day");
            session = false;
        }else if (command == null) {
            alert("Goodbye");
            session = false;
        }else {
            alert("Invalid command, try again.")
        }
    }
    
}




    // user_command = input("What would you like to do (deposit, withdrawl, check balance, histrory)? ")
    // if user_command == "deposit":
    //     amount = input("How much would you like to deposit?: $")
    //     try:
    //         account.deposit(int(amount))
    //         print(f"Your deposit of ${amount} has been added to your account")
    //     except:
    //         print("Please enter a valid amount.")
    // elif user_command == "withdrawl":
    //     amount = input("How much would you like to withdraw?: $")
    //     try:
    //         if account.withdraw(int(amount)) == "insufficient funds": 
    //             print ("insufficient funds")
    //         else:
    //             print(f"Your withdrawl of ${amount} has been deducted from your account ")
    //     except:
    //         "invalid input"   
    // elif user_command == "check balance":
    //     print(str(account.check_balance(),end='\n'))
    // elif user_command == "history":
    //     account.print_transactions()
    // exit_string = input("Would you like to do anything else?(y or n): ")
    // if exit_string == "n":
    //         break




