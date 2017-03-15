const assert = require('assert');
const quickSort = require('./quickSort');

const testCases = [
  { input: [], expected: [] },
  { input: [1], expected: [1] },
  { input: [1,2], expected: [1,2] },
  { input: [2,1], expected: [1,2] },
  { input: [2,3,1], expected: [1,2,3] },
  { input: [2,3,1,4], expected: [1,2,3,4] },
  { input: [2,2,3,1,4,1], expected: [1,1,2,2,3,4] },
  { input: [3,8,2,5,1,4,7,6], expected: [1,2,3,4,5,6,7,8] },
];

describe('QuickSort', () => {
  Object.keys(testCases).forEach(key => {
    it(`Case ${+key+1}`, () => {
      const testCase = testCases[key];
      const output = quickSort(testCase.input);
      assert.deepEqual(output, testCase.expected);
    });
  });
});
