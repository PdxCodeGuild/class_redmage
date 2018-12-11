let target = document.getElementById("target");

let textTarget = document.getElementById("textTarget");

let pageNum = document.getElementById("pageInputOption");

let indexNum = document.getElementById("indexInputOption");

let submitButton = document.getElementById("submit");

let filterInput = document.getElementById("filter");

let numberOfResults = document.getElementById("numberOfResults")

let removeAllButton = document.getElementById("removeAll")

// Used to give page dropdown value from 1 to 10
for (let i=1; i < 11; i++) {
    let newPage = document.createElement("option");
    newPage.value = i;
    newPage.innerText = i;
    pageNum.appendChild(newPage);
};

// Submits filter function
submitButton.addEventListener("click", function(e) {
    
    let req = new XMLHttpRequest();

    req.addEventListener("progress", function(e) {
        // console.log(e.loaded);
    });

    req.addEventListener("error", function(e) {
        
        console.log(e.status);
        
        target.innerText = "Cannot load quote. Try again later!";

    });

    req.addEventListener("load", function(e) {        
        let response = JSON.parse(req.responseText);
        
        for (let i=0; i < numberOfResults.value; i++) {

            let randomNum = Math.floor(Math.random() * 25)
            
            let resultHTML = ` <p>${response.quotes[randomNum].body}</p> <p><i><a href="${response.quotes[randomNum].url}">${response.quotes[randomNum].author}</a></i></p> `;

            textTarget.innerHTML += resultHTML;
        };

        // filterInput.value = "";
    });

    req.open("GET", `https://favqs.com/api/quotes?page=${pageNum.value}&filter=${filterInput.value}`);

    req.setRequestHeader("Authorization", `Token token=${apiKey}`);

    req.send()
});


// Remove All
removeAllButton.addEventListener("click", function(e) {

    let targetLen = textTarget.getElementsByTagName("p");

    for (let i=targetLen.length - 1; i > -1; i--) {
        targetLen[i].remove();
    };
});




















// Used to look up indexes
// indexNum.addEventListener("click", function(e) {
//     let req = new XMLHttpRequest();

//     req.addEventListener("progress", function(e) {
//         // console.log(e.loaded);
//     });

//     req.addEventListener("error", function(e) {
        
//         console.log(e.status);
        
//         target.innerText = "Cannot load quote. Try again later!";

//     });
    
//     req.addEventListener("load", function(e) {
//         let response = JSON.parse(req.response);

//         let indexCounter = 1;
//         for (let i = 0; i < response.quotes.length; i++) {
//             let newIndex = document.createElement("option");
//             newIndex.value = i;
//             newIndex.innerText = `${indexCounter}.) ${response.quotes[i].body}`;
            
//             indexNum.appendChild(newIndex);

//             indexCounter++;
//         }


//     });

//     req.open("GET", "https://favqs.com/api/quotes");

//     req.setRequestHeader("Authorization", `Token token=${apiKey}`);

//     req.send()

// });