# graph representations:
# http://www.cs.princeton.edu/courses/archive/fall07/cos226/lectures/digraph.pdf

from graph_recursive import Graph, create_from_file

ROOT = "d:/repos/playground/Graph Search, Shortest Paths, and Data Structures/scc/"

RESULT = create_from_file(ROOT + "tc1.txt").find_scc()
assert RESULT == '3,3,3,0,0'

RESULT = create_from_file(ROOT + "tc2.txt").find_scc()
assert RESULT == '3,3,2,0,0'

RESULT = create_from_file(ROOT + "tc3.txt").find_scc()
assert RESULT == '3,3,1,1,0'

RESULT = create_from_file(ROOT + "tc4.txt").find_scc()
assert RESULT == '7,1,0,0,0'

RESULT = create_from_file(ROOT + "tc5.txt").find_scc()
assert RESULT == '6,3,2,1,0'

RESULT = create_from_file(ROOT + "tc6.txt").find_scc()
assert RESULT == '3,1,1,0,0'

RESULT = create_from_file(ROOT + "tc7.txt").find_scc()
assert RESULT == '7,3,0,0,0'

####

RESULT = create_from_file(ROOT + "tc8.txt").find_scc()
assert RESULT == '4,2,1,1,1'

RESULT = create_from_file(ROOT + "tc9.txt").find_scc()
assert RESULT == '9,1,1,1,1'

print RESULT
