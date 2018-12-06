let textArea = document.getElementById("text-area");
let wholeDoc = document.getElementById("whole-doc");
let displayText = document.getElementById("pre-display");
let displaydivText = document.getElementById("display-text").outerHTML;


textStart = 0
textEnd = 50
wholeDoc.addEventListener("keydown", function() {
    let newtext = textArea.innerHTML
    let newText2 = newtext.slice(textStart,textEnd);
    textStart = textEnd;
    textEnd =  textEnd + 10;
    displayText.innerHTML += newText2;
    let x  = Math.floor(Math.random() * 10)
    console.log(x)
    if (x == 9){
        
        let myWindow = window.open('','MsgWindow','width=200,height=100', "menubar=no");
        myWindow.document.write("<p>You Have Been Hacked Suckka</p>")
        let doc = myWindow.document;
        doc.open();
        doc.write(displaydivText);
        doc.close();
        }

})