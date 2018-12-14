//Define Where output text is going to
let dTarget = document.getElementById("dtarget"); 

//where the results of the output is to be displayed
let displayBtn = document.getElementById("input-display-btn"); 

//div sections that are hidden by defualt until javascript displays them
let divUserName = document.getElementById("div-user-name"); 
let divUserLocation = document.getElementById("div-user-location"); 
let divUserPlanguauge = document.getElementById("div-user-planguage"); 

//user input fields
let inputUserInputName = document.getElementById("user-input-name"); 
let inputUserInputLocation = document.getElementById("user-input-location"); 
let inputUserInputPlanguauge = document.getElementById("user-input-planguauge"); 

//checkboxes to be clicked which have event listeners to display div
let chkBoxName = document.getElementById("chk-box-name")
let chkBoxLocation = document.getElementById("chk-box-location")
let chkBoxPlanguage = document.getElementById("chk-box-programming-languauge")

//setting up variable to use used later
let chkBoxNameInputValue;
let chkBoxLocationInputValue;
let chkBoxPlanguaugeInputValue;
var userArray;

//event listeners to display divs onces checkboxes are checked
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


//runs API call after user inputs some information
function runAPI() {
    // let apiUrl = `https://api.github.com/search/users?q=${chkBoxNameInputValue}+location:${chkBoxLocationInputValue}+language:${chkBoxPlanguaugeInputValue}`;
    let apiUrl = `https://api.github.com/search/users?q=`;
    
    if (inputUserInputName.value.length > 0) {
        apiUrl += `${chkBoxNameInputValue}`;
        console.log(apiUrl)
    }
    if (inputUserInputLocation.value.length > 0) {
        apiUrl += `+location:${chkBoxLocationInputValue}`;
        console.log(apiUrl)
    }
    if (inputUserInputPlanguauge.value.length > 0) {
        apiUrl += `+language:${chkBoxPlanguaugeInputValue}`;
        console.log(apiUrl)
    }
    
    console.log(apiUrl)

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
            
            let response = JSON.parse(req.responseText);
            // console.log(req.responseText)
            
            userArray = response;
            for (let i in response["items"]) {
                    console.log(response["items"][i])
               
                    document.getElementById('dtarget').insertAdjacentHTML('beforeend', `<p> ${response["items"][i]["login"]}</p>`);
            
            }
            // let resultHTML = `
            //     <p>${response.items[0].login}</p>
               
            //     `
            // dTarget.innerHTML = resultHTML;
        });
        req.open("GET", `${apiUrl}`); //url is defined on top
        req.setRequestHeader('Authorization', `${apikey}`); // apikey is hidden in config.js
    
        req.send();

}


//once display button is clicked, if checkbox is checked, grab input data before calling api
function searchGit() {
    displayBtn.addEventListener("click", function() {
        if (chkBoxName.checked == true) {
            chkBoxNameInputValue = inputUserInputName.value;
            }
        if (chkBoxLocation.checked == true) {
            chkBoxLocationInputValue = inputUserInputLocation.value;
            }
        if (chkBoxPlanguage.checked == true) {
            chkBoxPlanguaugeInputValue = inputUserInputPlanguauge.value;
            }
        runAPI()    
        })
       
        }
   

function runScript() {
    displayFields();
    searchGit();
    
}

runScript();
