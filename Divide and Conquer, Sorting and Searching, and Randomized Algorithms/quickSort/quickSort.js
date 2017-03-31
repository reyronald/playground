exports = module.exports = quickSort;

function quickSort(input, choosePivot, beforeStart = () => {}) {
  beforeStart(input);

  if (input.length <= 1) {
    return input;
  }

  const {pivot, pivotKey} = choosePivot(input);
  const {output, pivotEndedUpAt} = partition(input, pivot, pivotKey);

  const firstHalf = quickSort( output.slice(0, pivotEndedUpAt), choosePivot, beforeStart );
  const secondHalf = quickSort( output.slice(pivotEndedUpAt + 1), choosePivot, beforeStart );

  return [...firstHalf, pivot, ...secondHalf];
}

// Partitions the array around a pivot without allocating any new memory
function partition(input, pivot, pivotKey) {
  const swap = (array, x, y) => [ array[x], array[y] ] = [ array[y], array[x] ];
  swap(input, pivotKey, 0);
  let i = 1;
  for (let j = i; j < input.length; j++) {
     if (input[j] < pivot) {
       swap(input, i++, j);
     }
  }

  swap(input, 0, i - 1);
  return { output: input, pivotEndedUpAt: i - 1 };
}

// Partitions the array around a pivot by allocating an extra array
function pivotAround(input, pivot, pivotKey) {
  const output = [];
  let l = 0;
  let r = input.length - 1;
  input.forEach((element, key) => {
    if (pivotKey !== key) {
      output[ element > pivot ? r-- : l++] = element;
    }
  });
  output[l] = pivot;
  return {output, pivotEndedUpAt: l};
}

