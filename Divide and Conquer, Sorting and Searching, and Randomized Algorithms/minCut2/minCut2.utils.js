const fs = require('fs');
const { Edge } = require('./minCut2');

function getEdgesFromFile(filePath) {
  const fileContents = fs.readFileSync(filePath, { encoding: 'utf8' }).trim();
  return getEdgesFromString(fileContents);
}

function getEdgesFromString(string) {
  const edges = new Map();
  string.split('\r\n').filter(s => s).forEach(line => {
    const integers = line.split(/\t|\s/).filter(s => s).map(n => +n);
    integers.slice(1).forEach(n => {
      const edge = new Edge(integers[0], n);
      edges.set(`${edge.point1}-${edge.point2}`, edge);
    });
  });
  return new Set(edges.values());
  // const edges = new Set();
  // string.split('\r\n').filter(s => s).forEach(line => {
  //   const integers = line.split(/\t|\s/).filter(s => s).map(n => +n);
  //   integers.slice(1).forEach(n => edges.add(new Edge(integers[0], n)))
  // });
  // return edges;
}

exports = module.exports = {
  getEdgesFromFile,
  getEdgesFromString,
};
