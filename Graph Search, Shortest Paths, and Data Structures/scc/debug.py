# graph representations:
# http://www.cs.princeton.edu/courses/archive/fall07/cos226/lectures/digraph.pdf

from graph import Graph

GRAPH = {
    'S': set(['A', 'B']),
    'A': set(['S', 'B', 'C']),
    'B': set(['S', 'A', 'D']),
    'C': set(['A', 'D', 'E']),
    'D': set(['B', 'C', 'E']),
    'E': set(['C', 'D']),
}

# GRAPH = {
#     1: set([2,3]),
#     2: set([4]),
#     3: set([4]),
#     4: set([])
# }

GRAPH = {
    1: set([7]),
    2: set([5]),
    3: set([9]),
    4: set([1]),
    5: set([8]),
    6: set([3, 8]),
    7: set([4, 9]),
    8: set([2]),
    9: set([6]),
}

graph = Graph(GRAPH)

graph.scc()
