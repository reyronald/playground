# graph representations:
# http://www.cs.princeton.edu/courses/archive/fall07/cos226/lectures/digraph.pdf

import sys
import threading
import time

from graph_recursive import create_from_file
sys.setrecursionlimit(10**6)
threading.stack_size(2 ** 26)

def scc():
    root = "d:/repos/playground/Graph Search, Shortest Paths, and Data Structures/scc/"
    graph = create_from_file(root + "SCC.txt")

    start = time.time()
    result = graph.find_scc()
    end = time.time()

    print result # 434821,968,459,313,211
    print end - start # 7.65700006485 seconds

THREAD = threading.Thread(target=scc)
THREAD.start()
