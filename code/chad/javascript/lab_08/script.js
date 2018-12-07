var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
let width = 100;
let height = 100;
let ball = {
    radius: 25,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};

ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 10 * Math.PI, false);
ctx.fillStyle = 'green';
ctx.fill();

function main_loop() {
    canvas.onclick = function(event) {
    var x = event.clientX;
    var y = event.clientY;
    console.log(x);
    console.log(y);
    // update the ball's position
    // check if it hit a boundary
    // draw the ball
    }
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);