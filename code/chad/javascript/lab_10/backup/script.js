//Define Where output text is going to
let dTarget = document.getElementById("dtarget"); 

//Page Buttons
let displayBtn = document.getElementById("input-display-btn");
let previousBtn = document.getElementById("input-previous-btn");
let nextBtn = document.getElementById("input-next-btn");


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

//setting up variable to use used later API Call
let chkBoxNameInputValue;
let chkBoxLocationInputValue;
let chkBoxPlanguaugeInputValue;
let pageNum = 0
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
function runAPI(e) {
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
    if (pageNum == 0) {

    }
    else if (pageNum != 0) {
        apiUrl += `&page=${pageNum}`;
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
                    console.log(response["items"][i]["url"])
                    e.defaultPrevented;
                    document.getElementById('dtarget').insertAdjacentHTML('beforeend', `
                    <div id="div-display-data">
                        <img style="width:100px;height:100px" src="${response["items"][i]["avatar_url"]}" alt="Githubimag">
                        <a href=${response["items"][i]["html_url"]}></iframe><p class="githubIds">${response["items"][i]["login"]}</p></a>
                    </div>
                    `);

                  
            }

        });
        req.open("GET", `${apiUrl}`); //url is defined on top
        req.setRequestHeader('Authorization',"token " + `${apikey}`); // apikey is hidden in config.js
                //make sure there is a space int he quote after "token "
        req.send();

}


//event listeners for buttons, once display button is clicked, if checkbox is checked, grab input data before calling api
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
    previousBtn.addEventListener("click", function() {
        pageNum --
        runAPI() 
    })

    nextBtn.addEventListener("click", function() {
        pageNum ++
        runAPI() 
        })
    }
       




function runScript() {
    displayFields();
    searchGit();
  
    
}

runScript();
