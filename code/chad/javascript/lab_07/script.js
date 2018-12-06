let textArea = document.getElementById("text-area");
let wholeDoc = document.getElementById("whole-doc");


textStart = 0
textEnd = 50
wholeDoc.addEventListener("keydown", function() {
    let newtext = textArea.innerHTML
    let newText2 = newtext.slice(textStart,textEnd);
    textStart = textEnd
    textEnd =  textEnd + 10
    var para = document.createElement("p");
    var node = document.createTextNode(newText2);
    para.appendChild(node);

    var element = document.getElementById("pre-display");
    element.appendChild(para);
    para.appendChild(node);
    
})