// pythonlab013.js

// no string.ascii so I type it out. boooooooooooo
var alphaList = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];

// obtaining input message
var userMessage = prompt("Enter the string you would like to encode. >");
userMessage = userMessage.toUpperCase();

// obtaining cipher number
var cipherNum = prompt("How many numbers would you like to shift the cipher? (valid integers: 0 - 25) >");
Number(cipherNum);

// creating the cipher
var rotCipher = alphaList.slice(0, cipherNum);
var rotCipher2 = alphaList.slice(cipherNum, alphaList.length);
rotCipher = rotCipher2.concat(rotCipher);


// iterating through each letter in the user's message, finding the corresponding index, and creating list of those indeces
var encodedNums = [];
for (let i = 0; i < userMessage.length; i++) {
    let userLetter = userMessage[i];
    let indexNum = alphaList.indexOf(userLetter);
    encodedNums.push(indexNum);
}

document.write(encodedNums)

// iterating through the list of indeces to find the corresponding letter in the ROT cipher created earlier
var encodedMsg = [];
for (let i = 0; i < encodedNums.length; i++) {
    let newLetter = encodedNums[i];
    encodedMsg.push(rotCipher[newLetter]);
}

encodedMsg.join();

document.write(`Your encoded message is: ${encodedMsg}`);