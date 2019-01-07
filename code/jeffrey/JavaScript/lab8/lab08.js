let cvs = document.getElementById("cvs");
let ctx = cvs.getContext("2d");

let friction = .99;
let gravity = 5;

let ball = {
  radius: 4,
  px: Math.random()*cvs.width,
  py: Math.random()*cvs.height,
  vx: (2*Math.random()-1)*10,
  vy: (2*Math.random()-1)*10
};

ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'green';
ctx.fill();

function main_loop() {
  // update the ball's position
  let ctx = cvs.getContext("2d");
  ball.py += ball.vy;
  ball.px += ball.vx;
  // redraw background
  ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
  ctx.fillRect(0, 0, cvs.width, cvs.height);
  // check if it hit a boundary *IF STATEMENTSSSSSSSS
  if ((ball.px + ball.radius) > cvs.width){
    ball.px = (cvs.width - ball.radius);
    // friction
    ball.vx *= friction;
    ball.vy *= friction;
    // reverse direction of ball
    ball.vx *= -1;
  } else if ((ball.px - ball.radius) < 0){
    ball.px = 0 + ball.radius;
    // friction
    ball.vx *= friction;
    ball.vy *= friction;
    // reverse direction of ball
    ball.vx *= -1;
  }
  if ((ball.py + ball.radius) > cvs.height){
    ball.py = (cvs.height - ball.radius);
    // friction
    ball.vx *= friction;
    ball.vy *= friction;
    // reverse direction of ball
    ball.vy *= -1;
  } else if ((ball.py + ball.radius) < 0) {
    ball.py = 0 + ball.radius;
    // friction
    ball.vx *= friction;
    ball.vy *= friction;
    // reverse direction of ball
    ball.vy *= -1;
  }
  if (ball.py - ball.radius > 0 ) {
    ball.py += gravity;
  } else if (ball.py + ball.radius < cvs.height) {
     ball.py += gravity;
  }

  // draw the ball
  ctx.beginPath();
  ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
  ctx.fillStyle = 'green';
  ctx.fill();

  window.requestAnimationFrame(main_loop);
}

window.requestAnimationFrame(main_loop);
