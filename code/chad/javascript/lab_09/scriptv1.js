
let pdisplayText = document.getElementById("ddisplay-test");
let idisplayBtn = document.getElementById("idisplay-button")






idisplayBtn.addEventListener("click", function() {
    let req = new XMLHttpRequest();
    var response;
    req.addEventListener("progress", function(e) {
        console.log(e.loaded);
        pdisplayText.innerText = "Loading...";
    });
    
    req.addEventListener("error", function(e) {
        console.log(e.status);
        target.innerText = "Cannot load quote. Try again later!";
    });
    
    req.addEventListener("load", function(e) {
        response = JSON.parse(req.responseText);
        let resultHTML = `
            <p>${response.quote.body}</p>
            <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
            `
        pdisplayText.innerHTML = resultHTML;
      
    });

    
    req.open("GET", "https://favqs.com/api/qotd");
    req.setRequestHeader("Authorization", 'Token token="apikey.js"');
    req.send();
   

    

    
})

// var para = document.createElement("p");
//     var node = document.createTextNode(response);
//     para.appendChild(node);
//     pdisplayText.appendChild(para);
