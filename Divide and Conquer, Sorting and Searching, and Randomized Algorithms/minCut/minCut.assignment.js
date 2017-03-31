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
const vertices = getVerticesFromFile('./kargerMinCut.txt');
const result = findMinCut(vertices);
console.log(result);
