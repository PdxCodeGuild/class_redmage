let cnv = document.getElementById('cnv');
let ctx = cnv.getContext('2d');

let ball = {
    radius: 4,
    px: Math.random()*1000,
    py: Math.random()*500,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};

ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'green';
ctx.fill();
let newX = (ball.px);
let newY = (ball.py);

function main_loop() {
    ctx.beginPath();
    ctx.arc(newX, newY, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = "white";
    ctx.strokeStyle = "white";
    ctx.stroke();
    ctx.fill();
     if (newX > 1000){
         newX= 1000;
         ball.vx = ball.vx * .99;
         ball.vx = -(ball.vx);
     }else if (newX < 0) {
         newX= 0;
         ball.vx = ball.vx * .99;
         ball.vx = -(ball.vx);
     }if (newY >500) {
         newY = 500;
         ball.vy = ball.vy * .99;
         ball.vy = -(ball.vy);
    }else if (newY< 0) {
         newY = 0;
         ball.vy = ball.vy * .99;
         ball.vy = -(ball.vy);
     }
     newY += ball.vy;
     if (newY > 0) {
         newY += 2;
     }else if (newY < 500) {
        newY -+ 2;
     }
     newX += ball.vx;
     ctx.beginPath();
     ctx.arc(newX, newY, ball.radius, 0, 2 * Math.PI, false);
     ctx.fillStyle = 'green';
     ctx.fill();
     console.log(newX, newY)
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);

