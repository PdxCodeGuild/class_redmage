let clock, time, targetDiv, clockBtn, clockBtnDiv;

targetClock = document.getElementById('target_clock');

clockBtn = document.createElement('button');
clockBtn.innerText = "You want clock, ok?";
clockBtn.addEventListener('click', createTime);

clockBtnDiv = document.getElementById('clock_btn');
clockBtnDiv.appendChild(clockBtn);

function createTime(){
  clock = new Date();
  time = clock.toString();
  targetClock.innerText = time;
  setInterval(createTime, 1000);
}


