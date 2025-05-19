const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(' ');

let height = Number(input[0]);
let width = Number(input[1]);

let bmi = parseInt((10000 * width) / (height * height));
console.log(bmi);
if (bmi >= 25) {
    console.log('Obesity');
}