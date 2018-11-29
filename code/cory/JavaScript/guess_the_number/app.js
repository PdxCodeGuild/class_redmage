let randomNum = Math.ceil(Math.random() * 10);

console.log(randomNum);

var guessTracker = 0;

let loopPerm = true;

while(loopPerm) {

    let gamePerm = false;

    let userInput = prompt("Choose a number between 1 and 10:");

    guessTracker++;

    if (parseInt(userInput) == randomNum) {
        alert(`The random number was ${randomNum}, you guessed correct after ${guessTracker} tries!`);
        gamePerm = true;
    } 
    
    else if (userInput.toLowerCase() == "quit") {
        loopPerm = false;
    } 
    
    else {
        alert("Incorrect! Guess again!");
    }

    while (gamePerm) {
        let continuePerm = prompt("Would you like to play again? Y/N:").toLowerCase();

        if (continuePerm == "y") {
            randomNum = Math.ceil(Math.random() * 10);
            console.log(randomNum);
            guessTracker = 0;
            gamePerm = false;
        }

        else if (continuePerm == "n") {
            gamePerm = false;
            loopPerm = false;
        }

        else {
            alert("The program didn't like that input... Please try again.");
        }

    }
}
