const fs = require('fs');
const {
  Vertex,
  Edge,
  minCut
} = require('./minCut');
const {
  getVerticesFromFile,
  getVerticesFromString,
} = require('./minCut.utils');


// Reading input
const vertices = getVerticesFromFile('./kargerMinCut.txt');

console.log(vertices[0]);
