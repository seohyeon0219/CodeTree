const fs = require("fs");
let score = fs.readFileSync(0).toString();

score = Number(score);

if (score === 100) {
    console.log('pass');
} else {
    console.log('failure');
}