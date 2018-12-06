//Word List From PDX Code Guild
let listWords = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it","yes","Most likely","Outlook good","Yes,Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Dont count on it", "My reply is no","My sources say no","Outlook not so good","Very doubtful"];

let eightballRandom = Math.floor(Math.random() * listWords.length);

let eightballChoice = listWords[eightballRandom];




while (true) {
    alert("Welcome To The Magic Eightball Game!!!");
    let askQuestion = prompt("Ask The Magic Eightball A Question? > ");
    alert(`The answer to your question is ${eightballChoice}`);
    let another_question = prompt('Would You like To Ask The Eight Ball Another Questions? Type 1.) for yes and 2.) for no');
    if (another_question == 2) {
        break
    }
    else if (another_question == 1) {
        continue
    }
    else {
        alert("You Selected an Invalid Character. Quitting Program Anyways")
        break
    }
}