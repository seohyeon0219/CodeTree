const fs = require("fs");
let input1 = fs.readFileSync(0).toString().split('\n');
let input2 = fs.readFileSync(0).toString();

let a = input1[0];
let b = input1[1];
let c = input2;

console.log(a,b,c);