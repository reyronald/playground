from dijkstra import Graph
import os

def from_file():
    instance = Graph()
    path = os.path.join(os.path.dirname(__file__), 'dijkstraData.txt')
    testfile = open(path, 'r')
    while testfile:
        line = testfile.readline().rstrip()
        if not line:
            break
        values = line.split('\t')
        head = int(values.pop(0))
        for pair in values:
            tail, weight = map(int, pair.split(','))
            instance.add_edge(head, tail, weight)
    return instance

def get_answer():
    graph = from_file()

    dist = graph.dijkstra(1)

    nodes_to_examine = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    node_distances = []
    while nodes_to_examine:
        node_distances.append(dist[nodes_to_examine.pop(0)])

    return ','.join(map(str, node_distances))

print get_answer()
