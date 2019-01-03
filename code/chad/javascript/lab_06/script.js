let clockTime = document.getElementById("pclock-time");
let displayLap = document.getElementById("pdisplay-lap");
let displayLapTime = document.getElementById("display-lapTtimes");
let startButton = document.getElementById("start-button");
let lapButton = document.getElementById("lap-button");
let countDownField = document.getElementById("icountdown-field");
let countDownBtn = document.getElementById("countdown-submit-button");
let stopButton = document.getElementById("stop-button");


let cocktimerint = setInterval(clockTimer, 1000);
let cocktimerdownint = setInterval(countDownTimer, 1000);
let stopbuttonint;
startButton.addEventListener("click", function() {
    stopbuttonint = setInterval(stopWatch, 1000);
})

stopButton.addEventListener("click", function() {
    clearInterval(stopbuttonint);

})


lapButton.addEventListener("click", function() {
    let newp = document.createElement("p");
    let newel = document.createTextNode(`${stoplapTime.toTimeString().match(/\d{2}:\d{2}:\d{2}/)[0]}`);
    alert(stoplapTime.toTimeString().match(/\d{2}:\d{2}:\d{2}/)[0])
    newp.appendChild(newel);
    displayLapTime.appendChild(newp);
    lapButton.removeEventListener("click");
})


function clockTimer() {
    let time = new Date()
    clockTime.innerHTML = time.toLocaleTimeString();

}

let stoplapTime = new Date();
stoplapTime.setHours(0,0,0,0);

function stopWatch(){
    stoplapTime.setSeconds(stoplapTime.getSeconds()+1);
    displayLap.innerHTML = stoplapTime.toTimeString().match(/\d{2}:\d{2}:\d{2}/)[0];

}

countDownBtn.addEventListener("click", function() {
    let inputValue = countDownField.value;
    let countTimerTime = new Date();
    countTimerTime.setHours(0,0,0,0);
    if (inputValue > 59){
        let countDownMinutes = Math.floor(inputValue / 60);
        let countDownSeconds = Math.floor(inputValue % 60);
        countTimerTime.setMinutes(countDownMinutes);
        countTimerTime.setSeconds(countDownSeconds);
        console.log(countTimerTime.toTimeString().match(/\d{2}:\d{2}:\d{2}/)[0])
    }
    alert(`${inputValue}`);

})

function countDownTimer(){
    countTimerTime.setSeconds(countTimerTime.getSeconds()-1);
    displayLap.innerHTML = stoplapTime.toTimeString().match(/\d{2}:\d{2}:\d{2}/)[0];

}


