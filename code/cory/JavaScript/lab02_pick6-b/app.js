winningTicket = [];
newTicket = [];
cashEarned = 0;

function numberGenerator() {
    let ranNum = Math.ceil(Math.random() * 6);
    // ranNum = 6;
    return ranNum;
}

let winBtn1Value;
let winBtn1 = document.getElementById("win-btn1");
winBtn1.addEventListener('click', function(e) {
    winBtn1Value = numberGenerator();
    winBtn1.textContent = `${winBtn1Value}`;
    winBtn1.disabled = true;
});

let winBtn2Value;
let winBtn2 = document.getElementById("win-btn2");
winBtn2.addEventListener('click', function(e) {
    winBtn2Value = numberGenerator();
    document.getElementById("win-btn2").textContent = `${winBtn2Value}`;
    winBtn2.disabled = true;
});

let winBtn3Value;
let winBtn3 = document.getElementById("win-btn3");
winBtn3.addEventListener('click', function(e) {
    winBtn3Value = numberGenerator();
    winBtn3.textContent = `${winBtn3Value}`;
    winBtn3.disabled = true;
});

let winBtn4Value;
let winBtn4 = document.getElementById("win-btn4");
winBtn4.addEventListener('click', function(e) {
    winBtn4Value = numberGenerator();
    winBtn4.textContent = `${winBtn4Value}`;
    winBtn4.disabled = true;
});

let winBtn5Value;
let winBtn5 = document.getElementById("win-btn5");
winBtn5.addEventListener('click', function(e) {
    winBtn5Value = numberGenerator();
    winBtn5.textContent = `${winBtn5Value}`;
    winBtn5.disabled = true;
});

let winBtn6Value;
let winBtn6 = document.getElementById("win-btn6");
winBtn6.addEventListener('click', function(e) {
    winBtn6Value = numberGenerator();
    winBtn6.textContent = `${winBtn6Value}`;
    winBtn6.disabled = true;
});

// ----------------------------------------------------------------------------

let userBtn1Value;
let userBtn1 = document.getElementById("user-btn1");
userBtn1.addEventListener('click', function(e) {
    userBtn1Value = numberGenerator();
    userBtn1.textContent = `${userBtn1Value}`;
    userBtn1.disabled = true;
});

let userBtn2Value;
let userBtn2 = document.getElementById("user-btn2");
userBtn2.addEventListener('click', function(e) {
    userBtn2Value = numberGenerator();
    document.getElementById("user-btn2").textContent = `${userBtn2Value}`;
    userBtn2.disabled = true;
});

let userBtn3Value;
let userBtn3 = document.getElementById("user-btn3");
userBtn3.addEventListener('click', function(e) {
    userBtn3Value = numberGenerator();
    userBtn3.textContent = `${userBtn3Value}`;
    userBtn3.disabled = true;
});

let userBtn4Value;
let userBtn4 = document.getElementById("user-btn4");
userBtn4.addEventListener('click', function(e) {
    userBtn4Value = numberGenerator();
    userBtn4.textContent = `${userBtn4Value}`;
    userBtn4.disabled = true;
});

let userBtn5Value;
let userBtn5 = document.getElementById("user-btn5");
userBtn5.addEventListener('click', function(e) {
    userBtn5Value = numberGenerator();
    userBtn5.textContent = `${userBtn5Value}`;
    userBtn5.disabled = true;
});

let userBtn6Value;
let userBtn6 = document.getElementById("user-btn6");
userBtn6.addEventListener('click', function(e) {
    userBtn6Value = numberGenerator();
    userBtn6.textContent = `${userBtn6Value}`;
    userBtn6.disabled = true;
});

let resultsText = document.getElementById("results-text");

function checkNums(e) {
    let cashTotal = 0;
    if (winBtn1Value == userBtn1Value) {
        cashTotal += 10;
    } if (winBtn2Value == userBtn2Value) {
        cashTotal += 10;
    } if (winBtn3Value == userBtn3Value) {
        cashTotal += 10;
    } if (winBtn4Value == userBtn4Value) {
        cashTotal += 10;
    } if (winBtn5Value == userBtn5Value) {
        cashTotal += 10;
    } if (winBtn6Value == userBtn6Value) {
        cashTotal += 10;
    }

    resultsText.innerText = `You have won: $${cashTotal}`
}

let resultsBtn = document.getElementById("results-btn");
// resultsBtn.disabled = true;

resultsBtn.addEventListener("click", checkNums);
