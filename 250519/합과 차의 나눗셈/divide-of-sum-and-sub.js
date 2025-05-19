const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(' ');

let a = Number(input[0]);
let b = Number(input[1]);

let plus = a + b;
let minus = a - b;

result = plus / minus;

console.log(result.toFixed(2));