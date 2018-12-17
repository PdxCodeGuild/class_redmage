

var canvas = document.getElementById("canvas");
canvas.width = canvas.scrollWidth;
canvas.height = canvas.scrollHeight;
var ctx = canvas.getContext("2d");
// function drawRotatedImage(ctx, image, x, y, width, height, rotation) {
//     var halfWidth = width / 2;
//     var halfHeight = height / 2;

//     ctx.save();

//     ctx.translate(x + halfWidth, y + halfHeight);
//     ctx.rotate(rotation);
//     ctx.drawImage(image, -halfWidth, -halfHeight, width, height);

//     ctx.restore();
// }

function draw(ctx, image) {

    if (!image.complete){
        setTimeout(function(){
            draw(ctx, image);
        }, 50);
        return;
    }
    
    animate();
}

var image = new Image();
image.src = "./image.png"

draw(ctx, image);

// image.onload = function(){
//     ctx.drawImage(image, 10, 10, 200, 200);
//     ctx.drawImage(image, 0, 0, image.naturalWidth / 2, image.naturalHeight / 4, 300, 10, 200, 200);
// }

var x = 300; // setting a starting point to beging iterating and moving with
var y = 100;
var dx = 4; // setting x velocity
var dy = 4;
var radius = 30;

function animate() {
    requestAnimationFrame(animate)
    ctx.clearRect(0, 0, 800, 600);

    ctx.drawImage(image, x, y, 60, 60);
    
    // ctx.beginPath();
    // ctx.arc(x, y, radius, 0, 2 * Math.PI, false);
    // ctx.fillStyle = 'green';
    // ctx.fill();

    if (x + 60 > 800 || x < 0) {
        dx = -dx;
    };

    if (y + 60 > 600 || y < 0) {
        dy = -dy;
    };
    
    // dx = dx * .99;
    // dy = dy * .99;

    x += dx;
    y += dy;
};



// ctx.beginPath();
// ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
// ctx.fillStyle = 'green';
// ctx.fill();

// function main_loop() {
//     // update the ball's position
//     // check if it hit a boundary
//     // draw the ball
//     window.requestAnimationFrame(main_loop);
// }
// window.requestAnimationFrame(main_loop);
