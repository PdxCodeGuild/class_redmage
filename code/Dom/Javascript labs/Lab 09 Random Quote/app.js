let target = document.getElementById("target");
let Btn = document.getElementById("button");

Btn.addEventListener("click", function(e){
    let req = new XMLHttpRequest();

req.addEventListener("progress", function(e) {
    target.innerText =`Request ${e.loaded/e.total *100}% complete`
});

req.addEventListener("error", function (e){
    target.innerText =`oh no error ${e.status}`;
});

req.addEventListener("load", function(e) {
    let response = JSON.parse(req.responseText);
    let resultHTML = `
        <h2>${response.quote.body}</h2>
        <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
        `
    target.innerHTML = resultHTML;
});

req.open("GET", "https://favqs.com/api/qotd");
req.send();
})
