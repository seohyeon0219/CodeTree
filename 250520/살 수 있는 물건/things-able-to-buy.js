const fs = require("fs");
let money = fs.readFileSync(0).toString();

money = Number(money);

if (money >= 3000) {
    console.log('book');
} elif (money >= 1000) {
    console.log('mask');
} else {
    console.log('no');
}