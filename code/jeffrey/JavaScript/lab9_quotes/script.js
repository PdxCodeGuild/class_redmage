let btn = document.getElementById("btn");
let target = document.getElementById("target");
let searchBox = document.getElementById("searchBox");
let searchBtn = document.getElementById("searchBtn");
let seatchTarget = document.getElementById("searchTarget");
let pageBack = document.getElementById("pageBack");
let pageForward = document.getElementById("pageForward");
let pageOn = document.getElementById("pageOn");

btn.addEventListener("click", function(e){
  let req = new XMLHttpRequest();

  req.addEventListener("progress", function(e) {
    console.log(e.loaded);
    target.innerText = "Loading...";
  });
  req.addEventListener("error", function(e) {
    console.log(e.status);
    target.innerText = "Cannot load quote. Try again later!";
  });
  req.addEventListener("load", function(e) {
    console.log(req.responseText);
    let response = JSON.parse(req.responseText);
    console.log(req.responseText);
    console.log(response); // returns a JavaScript object
    let resultText = `
      <q>${response.quote.body}</q>
      <p><i><a href=${response.quote.url}</a>${response.quote.author}</i></p>
    `;
    target.innerHTML = resultText;
    console.log(resultText);
  });

  req.open("GET", "https://favqs.com/api/qotd");
  req.send();
});

searchBtn.addEventListener("click", function(e){
  let req = new XMLHttpRequest();
  let searchCrit = document.querySelector('input[name="searchCrit"]:checked').nodeValue;
  let searchText = ((searchBox.value).split(' ').join('+'));
  console.log(searchText, searchCrit);
  let pageId = 1;

  let results = document.getElementsByTagName("li");
  for (let i=(results.length -1); i>=0; i--, i<results.length){
    searchTarget.removeChild(results[i]);
  }

  req.addEventListener("progress", function(e) {
    console.log(e.loaded);
    searchTarget.innerText = "Loading...";
  });

  req.addEventListener("error", function(e) {
    console.log(e.status);
    searchTarget.innerText = "Cannot load quote. Try again later!";
  });

  req.addEventListener("load", function(e) {
    searchTarget.innerText = "";
    let response = JSON.parse(req.responseText);
    pageOn.innerText = `** Page ${pageId} **`;
    for (let i=0; i< response.quotes.length; i++){
        let li = document.createElement("li");
        li.innerHTML = `${response.quotes[i].body}<i><a href="${response.quotes[i].url}"> ~${response.quotes[i].author}</a></i></p>`;
        searchTarget.appendChild(li);
    }
  });

  pageForward.addEventListener("click", function(){
    let response = JSON.parse(req.responseText);
    if (response.last_page === false){
      pageId += 1;
    }
    for (let i=(results.length -1); i>=0; i--, i<results.length){
      searchTarget.removeChild(results[i]);
    }
    req.open("GET", `https://favqs.com/api/quotes?page=${pageId}&filter=${searchText}`);
    req.setRequestHeader("Authorization", `Token token="${api_key}"`);
    req.send();
  });

  pageBack.addEventListener("click", function(){
    if (pageId > 1){
      pageId -= 1;
    }
    for (let i=(results.length -1); i>=0; i--, i<results.length){
      searchTarget.removeChild(results[i]);
    }
    req.open("GET", `https://favqs.com/api/quotes?page=${pageId}&filter=${searchText}`);
    req.setRequestHeader("Authorization", `Token token="${api_key}"`);
    req.send();
  });

  req.open("GET", `https://favqs.com/api/quotes?page=${pageId}&filter=${searchText}`);
  console.log( `https://favqs.com/api/quotes?page=${pageId}&filter=${searchText}`);
  req.setRequestHeader("Authorization", `Token token="${api_key}"`);
  req.send();
});