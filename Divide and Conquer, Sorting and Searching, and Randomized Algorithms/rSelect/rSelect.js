function rSelect(input, orderStatistic) {
  if (input.length < 2) {
    return input[0];
  }

  const {pivot, pivotKey} = chooseRandomPivot(input);
  const {output, pivotEndedUpAt} = partition(input, pivot, pivotKey);
  
  if (pivotEndedUpAt === orderStatistic) {
    return output[pivotEndedUpAt];
  } else if (pivotEndedUpAt > orderStatistic) {
    return rSelect(output.slice(0, pivotEndedUpAt), orderStatistic)
  } else {
    return rSelect(output.slice(pivotEndedUpAt), orderStatistic - pivotEndedUpAt);
  }
}

function chooseRandomPivot(input) {
  const pivotKey = Math.floor( Math.random() * input.length);
  return { pivot: input[pivotKey], pivotKey };
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
