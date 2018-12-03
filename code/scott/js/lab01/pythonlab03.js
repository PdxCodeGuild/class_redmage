// collecting input from the user as an integer
var score = prompt("What was your score on the exam?");

score = Number(score);
//score = int(input("What was your score on the exam?"))

// determining the letter grade
if (score <= 100 && score >= 90) {
    var grade = "A";
} else if (score < 90 && score >= 80) {
    var grade = "B";
} else if (score < 80 && score >= 70) {
    var grade = "C";
} else if (score < 70 && score >= 60) {
    var grade = "D";
} else {
    var grade = "F";
}
// if score in range(90, 100):
//     grade = "A"
// elif score in range(80, 89):
// grade = "B"
// elif score in range(70, 79):
// grade = "C"
// elif score in range(60, 69):
// grade = "D"
// elif score < 60:
// grade = "F"


// determining if there is the need for a + or -
if (score % 10 >= 0 && score % 10 <= 3) {
    var gradeplus = "-";
} else if (score % 10 >= 8 && score % 10 <= 9) {
    var gradeplus = "+";
}  
// if score % 10 in range(0, 3):
//         gradeplus = "-"
// elif score % 10 in range(8, 9):
// gradeplus = "+"


// sending responses, includes catch for A + not caught by 'gradeplus' determination
if (grade == "F") {
    document.write(`You have failed!`);
} else if (score == 100) {
    document.write(`You got an A+!`)
} else {
    document.write(`Your grade is ${grade}${gradeplus}`)
}
// if grade == "F":
//     print("You have failed!")
// elif score == 100:
// print("You got an A+!")
// else:
// print(f"Your grade is {grade}{gradeplus}!")
