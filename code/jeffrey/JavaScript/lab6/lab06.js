let clock, time, watch, timer;

let targetClock = document.getElementById('target_clock');
// let targetTimer = document.getElementById('target_timer');
let targetStop = document.getElementById('target_stop')

let clockBtn = document.createElement('button');
clockBtn.innerText = "Clock";
clockBtn.addEventListener('click', createClock);
clockBtn.addEventListener('click', showClock);

let clockBtnDiv = document.getElementById('clock_btn');
clockBtnDiv.appendChild(clockBtn);

// let timerBtn = document.createElement('button');
// timerBtn.innerText = "Timer";
// timerBtn.addEventListener('click', createTimer);
// timerBtn.addEventListener('click', showTimer);

// let timerBtnDiv = document.getElementById('timer_btn');
// timerBtnDiv.appendChild(timerBtn);

let stopwatchBtn = document.createElement('button');
stopwatchBtn.innerText = "Stopwatch";
stopwatchBtn.addEventListener('click', createStop);
stopwatchBtn.addEventListener('click', showWatch);

let stopwatchBtnDiv = document.getElementById('stopwatch_btn');
stopwatchBtnDiv.appendChild(stopwatchBtn);

// runs the stopwatch
let startBtn = document.createElement('button');
startBtn.innerText = "Start";
startBtn.id = "watchStart";
startBtn.addEventListener('click', function(){
  interval = setInterval(startOperation, 1000);
  startBtn.disabled = true;
});

// stops the stopwatch
let stopBtn = document.createElement('button');
stopBtn.innerText = "Stop";
stopBtn.id = "watchStop";
stopBtn.addEventListener('click', function(){
  clearInterval(interval);
  startBtn.disabled = false;
});

let lapBtn = document.createElement('button');
lapBtn.innerText = "Lap";
lapBtn.id = "watchLap";
lapBtn.addEventListener('click', lapTime);

let lapsList = document.getElementById('target_laps');

function lapTime(){
  let laps = document.createElement("li");
  let hours = watch.getHours();
  let minutes = watch.getMinutes();
  let seconds = watch.getSeconds();
  hours = addZeros(hours);
  minutes = addZeros(minutes);
  seconds = addZeros(seconds);
  laps.innerText = `${hours} : ${minutes} : ${seconds}`;
  lapsList.appendChild(laps);
};

let resetBtn = document.createElement('button');
resetBtn.innerText = "Reset";
resetBtn.id = "watchReset";
resetBtn.addEventListener("click", function(){
  // remove laps from list loop
  let laps = document.getElementsByTagName("li");
  for (let i=(laps.length - 1); i>=0; i--){
    lapsList.removeChild(laps[i]);
  }
  watch.setHours(0,0,0,0);
  clearInterval(interval);
  document.getElementById("target_stop").innerText = `${hours} : ${minutes} : ${seconds}`;
  startBtn.disabled = false;
})

// let timerField = document.createElement('input');
// timerField.placeholder = 'input a number here';

// let timerSubmitBtn = document.createElement('button');
// timerSubmitBtn.type = 'submit';
// timerSubmitBtn.innerText = "Submit";

let watchOpsDiv = document.getElementById('watch_ops');
// let timerOpsDiv = document.getElementById('timer_ops');

watchOpsDiv.appendChild(startBtn);
watchOpsDiv.appendChild(stopBtn);
watchOpsDiv.appendChild(lapBtn);
watchOpsDiv.appendChild(resetBtn);


// timerOpsDiv.appendChild(timerField);
// timerOpsDiv.appendChild(timerSubmitBtn);

// document.getElementById('watch_ops').style.visibility = "hidden";
// document.getElementById('timer_ops').style.visibility = "hidden";

function addZeros(i) {
  if (i < 10) {
    i = "0" + i
  };
  return i;
}

function showClock(){
  document.getElementById("target_clock").style.display = "block";
  // document.getElementById("target_timer").style.visibility = "hidden";
  document.getElementById("target_stop").style.display = "none";
  document.getElementById('watch_ops').style.display = "none";
// document.getElementById('timer_ops').style.visibility = "hidden";
}

// function showTimer(){
  // document.getElementById("target_timer").style.visibility = "visible";
//   document.getElementById('timer_ops').style.visibility = "visible";
//   document.getElementById("target_clock").style.visibility = "hidden";
//   document.getElementById("target_stop").style.visibility = "hidden";
//   document.getElementById('watch_ops').style.visibility = "hidden";
// }

function showWatch(){
  document.getElementById("target_stop").style.display = "block";
  document.getElementById('watch_ops').style.display = "block";
  // document.getElementById("target_timer").style.visibility = "hidden";
  document.getElementById("target_clock").style.display = "none";
  // document.getElementById('timer_ops').style.visibility = "hidden";
}

function createClock(){
  clock = new Date();
  time = clock.toString();
  targetClock.innerText = time;
  let interval = setInterval(function(){
    createClock();
    if (document.getElementById("target_clock").style.display === "none"){
      clearInterval(interval);
    };
  }, 1000);
}

// function createTimer() {
//   timer = new Date();
//   time = timer.toString();
//   targetTimer.innerText = time;
// }

// sets stopwatch = 0 on page load
watch = new Date();
watch.setHours(0,0,0);
let hours = watch.getHours();
let minutes = watch.getMinutes();
let seconds = watch.getSeconds();
hours = addZeros(hours);
minutes = addZeros(minutes);
seconds = addZeros(seconds);

// puts the stopwatch on the page
function createStop(){
  watch = new Date();
  watch.setHours(0,0,0);
  let hours = watch.getHours();
  let minutes = watch.getMinutes();
  let seconds = watch.getSeconds();
  hours = addZeros(hours);
  minutes = addZeros(minutes);
  seconds = addZeros(seconds);
  let displayTime = `${hours} : ${minutes} : ${seconds}`;
  targetStop.innerText = displayTime;
}

function startOperation(){
  watch.setSeconds(watch.getSeconds() + 1);
  let hours = watch.getHours();
  let minutes = watch.getMinutes();
  let seconds = watch.getSeconds();
  hours = addZeros(hours);
  minutes = addZeros(minutes);
  seconds = addZeros(seconds);

  let displayTime = `${hours} : ${minutes} : ${seconds}`;
  targetStop.innerText = displayTime;
}