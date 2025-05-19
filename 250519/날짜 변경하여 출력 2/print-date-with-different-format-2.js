const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split('-');

let month = input[0];
let day = input[1];
let year = input[2];

console.log(year+'.'+month+'.'+day);
