const letters = [
  "a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
  "A",
  "B",
  "C",
  "D",
  "E",
  "F",
  "G",
  "H",
  "I",
  "J",
  "K",
  "L",
  "M",
  "N",
  "O",
  "P",
  "Q",
  "R",
  "S",
  "T",
  "U",
  "V",
  "W",
  "X",
  "Y",
  "Z",
];
const numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"];
let numberOfLetters;
let numberOfSymbols;
let numberOfNumbers;
document.getElementById("button").addEventListener("click", () => {
  let password = [];
  numberOfLetters = Number(
    prompt("please tell us how many letters you want to have?")
  );
  numberOfSymbols = Number(
    prompt("please tell us how many symbols you want to have?")
  );
  numberOfNumbers = Number(
    prompt("please tell us how many number you want to have?")
  );
  //generating random letters
  for (i = 0; i < numberOfLetters; i++) {
    const randomIndex = Math.floor(Math.random() * letters.length);
    password.push(letters[randomIndex]);
  }
  //generating random symbols
  for (i = 0; i < numberOfSymbols; i++) {
    const randomIndex = Math.floor(Math.random() * symbols.length);
    password.push(symbols[randomIndex]);
  }
  //generating random numbers
  for (i = 0; i < numberOfNumbers; i++) {
    const randomIndex = Math.floor(Math.random() * numbers.length);
    password.push(numbers[randomIndex]);
  }
  //using the lodash library to shuffle the array.
  const shuffleArray = _.shuffle(password);
  //joining lists in one string

  const ramdonPassword = shuffleArray.join("");

  const passwordDiv = document.getElementById("password");
  if (ramdonPassword) {
    passwordDiv.textContent = ramdonPassword;
  }
});
