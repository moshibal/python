//3rd party module to read the file from user console.
const readlineSync = require("readline-sync");
// # Rock
const rock = `
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
`;

//Paper
const paper = `
     _______
---'    ____)____
           ______)
          _______)
         ______)
---.__________)
`;

//  Scissors
const scissors = `
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
`;
console.log("let's play rock paper scissors with the computer.");

console.log("Please choose 0 for rock, 1 for paper and 2 for scissors.");
let person = Number(readlineSync.question());

//had to multiby by 3 as math.floor round down to the lowest interger.
const computer = Math.floor(Math.random() * 3);

//for person
if (person === 0) {
  console.log(`you have choosen rock\n ${rock}`);
} else if (person === 1) {
  console.log(`you have choosen paper\n ${paper}`);
} else if (person === 2) {
  console.log(`you have choosen scissors\n ${scissors}`);
} else {
  console.log(`please play game with the rules.`);
}
//for computer
if (computer === 0) {
  console.log(`computer has choosen rock\n ${rock}`);
} else if (computer === 1) {
  console.log(`computer has choosen paper\n ${paper}`);
} else if (computer === 2) {
  console.log(`computer has choosen scissors\n ${scissors}`);
}
//logic of the game
if (person === computer) {
  console.log("Thats a very tight game, its a draw!");
} else if (person === 0 && computer == 1) {
  console.log("you lose!");
} else if (person === 0 && computer == 2) {
  console.log("you win!");
} else if (person === 1 && computer == 2) {
  console.log("you lose!");
} else if (person === 2 && computer == 1) {
  console.log("you win!");
} else if (person === 1 && computer == 0) {
  console.log("you win!");
} else if (person === 2 && computer == 0) {
  console.log("you lose!");
} else {
  console.log("you have choosen wrong number, so you lose the game.");
}
