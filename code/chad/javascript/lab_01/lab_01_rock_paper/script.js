let items = {rock:"paper", paper:"scissors", scissors:"rock"};

let computerValues = ['rock', 'paper', 'scissors']
let computerChoice = computerValues[ Math.random() * computerValues.length | 0 ];
console.log(`Computer Chooses ${computerChoice}`);

function calculateFunc(textValue) {
    if (textValue === computerChoice) {
        alert('You Have A Tie');
    }
    else if (items[textValue] === computerChoice) {
        alert('Computer Won');
    }
    else {
        alert('User Won');
        console.log("you got here");
    }
}
let btn = document.getElementById('btn_submit');
let usertext = document.getElementById('userInput');

    
btn.addEventListener("click", function(evt) {
    let textValue = usertext.value;
    textValue = textValue.toLocaleLowerCase();
    console.log(textValue);
    if (textValue === "rock" || textValue === "paper" || textValue === "scissors"){
    calculateFunc(textValue);
    }
})
