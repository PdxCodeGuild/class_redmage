winningTicket = [];
newTicket = [];
cashEarned = 0;

function numberGenerator() {
    let ranNum = Math.ceil(Math.random() * 6);
    console.log(ranNum)
    return ranNum;
}

let winBtn1Value;
let winBtn1 = document.getElementById("win-btn1");
winBtn1.addEventListener('click', function(e) {
    winBtn1Value = numberGenerator();
    document.getElementById("win-btn1").textContent = `${winBtn1Value}`;
});

console.log(winBtn1.textContent);

let winBtn2Value;
let winBtn2 = document.getElementById("win-btn2");
winBtn2.addEventListener('click', function(e) {
    winBtn2Value = numberGenerator();
});

