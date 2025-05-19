const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(' ');
let a = Number(input[0]);
let b = Number(input[1]);
let c = Number(input[2]);

sum = a + b + c;
average = sum / 3;
console.log(sum + '\n' + average + '\n' + sum - average);