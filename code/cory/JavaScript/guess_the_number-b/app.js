let randomNum = Math.ceil(Math.random() * 10);

console.log(randomNum);

var userInput = 0;

var guessTracker = 0;


//-----------------------------------

function win(userInput){

    if (parseInt(userInput) == randomNum) {
        alert(`The random number was ${randomNum}, you guessed correct after ${guessTracker} tries!`);
        playAgain();
    }   
}

//-----------------------------------

function playAgain() {

    gamePerm = true;

    while (gamePerm) {

        let continuePerm = prompt("Would you like to play again? Y/N:").toLowerCase();

        if (continuePerm == "y") {
            randomNum = Math.ceil(Math.random() * 10); // resets random num
            console.log(randomNum); // displays num in console
            guessTracker = 0; // resets counter
            gamePerm = false;
            enableBtn();
        }

        else if (continuePerm == "n") {
            gamePerm = false;
            endTitle = document.getElementById("title1-text");
            endTitle.innerText = "----- Thanks for playing! -----";
            endTitle.style.fontSize = "48px";
            endTitle.style.color = "red";
        }

        else {
            alert("The program didn't like that input... Please try again.");
        }

    }
    
}

//-----------------------------------

function enableBtn() {

    let x = document.getElementsByTagName("button");

    for (i = 0; i < x.length; i++) {
        x[i].disabled = false;
    }
}

//-----------------------------------

let button1 = document.getElementById("button1");
button1.addEventListener('click', button1Func);

let button2 = document.getElementById("button2");
button2.addEventListener('click', button2Func);

let button3 = document.getElementById("button3");
button3.addEventListener('click', button3Func);

let button4 = document.getElementById("button4");
button4.addEventListener('click', button4Func);

let button5 = document.getElementById("button5");
button5.addEventListener('click', button5Func);

let button6 = document.getElementById("button6");
button6.addEventListener('click', button6Func);

let button7 = document.getElementById("button7");
button7.addEventListener('click', button7Func);

let button8 = document.getElementById("button8");
button8.addEventListener('click', button8Func);

let button9 = document.getElementById("button9");
button9.addEventListener('click', button9Func);

let button10 = document.getElementById("button10");
button10.addEventListener('click', button10Func);

function button1Func(e) {
    userInput = 1;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button1.disabled = true;
    win(userInput);
}

function button2Func(e) {
    userInput = 2;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button2.disabled = true;
    win(userInput);
}

function button3Func(e) {
    userInput = 3;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button3.disabled = true;
    win(userInput);
}

function button4Func(e) {
    userInput = 4;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button4.disabled = true;
    win(userInput);
}

function button5Func(e) {
    userInput = 5;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button5.disabled = true;
    win(userInput);
}

function button6Func(e) {
    userInput = 6;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button6.disabled = true;
    win(userInput);
}

function button7Func(e) {
    userInput = 7;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button7.disabled = true;
    win(userInput);
}

function button8Func(e) {
    userInput = 8;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button8.disabled = true;
    win(userInput);
}

function button9Func(e) {
    userInput = 9;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button9.disabled = true;
    win(userInput);
}

function button10Func(e) {
    userInput = 10;
    guessTracker++;
    console.log(userInput, "Guess number: " + guessTracker);
    button10.disabled = true;
    win(userInput);
}






// else if (userInput.toLowerCase() == "quit") {
//     loopPerm = false;
// } 

// else {
//     // alert("Incorrect! Guess again!");
// }

