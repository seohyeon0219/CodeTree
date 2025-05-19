const fs = require("fs");
let input = fs.readFileSync(0).toString();
input = Number(input);

console.log(input);

if (input < 0){
    console.log('minus');
}