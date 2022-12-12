const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    let height= [];
    
    for(let i = 1; i <= Number(input[0]); i++) {
    height.push('*');
    console.log(height.join(''))
        
    }

});