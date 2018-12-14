
let pdisplayText = document.getElementById("ddisplay-test");
let idisplayBtn = document.getElementById("idisplay-button");
let inextPageBtn = document.getElementById("inext-button");
let ipreviousPageBtn = document.getElementById("iprevious-button");
let isearchText;
let pagenum = 1;





function executeDisplay(){

    let isearchText = document.getElementById("isearch-text").value;
    // if (isearchText.length > 0) {    
    //     let filter = `&filter=${isearchText}`
    //     let siteurl = `https://favqs.com/api/quotes/?page=${pagenum}${filter}`;
    //     }
    //     if (isearchText == ""){
    //         let siteurl = `https://favqs.com/api/quotes/?page=${pagenum}`;
    //     }

    let filter = `&filter=${isearchText}`
    let siteurl = `https://favqs.com/api/quotes/?page=${pagenum}${filter}`; 
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

        pdisplayText.innerText = "";
        response = JSON.parse(req.responseText);
        console.log(response.quotes);
        for (let i in response.quotes) {
            //console.log(response.quotes[i]);
            let resultHTML = `
            ${response.quotes[i].body}
            `;
            let resultAnchor = `
            ${response.quotes[i].url}`

                var para = document.createElement("p");
                var node = document.createTextNode(resultHTML);
                para.appendChild(node);
                pdisplayText.appendChild(para)
                var anc = document.createElement("a");
                
                anc.setAttribute('href',resultAnchor);
                anc.innerHTML = "CLick Me To Go To Quote";
                pdisplayText.appendChild(anc);
            }
            
    
    })
        req.open("GET", siteurl);
        req.setRequestHeader("Authorization", `Token token="${apikey}"`);
        req.send();
    }

idisplayBtn.addEventListener("click", function() {
    executeDisplay()
    
})

ipreviousPageBtn.addEventListener("click", function() {
    pagenum -= 1;
    executeDisplay()
})

inextPageBtn.addEventListener("click", function() {
    pagenum += 1;
    executeDisplay()
})
    

   
   

    

    


// var para = document.createElement("p");
//     var node = document.createTextNode(response);
//     para.appendChild(node);
//     pdisplayText.appendChild(para);
