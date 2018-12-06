// variables

let g_choices;
let human_score;
let computer_choice;
let p_start;

function randomChoice(arr) {
    return arr[Math.floor(arr.length * Math.random())];
}

alert("Welcome to the Ol' Rock, Paper, Scissors Saloon!\n\nAs a reminder, rock beats scissors, paper covers rock, and scissors cuts paper!\n\nYou'll be engaged in mortal kombat with our world-famous champion Glorath!\n\nThe safe word is 'no'\nGame on!");

g_choices = ["rock","paper","scissors"];

human_score = 0;
computer_score = 0;

p_start = prompt("Do you want to play a game?");
p_start = p_start.toLowerCase();

while (p_start != "no") {

    let user_choice = prompt("Do you plan to throw rock, paper, or scissors?");
    user_choice = user_choice.toLowerCase();
    computer_choice = randomChoice(g_choices);

    if (user_choice == computer_choice) {

        alert("You and Glorath tie!");
        p_start = prompt("Do you want to continue?");
        p_start = p_start.toLowerCase();
    } else if (user_choice == g_choices[0] && computer_choice == g_choices[1]){
        alert("Glorath's paper covered your rock, oh no!");
        computer_score += 1;
        alert("Glorath's score: "+computer_score+" vs. your score: "+human_score);
        p_start = prompt("Do you want to continue?");
        p_start = p_start.toLowerCase();
    } else if (user_choice == g_choices[1] && computer_choice == g_choices[2]){

        alert("Glorath's scissors cut your paper, oh no!");
        computer_score += 1;
        alert("Glorath's score: "+computer_score+" vs. your score: "+human_score);
        p_start = prompt("Do you want to continue?");
        p_start = p_start.toLowerCase();
    } else if (user_choice == g_choices [2] && computer_choice == g_choices[0]){
        alert("Glorath's rock smashed your scissors, oh no!");
        computer_score += 1;
        alert("Glorath's score: "+computer_score+" vs. your score: "+human_score);
        p_start = prompt("Do you want to continue?");
        p_start = p_start.toLowerCase();
    } else if (user_choice == g_choices[0] && computer_choice == g_choices[2]){

        alert("You smashed Glorath's scissors, you're very lucky!");
        human_score += 1;
        alert("Glorath's score: "+computer_score+" vs. your score: "+human_score);
        p_start = prompt("Do you want to continue?");
        p_start = p_start.toLowerCase();
    } else if (user_choice == g_choices[1] && computer_choice == g_choices[0]){

        alert("You covered Glorath's rock, you're very lucky!");
        human_score += 1;
        alert("Glorath's score: "+computer_score+" vs. your score: "+human_score);
        p_start = prompt("Do you want to continue?");
        p_start = p_start.toLowerCase();
    } else if (user_choice == g_choices[2] && computer_choice == g_choices[1]){

        alert("You cut Glorath's paper, you're very lucky!");
        human_score += 1;
        alert("Glorath's score: "+computer_score+" vs. your score: "+human_score);
        p_start = prompt("Do you want to continue?");
        p_start = p_start.toLowerCase();
    } else {

        alert("Please choose: rock, paper, or scissors");
    }


}

alert(`"Glorath scored ${computer_score} while you scored ${human_score}!`);
alert("Thanks for playing!");