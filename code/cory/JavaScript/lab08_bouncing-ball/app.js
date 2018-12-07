let canvas = document.querySelector("canvas");

let widthButton = document.getElementById("width-button");

let widthInput = document.getElementById("width-input");

let heightButton = document.getElementById("height-button");

let heightInput = document.getElementById("height-input");

let ctx = canvas.getContext('2d');

let ball;

ball = {
    radius: 20,
    px: Math.random()*canvas.width,
    py: Math.random()*canvas.height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10
};


console.log(canvas.width)
console.log(canvas.height)


// -------------------------------------------------------------------------- //



ctx.beginPath();
ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
ctx.fillStyle = 'green';
ctx.fill();
ctx.stroke();



function main_loop() {
    // ctx.moveTo(300, 200);
    // check if it hit a boundary
    // draw the ball
    window.requestAnimationFrame(main_loop);
}
window.requestAnimationFrame(main_loop);

// Click to draw lines
ctx.beginPath();
let unClicked = true;
canvas.onclick = function(event) {
  var x = event.clientX;
  var y = event.clientY;
  if (unClicked) {
    ctx.moveTo(x,y)
    unClicked = false;
  } else {
    ctx.lineTo(x,y);
    ctx.stroke();
  }
}

// Ball Function
function ballFunc(e)  {
    ball = {
        radius: 20,
        px: Math.random()*canvas.width,
        py: Math.random()*canvas.height,
        vx: (2*Math.random()-1)*10,
        vy: (2*Math.random()-1)*10
    };
    
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'green';
    ctx.fill();
};

// Width input
widthInput.addEventListener("keydown", function(e) {
    if (e.keyCode === 13) {
        widthButton.click();
    }
})

// Width Button
widthButton.addEventListener("click", function(e) {
    console.log(widthInput.value);
    canvas.width = widthInput.value;
    ballFunc();
    widthInput.value = "";
});

// Height input
heightInput.addEventListener("keydown", function(e) {
    if (e.keyCode === 13) {
        heightButton.click();
    }
})

// Height Button
heightButton.addEventListener("click", function(e) {
    console.log(heightInput.value);
    canvas.height = heightInput.value;
    ballFunc();
    heightInput.value = "";
});


