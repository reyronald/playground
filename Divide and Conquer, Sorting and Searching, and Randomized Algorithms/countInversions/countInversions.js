function countInversions(input) {
  return sortAndcount(input).count;
}

function sortAndcount(input) {
  if (input.length === 1) {
    return {list: input, count: 0};
  }

  const middle = input.length / 2;

  const {list: b, count: x} = sortAndcount( input.slice(0, middle) );
  const {list: c, count: y} = sortAndcount( input.slice(middle) );
  const {list: d, count: z} = mergeAndCountSplitInv(b, c);

  return {list: d, count: x + y + z};
}

function mergeAndCountSplitInv(left, right) {
  const list = [];
  let l = 0;
  let r = 0;
  let count = 0;
  while (list.length != (left.length + right.length)) {
    const leftIsSmaller = left[l] < right[r] || typeof right[r] === 'undefined';
    list.push( leftIsSmaller ? left[l++] : right[r++]);
    count += leftIsSmaller ? 0 : left.length - l;
  }
  return {list, count};
}

exports = module.exports = countInversions;
