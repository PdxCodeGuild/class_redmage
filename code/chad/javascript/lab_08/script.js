var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
let width;
let height;



function main_loop() {
    canvas.onclick = function(event) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        let ball = {
            radius: 25,
            px: Math.random()*(762.5) + 25,
            py: Math.random()*(562.5) + 25,
            vx: (2*Math.random()-1)*10,
            vy: (2*Math.random()-1)*10
            };
       
        console.log(ball.px);
        console.log(ball.py);
        if (Math.floor(ball.px) === 25 || Math.floor(ball.py === 25)){
            alert("you hit a boundry")
        }
        ctx.beginPath();
        ctx.arc(ball.px, ball.py, ball.radius, 0, 10 * Math.PI, false);
        ctx.fillStyle = 'green';
        ctx.fill();
        
    }
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);