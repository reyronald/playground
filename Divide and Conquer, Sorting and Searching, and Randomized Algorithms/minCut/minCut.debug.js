const fs = require('fs');
const {
  Vertex,
  findMinCut,
  minCut
} = require('./minCut');
const {
  getVerticesFromFile,
  getVerticesFromString,
} = require('./minCut.utils');

// Reading input
// const vertices = getVerticesFromFile('D:/repos/playground/minCut/TC1.txt');
// const vertices = new Map([
//   [1, new Vertex(1, [2,3])],
//   [2, new Vertex(2, [1,3,4])],
//   [3, new Vertex(3, [1,2,4])],
//   [4, new Vertex(4, [2,3])],
// ]);

const vertices = new Map([
  [2, new Vertex(2, [3,3,3])],
  [3, new Vertex(3, [2,2,2,3,3,3,3,8,8,8])],
  [8, new Vertex(8, [3,3,3])],
]);

const result = findMinCut(vertices);
console.log(result);
