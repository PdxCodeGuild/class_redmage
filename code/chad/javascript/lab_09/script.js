let req = new XMLHttpRequest("https://favqs.com/api/qotd");
let pdisplayText = document.getElementById("ddisplay-test");
let idisplayBtn = document.getElementById("idisplay-button")

req.addEventListener("progress", function(e) {
    console.log(e.loaded);
});
req.addEventListener("error", function(e) {
    console.log(e.status);
});
req.addEventListener("load", function(e) {
    console.log(req.responseText);
});

idisplayBtn.addEventListener("click", function() {
    req.open("GET", "https://favqs.com/api/qotd");
    var para = document.createElement("p");
    var node = document.createTextNode(req);
    para.appendChild(node);

    
    pdisplayText.appendChild(para);
})