// -------------------- V1 LAB -------------------- //



// Sets clock on page, so it loads with the time instead of waiting
let v1Date = new Date();
document.getElementById("clock-wrapper").innerHTML = v1Date.toLocaleTimeString();

// Variable to set clock changes every second
let clockInterval = setInterval(clockTimer, 1000);

// Function to update time
function clockTimer() {
    v1Date = new Date();
    document.getElementById("clock-wrapper").innerHTML = v1Date.toLocaleTimeString();
};



// -------------------- V2 LAB -------------------- //



// Creates new date, initiates 0 time, creates 0:0:0 text at top, inits sec counter
let d = new Date();
d.setHours(0, 0, 0, 0);
document.getElementById("clock").innerHTML = d.toLocaleTimeString("en-gb");
let secCounter = 0;

// Main function to update seconds
function clock() {
    secCounter += 1;
    d.setHours(0, 0, secCounter);
    document.getElementById("clock").innerHTML = d.toLocaleTimeString("en-gb");
}

// Start button stuff
let myTimer;
let startBtn = document.getElementById("start-button");
startBtn.addEventListener("click", function(e) {
    if (startBtn.innerText == "Start") {
        myTimer = setInterval(clock, 1000);
        startBtn.innerText = "Stop";
        resetBtn.disabled = true;
    } else if (startBtn.innerText == "Stop") {
        clearInterval(myTimer);
        startBtn.innerText = "Start";
        resetBtn.disabled = false;
    }
});

// Reset button stuff
let resetBtn = document.getElementById("reset-button");
resetBtn.disabled = false;
resetBtn.addEventListener("click", function(e) {
    d.setHours(0, 0, 0, 0);
    document.getElementById("clock").innerHTML = d.toLocaleTimeString("en-gb");
    secCounter = 0;
});

// Lap button stuff
let lapCounter = 1;
let lapBtn = document.getElementById("lap-button");
lapBtn.addEventListener("click", function(e) {

    let lapVar = document.createTextNode(`Lap ${lapCounter}: ` + d.toLocaleTimeString("en-gb"));

    lapCounter++;

    let newElement = document.createElement("li");

    newElement.appendChild(lapVar);

    document.getElementById("lap-list").appendChild(newElement);
});



// -------------------- V3 LAB -------------------- //

let v3Date = new Date();
v3Date.setHours(0, 0, 0)
document.getElementById("countdown-timer").innerHTML = v3Date.toLocaleTimeString("en-gb");

let dropMenu = document.getElementById("countdown-list");

let timeInput = document.getElementById("countdown-input");

// Event for setting countdown timer
let timeSubmit = document.getElementById("countdown-input-btn");
timeSubmit.addEventListener("click", function(e) {
    if (dropMenu.value == "Hour") {
        v3Date.setHours(timeInput.value);
        document.getElementById("countdown-timer").innerHTML = v3Date.toLocaleTimeString("en-gb");
    } else if (dropMenu.value == "Minute") {
        v3Date.setMinutes(timeInput.value);
        document.getElementById("countdown-timer").innerHTML = v3Date.toLocaleTimeString("en-gb");
    } else if (dropMenu.value == "Second") {
        v3Date.setSeconds(timeInput.value);
        document.getElementById("countdown-timer").innerHTML = v3Date.toLocaleTimeString("en-gb");
    }
});

function countdownClock() {
    console.log(v3Date)
    v3Date.setSeconds(v3Date.getSeconds()-1);
    document.getElementById("countdown-timer").innerHTML = v3Date.toLocaleTimeString("en-gb");
};

// Start button stuff
let myTimerv3;
let startBtnv3 = document.getElementById("countdown-start-btn");
startBtnv3.addEventListener("click", function(e) {
    myTimerv3 = setInterval(countdownClock, 1000);
    console.log(v3Date)
});

// } else if (startBtn.innerText == "Stop") {
//     clearInterval(myTimer);
//     startBtn.innerText = "Start";
//     resetBtn.disabled = false;
// }