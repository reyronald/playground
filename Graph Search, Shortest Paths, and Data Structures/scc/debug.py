# graph representations:
# http://www.cs.princeton.edu/courses/archive/fall07/cos226/lectures/digraph.pdf

from graph2 import Graph

GRAPH = {
  1: [4],
  4: [7],
  9: [3,7],
  7: [1],
  3: [6],
  6: [9],
  8: [5,6],
  5: [2],
  2: [8]
}

#result = Graph.create_from_dict(GRAPH).find_scc()
#assert result == '3,3,3,0,0'

result = Graph.create_from_file("D:/repos/playground/Graph Search, Shortest Paths, and Data Structures/scc/tc3.txt").find_scc()
assert result == '3,3,1,1,0'

print result
