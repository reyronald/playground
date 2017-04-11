# graph representations:
# http://www.cs.princeton.edu/courses/archive/fall07/cos226/lectures/digraph.pdf

from scc.graph2 import Graph

ROOT = "D:/repos/playground/Graph Search, Shortest Paths, and Data Structures/scc/"

RESULT = Graph.create_from_file(ROOT + "tc1.txt").find_scc()
assert RESULT == '3,3,3,0,0'

RESULT = Graph.create_from_file(ROOT + "tc2.txt").find_scc()
assert RESULT == '3,3,2,0,0'

RESULT = Graph.create_from_file(ROOT + "tc3.txt").find_scc()
assert RESULT == '3,3,1,1,0'

RESULT = Graph.create_from_file(ROOT + "tc3.txt").find_scc()
assert RESULT == '3,3,1,1,0'

RESULT = Graph.create_from_file(ROOT + "tc4.txt").find_scc()
assert RESULT == '7,1,0,0,0'

RESULT = Graph.create_from_file(ROOT + "tc5.txt").find_scc()
assert RESULT == '6,3,2,1,0'

print RESULT
