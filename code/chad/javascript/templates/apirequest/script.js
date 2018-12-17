let dTarget = document.getElementById("dtarget"); //Define Where output text is going to
let displayBtn = document.getElementById("display-btn"); //assumes you have a button in your html
let apiUrl = ""

function runAPI() {
    displayBtn.addEventListener("click", function(e) {
        let req = new XMLHttpRequest();
        req.addEventListener("progress", function(e) {
            console.log(e.loaded);
            dTarget.innerText = "Loading...";
        });
        req.addEventListener("error", function(e) {
            console.log(e.status);
            dTarget.innerText = "Cannot load quote. Try again later!";
        });
        req.addEventListener("load", function(e) {
            dTarget.innerText = ""
            console.log(req.responseText);
            let response = JSON.parse(req.responseText);
            console.log(response);
            let resultHTML = `
                <p>${response.quote.body}</p> 
                <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
                `; //examples of api function queries, every api is going to be different here
            textTarget.innerHTML = resultHTML;
        });
        req.open("GET", `${apiUrl}`); //url is defined on top
        req.setRequestHeader("Authorization", `${apikey}`); // apikey is hidden in config.js
        req.send()
});
}
runAPI()