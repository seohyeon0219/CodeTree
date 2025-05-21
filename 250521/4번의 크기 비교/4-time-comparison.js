const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split('\n');

let a = Number(input[0]);
let arr = input[1].trim().split(' ');

let b = Number(arr[0]);
let c = Number(arr[1]);
let d = Number(arr[2]);
let e = Number(arr[3]);

if (a > b) {
    console.log(1);
} else {
    console.log(0);
}

if (a > c) {
    console.log(1);
} else {
    console.log(0);
}

if (a > d) {
    console.log(1);
} else {
    console.log(0);
}

if (a > e) {
    console.log(1);
} else {
    console.log(0);
}