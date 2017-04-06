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

result = Graph.create_from_dict(GRAPH).find_scc()
assert result == '3,3,3,0,0'

root = "D:/repos/playground/Graph Search, Shortest Paths, and Data Structures/scc/"

result = Graph.create_from_file(root + "tc1.txt").find_scc()
assert result == '3,3,3,0,0'

result = Graph.create_from_file(root + "tc2.txt").find_scc()
assert result == '3,3,2,0,0'

result = Graph.create_from_file(root + "tc3.txt").find_scc()
assert result == '3,3,1,1,0'

result = Graph.create_from_file(root + "tc4.txt").find_scc()
assert result == '7,1,0,0,0'

result = Graph.create_from_file(root + "tc5.txt").find_scc()
assert result == '6,3,2,1,0'

print result
