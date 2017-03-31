class Edge {
  /**
   * @param {number} point1 
   * @param {number} point2 
   */
  constructor(point1, point2) {
    this.point1 = point1;
    this.point2 = point2;
    this.swapPointsIfNeeded();
  }

  swapPointsIfNeeded() {
    if (this.point1 > this.point2) {
      [this.point1, this.point2] = [this.point2, this.point1];
    }
  }

  /**
   * @param {number} from 
   * @param {number} to 
   */
  changeEndpoint(from, to) {
    if (this.point1 === from) {
      this.point1 = to;
    } 
    if (this.point2 === from) {
      this.point2 = to;
    }
    this.swapPointsIfNeeded();
  }

  isSelfLoop() {
    return this.point1 === this.point2;
  }

  toString() {
    return `[${this.point1},${this.point2}]`;
  }
}

/**
 * @param {Set<Edge>} edges 
 */
function findMinCut(edges) {
  const vertices = getVerticesFromEdges(edges);
  let numberOfTrials = vertices.size * vertices.size;
  let result = null;
  while (numberOfTrials--) {
    const edgesClone = cloneEdges(edges);
    const verticesClone = getVerticesFromEdges(edgesClone);
    const currentMinCut = minCut(verticesClone, edgesClone);
    if (result === null || currentMinCut < result) {
      result = currentMinCut;
    }
  }
  return result;
}

/**
 * @param {Set<Edge>} edges 
 */
function cloneEdges(edges) {
  const edgesClone = new Set();
  edges.forEach(edge => {
    edgesClone.add(new Edge(edge.point1, edge.point2));
  });
  return edgesClone;
}

/**
 * @param {Set<Edge>} edges 
 * @return {Map<number, Set<Edge>>}
 */
function getVerticesFromEdges(edges) {
  const vertices = new Map();
  for (let edge of edges) {
    if (!vertices.has(edge.point1)) {
      vertices.set(edge.point1, new Set());
    }
    if (!vertices.has(edge.point2)) {
      vertices.set(edge.point2, new Set());
    }
    vertices.get(edge.point1).add(edge);
    vertices.get(edge.point2).add(edge);
  }
  return vertices;  
}

/**
 * @param {Map<number, Set<Edge>>} vertices 
 * @param {Set<Edge>} edges 
 */
function minCut(vertices, edges) {
  while (vertices.size > 2) {
    const randomEdge = pickRandomValueFromSet(edges);
    
    vertices.get( randomEdge.point1 ).delete(randomEdge);
    vertices.get( randomEdge.point2 ).delete(randomEdge);
    
    vertices.get( randomEdge.point2 ).forEach(edge => {
      edge.changeEndpoint(randomEdge.point2, randomEdge.point1);
      if (edge.isSelfLoop()) {
        edges.delete(edge);
        vertices.get( randomEdge.point1 ).delete(edge);
      } else {
        vertices.get( randomEdge.point1 ).add(edge);
      }
    });

    vertices.delete(randomEdge.point2);
    edges.delete(randomEdge);
  }
  return edges.size;
}

function pickRandomValueFromSet(set) {
  // const compare = list.shift();
  // for (let val of set) {
  //   if (val.point1 === compare[0] && val.point2 === compare[1]) {
  //     return val;
  //   }
  // }

  const getRandom = size => Math.round(Math.random() * --size);
  const index = getRandom(set.size);
  return [...set.values()][index];
}

/**
 * @param {Set<Edge>} edges 
 */
function removeSelfLoops(edges) {
  for (let edge of edges) {
    if (edge.isSelfLoop()) {
      edges.delete(edge);
    }
  }
}

exports = module.exports = {
  Edge,
  findMinCut
};

/////////////////////////////

// const {
//   getEdgesFromFile,
// } = require('./minCut2.utils');

// const edges = getEdgesFromFile('D:/repos/playground/minCut/TC1.txt');

// const vertices = getVerticesFromEdges(edges);

// const result = findMinCut(edges);

// console.log(result);
