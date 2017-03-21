const fs = require('fs');
const { Vertex } = require('./minCut');

function getVerticesFromFile(filePath) {
  const fileContents = fs.readFileSync(filePath, { encoding: 'utf8' }).trim();
  return getVerticesFromString(fileContents);
}

function getVerticesFromString(string) {
  const verticesIterable = string.split('\r\n').filter(s => s).map(line => {
    const integers = line.split(/\t|\s/).filter(s => s);
    const label = +integers[0];
    // const adjacentVertices = new Set(integers.slice(1).map(n => +n));
    const adjacentVertices = integers.slice(1).map(n => +n);
    return [label, new Vertex(label, adjacentVertices)];
  });
  return new Map(verticesIterable);
}

exports = module.exports = {
  getVerticesFromFile,
  getVerticesFromString,
};
