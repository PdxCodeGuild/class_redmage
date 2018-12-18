let container = document.getElementById("container");
let buttonDiv = document.getElementById("button-div");
let getRandomButton = document.getElementById("get-random-button");
let searchDiv = document.getElementById("search-div");
let searchBox = document.getElementById("search-box");
let searchButton = document.getElementById("search-button");
let quoteDiv = document.getElementById("quote-div");
let page_id = 1;

getRandomButton.addEventListener("click", getQuote);
searchButton.addEventListener("click", searchQuote);

let nextButton = document.createElement("button");
nextButton.innerHTML = "Next Page";
nextButton.addEventListener("click", function () {
    let req = new XMLHttpRequest();
    let addHTML = "";
    req.addEventListener("progress", function (e) {
        console.log(e.loaded);
        quoteDiv.innerText = "Loading...";
    });
    req.addEventListener("error", function (e) {
        console.log(e.status);
        quoteDiv.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function (e) {
        console.log(req.responseText); // returns the raw text response
        let response = JSON.parse(req.responseText);
        let quotes = response.quotes;
        console.log(response); // returns a JavaScript object

        for (i = 0; i < quotes.length; i++) {
            addHTML += `
        <p>${quotes[i].body}</p>
        <p><i><a href="${quotes[i].url}">${quotes[i].author}</a></i></p>
        `
        }

        quoteDiv.innerHTML = addHTML;
        pageNum += 1;

    });

    let searchText = searchBox.value;
    req.open("GET", "https://favqs.com/api/quotes/?page=" + pageNum + "filter=" + searchText);
    req.setRequestHeader("Authorization", 'Token token=' + config.favqKey);
    req.send();
});


function getQuote() {
    console.log("getquote");
    let req = new XMLHttpRequest();
    req.addEventListener("progress", function (e) {
        console.log(e.loaded);
        quoteDiv.innerText = "Loading...";
    });
    req.addEventListener("error", function (e) {
        console.log(e.status);
        quoteDiv.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function (e) {
        console.log(req.responseText); // returns the raw text response
        let response = JSON.parse(req.responseText);
        console.log(response); // returns a JavaScript object
        let resultHTML = `
        <p>${response.quote.body}</p>
        <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
        `
        quoteDiv.innerHTML = resultHTML;
    });
    req.open("GET", "https://favqs.com/api/qotd");
    req.setRequestHeader("Authorization", 'Token token=' + config.favqKey);
    req.send();
    console.log(req);
};

var pageNum;

function searchQuote() {
    console.log("searchquote");
    let req = new XMLHttpRequest();
    let addHTML = "";
    pageNum = 1;
    req.addEventListener("progress", function (e) {
        console.log(e.loaded);
        quoteDiv.innerText = "Loading...";
    });
    req.addEventListener("error", function (e) {
        console.log(e.status);
        quoteDiv.innerText = "Cannot load quote. Try again later!";
    });
    req.addEventListener("load", function (e) {
        console.log(req.responseText); // returns the raw text response
        let response = JSON.parse(req.responseText);
        let quotes = response.quotes;
        console.log(response); // returns a JavaScript object

        for (i = 0; i < quotes.length; i++) {
            addHTML += `
        <p>${quotes[i].body}</p>
        <p><i><a href="${quotes[i].url}">${quotes[i].author}</a></i></p>
        `
        }
        
        quoteDiv.innerHTML = addHTML;
        console.log("added quotes, supposed to run 'createnext' now")
        createNext();
    });
    let searchText = searchBox.value;
    req.open("GET", "https://favqs.com/api/quotes/?filter=" + searchText);
    req.setRequestHeader("Authorization", 'Token token=' + config.favqKey);
    req.send();
    console.log(req);
};

function createNext() {
    console.log("createnext has started");
    searchDiv.appendChild(nextButton);
    console.log("it should have appended the button by now. Where is it?")
};
