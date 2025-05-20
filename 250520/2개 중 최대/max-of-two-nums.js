const fs = require("fs");
let arr = fs.readFileSync(0).toString().trim().split(' ');

let a = Number(arr[0]);
let b = Number(arr[1]);

if (a > b) {
    console.log(a);
} else {
    console.log(b);
}