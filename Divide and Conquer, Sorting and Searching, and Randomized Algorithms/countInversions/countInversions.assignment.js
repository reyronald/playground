const fs = require('fs');
const countInversions = require('./countInversions');

const integers = fs.readFileSync('./IntegerArray.txt', { encoding: 'utf8' });

const input = integers.split('\r\n').filter(s => s).map(n => +n);

const output = countInversions(input);

console.log(output);
