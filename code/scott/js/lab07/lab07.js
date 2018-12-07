function getRandomInt() {
    return Math.ceil(Math.random() * 5);
}
var hackSource = document.getElementById("pre-div");
hackSourceCode = hackSource.innerText;

var startNum = 0;
var cont = document.getElementById("container");
var hackingSpaceDiv = document.getElementById("hacking-space-div")


function addHacks() {
    console.log("addhacks started");
    let randInt = startNum + getRandomInt();
    let newSlice = hackSourceCode.slice(startNum, randInt);
    startNum = randInt;
    let startStr = hackingSpaceDiv.innerText;
    let newStr = startStr + newSlice;
    hackingSpaceDiv.append(newSlice);
};

var hackerTextDiv = document.getElementById("hacker-text-div");
var hackerTextPre = document.createElement("pre");
hackerTextDiv.addEventListener("keypress", addHacks);

var bod = document.getElementById("body");

bod.addEventListener("keypress", addHacks);
// cont.addEventListener("keydown", addHacks);
hackerTextDiv.appendChild(hackerTextPre);
