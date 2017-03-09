function mergeSort(values) {
  const middle = values.length / 2;
  if (middle < 1) {
    return values;
  }
  const left = mergeSort( values.slice(0, middle) );
  const right = mergeSort( values.slice(middle) );

  return merge(left, right);
}

function merge(left, right) {
  const output = [];
  let l = 0;
  let r = 0;
  while (output.length != (left.length + right.length)) {
    output.push(left[l] < right[r] || typeof right[r] === 'undefined' ? left[l++] : right[r++]);
  }
  return output;
}

exports = module.exports = mergeSort;
