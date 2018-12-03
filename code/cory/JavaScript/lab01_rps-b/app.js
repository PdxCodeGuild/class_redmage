let rpsList = ['Rock', 'Paper', 'Scissors'];


var gameLoop = true;

while (gameLoop) {
    cpuChoice = rpsList[Math.floor(Math.random() * 3)]

    userChoice = prompt(`Choose one: ${rpsList[0]}, ${rpsList[1]}, or ${rpsList[2]}:`)

    // Tie breaker
    if (userChoice === cpuChoice) {
        alert("It's a tie!")
    }

    // If user chooses Rock
    if (userChoice === rpsList[0] && cpuChoice == rpsList[1]) {
        alert("You Lose!");
    } else if (userChoice === rpsList[0] && cpuChoice == rpsList[2]) {
        alert("You Win!");
    }

    // If user chooses Paper
    if (userChoice === rpsList[1] && cpuChoice == rpsList[2]) {
        alert("You Lose!");
    } else if (userChoice === rpsList[1] && cpuChoice == rpsList[0]) {
        alert("You Win!");
    }

    // If user chooses Scissors
    if (userChoice === rpsList[2] && cpuChoice == rpsList[0]) {
        alert("You Lose!");
    } else if (userChoice === rpsList[2] && cpuChoice == rpsList[1]) {
        alert("You Win!");
    }

    endVar = prompt("Would you like to play again? y/n") 
    
    if (endVar == 'y') {

    } else if (endVar == 'n') {
        var gameLoop = false;
    }
}   
