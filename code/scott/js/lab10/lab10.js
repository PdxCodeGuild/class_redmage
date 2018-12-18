// priming
let searchDiv = document.getElementById("searchDiv");
let searchButton = document.getElementById("searchButton");
let randomDate = document.getElementById("randomDate");
let randomYear = document.getElementById("randomYear");
let infoDiv = document.getElementById("infoDiv");
let dateDiv = document.getElementById("dateDiv");
let textDiv = document.getElementById("textDiv");
let yearDiv = document.getElementById("yearDiv");
let dateBox = document.getElementById("dateBox");

let yearToCheck;
let monthToCheck;
let dayToCheck; // done priming

// event listener for the random buttons
randomDate.addEventListener("click", getRandomDate);
randomYear.addEventListener("click", getRandomYear);


function getRandomDate() {
    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {

        if (xhr.readyState == 4) {
            if (xhr.status == 200) {
                console.log(xhr);
                dateDiv.innerHTML = xhr.responseText;
            }
            if (xhr.status == 404) {
                dateDiv.innerHTML = "Uh oh, something went wrong."
            }
        }
    }
    xhr.open("get", "http://numbersapi.com/random/date", true);
    xhr.send();
}

function getRandomYear() {
    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {

        if (xhr.readyState == 4) {
            if (xhr.status == 200) {
                console.log(xhr);
                yearDiv.innerHTML = xhr.responseText;
            }
            if (xhr.status == 404) {
                yearDiv.innerHTML = "Uh oh, something went wrong."
            }
        }
    }
    xhr.open("get", "http://numbersapi.com/random/year", true);
    xhr.send();
}



// event listener for the search button
searchButton.addEventListener("click", sendXhr1);

function sendXhr1() {
    const xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function () {

        if (xhr.readyState == 4) {
            if (xhr.status == 200) {
                console.log(xhr);
                dateDiv.innerHTML = xhr.responseText;
                sendXhr2();
            }
            if (xhr.status == 404) {
                dateDiv.innerHTML = "Uh oh, something went wrong."
            }
        }
    }
    var dateToCheck = document.getElementById("dateBox").value;

    // making sure it is grabbed
    console.log(dateToCheck);

    // parsing the default format
    monthToCheck = dateToCheck.substr(5, 2);
    dayToCheck = dateToCheck.substr(8, 2); // done parsing
    xhr.open("get", `http://numbersapi.com/${monthToCheck}/${dayToCheck}/date?default=stop+picking+boring+numbers.`, true);
    xhr.send();
}

function sendXhr2() {
    const xhr2 = new XMLHttpRequest();

    xhr2.onreadystatechange = function () {

        if (xhr2.readyState == 4) {
            if (xhr2.status == 200) {
                console.log(xhr2);
                console.log(xhr2.responseText);
                yearDiv.innerHTML = xhr2.responseText;
                req3();
            }
            if (xhr2.status == 404) {
                yearDiv.innerHTML = "Uh oh, something went wrong."
            }
        }
    }
    var dateToCheck = document.getElementById("dateBox").value;

    // making sure it is grabbed
    console.log(dateToCheck);

    // parsing the default format
    yearToCheck = dateToCheck.substr(0, 4) // done parsing
    xhr2.open("get", `http://numbersapi.com/${yearToCheck}/year?notfound=floor?default=stop+picking+boring+numbers.`, true);
    xhr2.send();
}



