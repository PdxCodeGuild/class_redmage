let urlList = ["https://www.google.com/", "https://www.wikipedia.org/", "https://www.cnn.com/", "https://www.facebook.com/\n"]

function randomNum() {
    let x = Math.floor(Math.random() * urlList.length);
    return x;
}

// Version 1

// setInterval(function() {
//     let testy = urlList[randomNum()];
//     window.location = testy;
// }, 5000);

// Version 2

let counter = 5;


let interval = setInterval(function() {

    let parent = document.getElementById("h1-wrapper");
    let elementExists = document.getElementById("h1");
        
        if (elementExists === null) {
            var countDown = document.createElement("h1");
            countDown.id = "h1"
            countDown.textContent = `Page change in ${counter} seconds.`;
            parent.appendChild(countDown);
        } else {
            document.getElementById("h1").remove();
            var countDown = document.createElement("h1");
            countDown.id = "h1"
            countDown.textContent = `Page change in ${counter} seconds.`;
            parent.appendChild(countDown);
        }


    console.log(counter);
    counter -= 1;

    if (counter === 0) {
        let testy = urlList[randomNum()];
        window.location = testy;
    }

}, 1000);
