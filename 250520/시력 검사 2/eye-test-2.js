const fs = require("fs");
let eye = fs.readFileSync(0).toString();

if (eye >= 1.0) {
    console.log('High');
} else if (eye >= 0.5) {
    console.log('Middle');
} else {
    console.log('Low');
}