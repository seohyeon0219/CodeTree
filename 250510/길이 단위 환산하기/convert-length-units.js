const fs = require("fs");
let ft = fs.readFileSync(0).toString().trim();
modified_ft = Number(ft) * 30.48;
console.log(modified_ft.toFixed(1));