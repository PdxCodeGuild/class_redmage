let boxVar = document.getElementById("box-holder");
boxVar.addEventListener("click", function(e) {
    if (boxVar.className === "clicked") {
        boxVar.className = "";
    } else {
        boxVar.className = "clicked";
    };    
})


