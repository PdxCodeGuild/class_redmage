let userText = document.getElementById("inputText");
let btn = document.getElementById("userButton");





btn.addEventListener("click", function(evt){
    console.log(grade);
    if (grade == 100) {
        var plusminus = '+';
    }
    else if (grade % 5 == 0) {
        var plusminus = '';
    }
    else if (grade % 10 > 5) {
        var plusminus = '+';
    }
    else if (grade % 10 <= 5) {
        var plusminus = '-';
    }
    if (grade >= 90 && grade < 100) {
        alert(`You Got An "A${plusminus}" Grade`);
    }
    else if (grade >= 80 && grade < 90) {
        alert(`You Got An "B ${plusminus}" Grade`);
    }
    else if (grade >= 70 && grade < 80) {
        alert(`You Got An "C${plusminus}" Grade`);
    }
    else if (grade >= 60 && grade < 70) {
        alert(`You Got An "D${plusminus}" Grade`);
    }
    else if (grade < 60) {
        alert(`You Got An "F" Grade`);
    }
    else {
        alert(`You Typed An Invalid Argument`);
    }
    
})

