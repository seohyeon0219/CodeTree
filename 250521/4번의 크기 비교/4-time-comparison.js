const fs = require("fs");
let a = fs.readFileSync(0).toString();
let arr = fs.readFileSync(0).toString().trim().split(" ");

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