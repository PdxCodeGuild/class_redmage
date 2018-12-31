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

let startBtn = document.createElement('button');
startBtn.innerText = "Start";
startBtn.id = "watchStart";
startBtn.addEventListener('click', startOperation);

let stopBtn = document.createElement('button');
stopBtn.innerText = "Stop";
stopBtn.id = "watchStop";

let lapBtn = document.createElement('button');
lapBtn.innerText = "Lap";
lapBtn.id = "watchLap";

let resetBtn = document.createElement('button');
resetBtn.innerText = "Reset";
resetBtn.id = "watchReset";

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

document.getElementById('watch_ops').style.visibility = "hidden";
// document.getElementById('timer_ops').style.visibility = "hidden";

function addZeros(i) {
  if (i < 10) {
    i = "0" + i
  };
  return i;
}

function showClock(){
  document.getElementById("target_clock").style.visibility = "visible";
  // document.getElementById("target_timer").style.visibility = "hidden";
  document.getElementById("target_stop").style.visibility = "hidden";
  document.getElementById('watch_ops').style.visibility = "hidden";
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
  document.getElementById("target_stop").style.visibility = "visbile";
  document.getElementById('watch_ops').style.visibility = "visible";
  // document.getElementById("target_timer").style.visibility = "hidden";
  document.getElementById("target_clock").style.visibility = "hidden";
  // document.getElementById('timer_ops').style.visibility = "hidden";
}

function createClock(){
  clock = new Date();
  time = clock.toString();
  targetClock.innerText = time;
  setInterval(createClock, 1000);
}

// function createTimer() {
//   timer = new Date();
//   time = timer.toString();
//   targetTimer.innerText = time;
// }

function createStop(){
  watch = new Date();
  watch.setHours(0,0,0,0);
  console.log(watch);
  let hours = watch.getHours();
  let minutes = watch.getMinutes();
  let seconds = watch.getSeconds();
  let mili = watch.getMilliseconds();
  console.log(hours,minutes,seconds,mili);
  hours = addZeros(hours);
  minutes = addZeros(minutes);
  seconds = addZeros(seconds);
  mili = addZeros(mili);
  console.log(hours,minutes,seconds,mili);

  let displayTime = `${hours} : ${minutes} : ${seconds} :: ${mili}`;
  console.log(displayTime);
  targetStop.innerText = displayTime;
}

function startOperation(){
  watch.setMilliseconds(watch.getMilliseconds() + 1);
  let hours = watch.getHours();
  let minutes = watch.getMinutes();
  let seconds = watch.getSeconds();
  let mili = watch.getMilliseconds();
  console.log(hours,minutes,seconds,mili);
  hours = addZeros(hours);
  minutes = addZeros(minutes);
  seconds = addZeros(seconds);
  mili = addZeros(mili);
  console.log(hours,minutes,seconds,mili);

  let displayTime = `${hours} : ${minutes} : ${seconds} :: ${mili}`;
  console.log(displayTime);
  targetStop.innerText = displayTime;
  setInterval(startOperation, 0001);
}