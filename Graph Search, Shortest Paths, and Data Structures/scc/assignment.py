# graph representations:
# http://www.cs.princeton.edu/courses/archive/fall07/cos226/lectures/digraph.pdf

import time
from graph2 import Graph

ROOT = "e:/repos/playground/Graph Search, Shortest Paths, and Data Structures/scc/"

GRAPH = Graph.create_from_file(ROOT + "SCC.txt")

start = time.time()
RESULT = GRAPH.find_scc()
end = time.time()

print RESULT
print end - start

# 434821,971,459,313,278 WRONG
# 434821,971,459,313,304 WRONG
# 434821,968,459,313,304 WRONG
# 434821,968,459,313,278 WRONG mine
# 434821,968,459,313,211 WRONG
