


let clockTime = document.getElementById("pclock-time")
let displayLap = document.getElementById("display-lap")
let displayLapTime = document.getElementById("display-lapTtimes")
let startButton = document.getElementById("start-button")
let lapButton = document.getElementById("lap-button")

setInterval(clockTimer, 1000);

startButton.addEventListener("click", function() {
    setInterval(stopWatch, 1000);
})

lapButton.addEventListener("click", function() {
    
    let newp = document.createElement("p");

    let newel = document.createTextNode(`${stoplapTime.toLocaleTimeString()}`);
    alert(stoplapTime.toLocaleTimeString())
    newp.appendChild(newel);
    displayLapTime.appendChild(newp);
})


function clockTimer() {
    let time = new Date()
    clockTime.innerHTML = time.toLocaleTimeString();
    // location.reload();
    
}

let stoplapTime = new Date();
stoplapTime.setHours(0,0,0,0);

function stopWatch(){
    stoplapTime.setSeconds(stoplapTime.getSeconds()+1);
    displayLap.innerHTML = stoplapTime.toLocaleTimeString();
    
   
}



