let dTarget = document.getElementById("dtarget"); //Define Where output text is going to

let displayBtn = document.getElementById("input-display-btn"); 

let divUserName = document.getElementById("div-user-name"); 
let divUserLocation = document.getElementById("div-user-location"); 
let divUserPlanguauge = document.getElementById("div-user-planguage"); 

let inputUserInputName = document.getElementById("user-input-name"); 
let inputUserInputLocation = document.getElementById("user-input-location"); 
let inputUserInputPlanguauge = document.getElementById("user-input-planguauge"); 


let chkBoxName = document.getElementById("chk-box-name")
let chkBoxLocation = document.getElementById("chk-box-location")
let chkBoxPlanguage = document.getElementById("chk-box-programming-languauge")

var chkBoxNameInputValue = ""
var chkBoxLocationInputValue = ""
var chkBoxPlanguaugeInputValue = "" 






function displayFields() {
    chkBoxName.addEventListener("change", function() { 
        if(this.checked) {
            document.getElementById("div-user-name").style.display = "block"
        }
        else {
            document.getElementById("div-user-name").style.display = "none"
        }
    })
    chkBoxLocation.addEventListener("change", function() { 
        if(this.checked) {
            document.getElementById("div-user-location").style.display = "block"
        }
        else {
            document.getElementById("div-user-location").style.display = "none"
        }
    })
        
    chkBoxPlanguage.addEventListener("change", function() { 
        if(this.checked) {
            document.getElementById("div-user-planguage").style.display = "block"
        }
        else {
            document.getElementById("div-user-planguage").style.display = "none"
        }
    })
        
}

function runAPI() {
    let apiUrl = `https://api.github.com/search/users?q="${chkBoxNameInputValue}"${chkBoxLocationInputValue}`;
    console.log(apiUrl)
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
            // let resultHTML = `
            //     <p>${response.quote.body}</p>
            //     <p><i><a href="${response.quote.url}">${response.quote.author}</a></i></p>
            //     `
            // textTarget.innerHTML = resultHTML;
        });
        req.open("GET", `${apiUrl}`); //url is defined on top
        req.setRequestHeader("Authorization", `${apikey}`); // apikey is hidden in config.js
        req.send()
});
}

function searchGit() {
    
    displayBtn.addEventListener("click", function() {
        if (chkBoxName.checked == true) {
            chkBoxNameInputValue = inputUserInputName.value;
            }
        if (chkBoxLocation.checked == true) {
            chkBoxLocationInputValue = inputUserInputLocation.value;
            console.log(chkBoxLocationInputValue);
            }
        if (chkBoxPlanguage.checked == true) {
            chkBoxPlanguaugeInputValue = inputUserInputPlanguauge.value;
            console.log(chkBoxPlanguaugeInputValue);
            }
        runAPI()    
        })
           
        }
   

function runScript() {
    displayFields();
    searchGit();
}

runScript()