const fs = require("fs");
let n = fs.readFileSync(0).toString().trim();
n = Number(n);
console.log(n.toFixed(2));