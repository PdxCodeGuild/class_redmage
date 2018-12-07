//Word List From PDX Code Guild
let listWords = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it","yes","Most likely","Outlook good","Yes,Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Dont count on it", "My reply is no","My sources say no","Outlook not so good","Very doubtful"];

let eightballRandomnum = Math.floor(Math.random() * listWords.length);

let eightballChoice = listWords[eightballRandomnum];





alert("Welcome To The Magic Eightball Game!!!");
let btn = document.getElementById("btnSubmit")
let userText = document.getElementById("inputText")

btn.addEventListener ("click", function(){
    alert(`The answer to your question is ${eightballChoice}`);
})




