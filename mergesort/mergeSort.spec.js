const assert = require('assert');
const mergeSort = require('./mergeSort');

const testCases = [
  { input: [], expected: [] },
  { input: [1], expected: [1] },
  { input: [1,2], expected: [1,2] },
  { input: [2,1], expected: [1,2] },
  { input: [2,3,1], expected: [1,2,3] },
  { input: [2,3,1,4], expected: [1,2,3,4] },
];

describe('Merge Sort', () => {
  Object.keys(testCases).forEach(key => {
    it(`Case ${+key+1}`, () => {
      const testCase = testCases[key];
      const output = mergeSort(testCase.input);
      assert.deepEqual(output, testCase.expected);
    });
  });
});
