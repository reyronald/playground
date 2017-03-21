class Vertex {
  // label: number;
  // adjacentVertices: number[];

  constructor(label, adjacentVertices) {
    this.label = label;
    this.adjacentVertices = adjacentVertices;
  }
}

function findMinCut(vertices /*: Map<number, Vertex>*/) {
  const trials = [];
  const numberOfTrials = vertices.size * vertices.size;
  for (let index = 0; index < 200*200; index++) {
    trials.push(minCut(new Map(vertices)));
  }
  return Math.min(...trials);
}

function minCut(refVertices /*: Map<number, Vertex>*/) {
  const vertices = new Map();
  for (let [key, value] of refVertices.entries()) {
    vertices.set(key, new Vertex(value.label, [...value.adjacentVertices]));
  }

  while (vertices.size > 2) {
    // Pick remaining edge uniformly at random
    const randomPointA = pickRandomValueFromMap(vertices); 
    const randomPointB = pickRandomValueFromArray(vertices.get(randomPointA.label).adjacentVertices);

    // Removing picked edge from both endpoints
    removeElementFromArray(randomPointA.adjacentVertices, randomPointB);
    removeElementFromArray(vertices.get(randomPointB).adjacentVertices, randomPointA.label);

    // Rearranging remaining edges
    randomPointA.adjacentVertices = [...randomPointA.adjacentVertices, ...vertices.get(randomPointB).adjacentVertices];
    removeSelfLoops(randomPointA);
    vertices.get(randomPointB).adjacentVertices.forEach(adjacentVertex => {
        const index = vertices.get(adjacentVertex).adjacentVertices.indexOf(randomPointB);
        vertices.get(adjacentVertex).adjacentVertices[index] = randomPointA.label;
    });
    vertices.delete(randomPointB);
  }
  vertices.forEach(v => removeSelfLoops(v));
  return vertices.values().next().value.adjacentVertices.length;
}

function pickRandomValueFromMap(map) {
  const index = getRandom(map.size);
  return map.get([...map.keys()][index]);
}

function pickRandomValueFromArray(array) {
  const index = getRandom(array.length);
  return array[index];
}

function getRandom(size) {
  return Math.round(Math.random() * --size);
}

function removeElementFromArray(array, element) {
  const index = array.indexOf(element);
  if (index !== -1) {
    array.splice(index, 1);
    return true;
  }
  return false;
}

function removeSelfLoops(vertex) {
  let index = vertex.adjacentVertices.indexOf(vertex.label);
  while (index !== -1) {
    vertex.adjacentVertices.splice(index, 1);
    index = vertex.adjacentVertices.indexOf(vertex.label);
  }
}

exports = module.exports = {
  Vertex,
  findMinCut,
  minCut
};
