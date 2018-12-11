linkList = ["https://www.aol.com/", "https://www.yahoo.com/", "https://www.youtube.com/", "https://www.reddit.com/", "https://www.youtube.com/"];

let btn = document.getElementById("btn");
let container = document.getElementById("container");

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
}

btn.addEventListener("click", countdown)

var count = 5;
var timer = function () {
    count--;
    document.getElementById('countdown').innerHTML = count;
}
setInterval(timer, 1000);

if (count = 0) {
    let listNum = linkList.length;
    let randomNum = getRandomInt(listNum);
    window.location = linkList[randomNum];
}


