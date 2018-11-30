// #guess_the_number
let num = Math.floor(Math.random()*21);
let guessNum = 0
let lastGuess = 0
// let game = true;
let btn = document.querySelector('#btn');
alert(num);
// keeps game going?
// 

btn.addEventListener('click', checkguess);
// 
// function to check the guess d
// 
function checkguess() {
    let guess = document.getElementById("guess");
    let userGuess = parseInt(guess.value);
    console.log(`num is ${num} user guess is ${userGuess}, last guess is ${lastGuess}`);
    console.log(guessNum);
    ++guessNum;
    let message = document.getElementById("message");{
    if (userGuess === num) {  
            // game = false; 
            message.innerText= `You won and it only took you ${guessNum} tries!`;
    }else if (userGuess !== num) {
        if (guessNum === 1) {
            if (userGuess < num) {
                    lastGuess = userGuess;
                    message.innerText= "too low, try again";
            }else if (userGuess > num) {
                    lastGuess = userGuess;
                    message.innerText="too high, try again";
            }
        } else {
            if (Math.abs(num - userGuess) < Math.abs(num -lastGuess)) {
                    lastGuess = userGuess;
                    message.innerText="Getting warmer, try again.";
            }else if (Math.abs(num - guess) > Math.abs(num -lastGuess)) {
                    lastGuess = guess;
                    message.innerText="Getting colder, try again.";
                } 
            }
        }
    }
}

