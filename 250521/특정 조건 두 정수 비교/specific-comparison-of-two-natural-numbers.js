const fs = require("fs");
let arr = fs.readFileSync(0).toString().trim().split(" ");

let a = Number(arr[0]);
let b = Number(arr[1]);
let result1 = 0;
let result2 = 0;

if (a < b) {
    result1 = 1;
} else {
    result1 = 0;
}

if (a === b) {
    result2 = 1;
} else {
    result2 = 0;
}

console.log(result1, result2);