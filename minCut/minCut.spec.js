const assert = require('assert');
const { getVerticesFromFile } = require('./minCut.utils');
const { findMinCut, Vertex } = require('./minCut');

const testCases = [
  { input: getVerticesFromFile('./TC1.txt'), expected: 2 },
  { input: getVerticesFromFile('./TC2.txt'), expected: 2 },
  { input: getVerticesFromFile('./TC3.txt'), expected: 1 },
  { input: getVerticesFromFile('./TC4.txt'), expected: 1 },
  { input: getVerticesFromFile('./TC5.txt'), expected: 3 },
  { input: getVerticesFromFile('./TC6.txt'), expected: 2 },
  {
    input: new Map([
      [2, new Vertex(2, [3,3,3])],
      [3, new Vertex(3, [2,2,2,3,3,3,3,8,8,8])],
      [8, new Vertex(8, [3,3,3])],
    ]),
    expected: 3
  },
  { input: getVerticesFromFile('./kargerMinCut.txt'), expected: 17 },
];

describe('Karger Min Cut', function() {
  this.timeout(0);

  testCases.forEach((testCase, key) => {
    it(`Case ${+key+1}`, () => {
      assert.equal( findMinCut(testCase.input), testCase.expected );
    });
  });
});
