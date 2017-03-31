const assert = require('assert');
const { getEdgesFromFile } = require('./minCut2.utils');
const { findMinCut, Edge } = require('./minCut2');

const testCases = [
  { input: getEdgesFromFile('../minCut/TC1.txt'), expected: 2 },
  { input: getEdgesFromFile('../minCut/TC2.txt'), expected: 2 },
  { input: getEdgesFromFile('../minCut/TC3.txt'), expected: 1 },
  { input: getEdgesFromFile('../minCut/TC4.txt'), expected: 1 },
  { input: getEdgesFromFile('../minCut/TC5.txt'), expected: 3 },
  { input: getEdgesFromFile('../minCut/TC6.txt'), expected: 2 },
  { input: getEdgesFromFile('../minCut/kargerMinCut.txt'), expected: 17 },
];

describe('Karger Min Cut', function() {
  this.timeout(0);

  testCases.forEach((testCase, key) => {
    it(`Case ${+key+1}`, () => {
      assert.equal( findMinCut(testCase.input), testCase.expected );
    });
  });
});
