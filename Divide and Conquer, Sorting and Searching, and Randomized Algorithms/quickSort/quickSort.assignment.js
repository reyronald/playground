const fs = require('fs');
const quickSort = require('./quickSort');

// Reading input
// const integers = fs.readFileSync('./QuickSort.txt', { encoding: 'utf8' });
const integers = fs.readFileSync('./1000.txt', { encoding: 'utf8' });
const input = integers.split('\r\n').filter(s => s).map(n => +n);

// Arrange
let comparisons = -input.length;
const incrementComparisons = input => {
  comparisons += input.length;
};

// Actual work
const chooseFirstPivot = input => ({pivot: input[0], pivotKey: 0});
quickSort([...input], chooseFirstPivot, incrementComparisons);
console.log('Comparisons First Pivot' , comparisons);

comparisons = -input.length;
const chooseLastPivot = input => ({pivot: input[input.length - 1], pivotKey: input.length - 1});
quickSort([...input], chooseLastPivot, incrementComparisons);
console.log('Comparisons Last Pivot' , comparisons);

comparisons = -input.length;
const chooseMedianPivot = input => {
  const middleIndex = Math.floor( (input.length - 1) / 2);

  const first = input[0];
  const last = input[input.length - 1];
  const mid = input[middleIndex];

  const median = [first, last, mid].sort((a,b) => a - b)[1];
  const medianIndex = median === first ? 0 : (median === last ? input.length - 1 : middleIndex);
  return { pivot: median, pivotKey: medianIndex };
};
quickSort([...input], chooseMedianPivot, incrementComparisons);
console.log('Comparisons Median Pivot' , comparisons);


comparisons = -input.length;
const chooseRandomPivot = input => {
  const index = Math.floor(Math.random() * input.length);
  return { pivot: input[index], pivotKey: index };
};
quickSort([...input], chooseRandomPivot, incrementComparisons);
console.log('Comparisons Random Pivot' , comparisons);
