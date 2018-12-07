// setting up the time display

var currentTimeDiv = document.getElementById("current-time-div");


function createTime() {
    var currentTime = new Date();
    var currentDate = currentTime.toDateString();
    var currentHour = currentTime.getHours();
    var currentMinute = currentTime.getMinutes();
    var currentSecond = currentTime.getSeconds();
    currentTimeDiv.innerText = `${currentDate} ${currentHour}:${currentMinute}:${currentSecond}`;
};
setInterval(createTime, 1000);

// setting up the laps system
var startButtonDiv = document.getElementById("start-button-div");
var cancelButtonDiv = document.getElementById("cancel-button-div");
var lapButtonDiv = document.getElementById("cancel-button-div");
var displayLapDiv = document.getElementById("display-lap-div");
var lapsListDiv = document.getElementById("lap-list-div");

var startButton = document.createElement("button");
startButton.innerText = "Start";
startButton.addEventListener("click", startLaps);
startButtonDiv.appendChild(startButton);
var lapsTime = new Date();
lapsTime.setHours(0, 0, 0, 0)

function startLaps() {
    var lapsTime = new Date();
    lapsTime.setHours(0, 0, 0, 0)
    updateLapDisplay();
    setInterval(updateLapDisplay, 1000);
    startButtonDiv.style.visibility = "hidden";
    cancelButtonDiv.style.visibility = "visible";
}

var cancelButton = document.createElement("button");
cancelButton.innerText = "Cancel";
cancelButton.addEventListener("click", cancelLaps);
cancelButtonDiv.appendChild(cancelButton);

function cancelLaps() {
    startButtonDiv.style.visibility = "visible";
    cancelButtonDiv.style.visibility = "hidden";
};

var lapButton = document.createElement("button");
lapButton.innerText = "Lap";
lapButton.addEventListener("click", addLap)
lapButtonDiv.appendChild(lapButton);


function addLap() {
    let laptoAdd = document.createElement("div");
    lapToAdd = displayLapDiv.innerText;
    lapsListDiv.append(lapToAdd);
}

function updateLapDisplay() {
    var lapHours = lapsTime.getHours();
    var lapMinutes = lapsTime.getMinutes();
    var lapSeconds = lapsTime.getSeconds();
    timeToDisplay = lapHours + ":" + lapMinutes + ":" + lapSeconds;
    displayLapDiv.innerText = timeToDisplay;
    lapsTime.setSeconds(lapsTime.getSeconds() + 1);
};