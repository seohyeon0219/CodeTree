const fs = require("fs");
let arr = fs.readFileSync(0).toString().trim().split(" ");
let a = arr[0];
let b = arr[1];
// temp = a;
// a = b;
// b = temp;
[a, b] = [b, a]
console.log(a, b);