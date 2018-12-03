let items = {rock:"paper", paper:"scissors", scissors:"rock"};

while (true) {
    var userInput = prompt("Choose Rock, Paper or Scissors");
    userInput.toLocaleLowerCase;
    if (userInput === "paper" || "rock" || "scissors") {break};
    
}

userInput.toLocaleLowerCase
console.log(`You Chose ${userInput}`)

let computerValues = ['rock', 'paper', 'scissors']
let computerChoice = computerValues[ Math.random() * computerValues.length | 0 ];
console.log(`Computer Chooses ${computerChoice}`)


if (userInput === computerChoice) {
    alert('You Have A Tie')
}
else if (items[userInput] === computerChoice) {
    alert('Computer Won')
}
else {
    alert('User Won')
    console.log("you got here")
}