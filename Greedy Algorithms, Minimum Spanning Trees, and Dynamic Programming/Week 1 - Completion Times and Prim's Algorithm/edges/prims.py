from collections import defaultdict

class Graph:
    INFINITY = float('inf')

    def __init__(self):
        self.graph = defaultdict(set)
        self.vertices = set()

    def add_edge(self, head, tail, weight):
        self.graph[head].add((tail, weight))
        self.graph[tail].add((head, weight))
        self.vertices.add(head)
        self.vertices.add(tail)

    def mst(self, start):
        unvisited_nodes, dist, prev = self._initialize(start)

        while unvisited_nodes:
            min_node = self.__minimum_distance(dist, unvisited_nodes)

            for vertex, weight in self.graph[min_node]:
                if weight < dist[vertex] and vertex in unvisited_nodes:
                    dist[vertex] = weight
                    prev[vertex] = min_node

            unvisited_nodes.remove(min_node)

        return dist, prev

    def mst_cost(self):
        start = next(iter(self.vertices))
        dist, prev = self.mst(start)
        return sum(dist.values())

    def _initialize(self, start):
        unvisited_nodes = set([start])
        dist = dict()
        prev = dict()
        for vertex in self.vertices:
            dist[vertex] = Graph.INFINITY
            prev[vertex] = None
            unvisited_nodes.add(vertex)

        dist[start] = 0

        return unvisited_nodes, dist, prev

    def __minimum_distance(self, dist, unvisited_nodes):
        min_node = None
        for vertex in unvisited_nodes:
            if min_node is None or dist[vertex] < dist[min_node]:
                min_node = vertex
        return min_node

def test_case_0():
    graph = Graph()
    graph.add_edge('A', 'B', 2)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('A', 'D', 3)
    graph.add_edge('B', 'C', 4)
    graph.add_edge('B', 'E', 3)
    graph.add_edge('C', 'D', 5)
    graph.add_edge('C', 'F', 6)
    graph.add_edge('C', 'E', 1)
    graph.add_edge('D', 'F', 7)
    graph.add_edge('E', 'F', 8)
    graph.add_edge('F', 'G', 9)
    cost = graph.mst_cost()
    assert cost == 24

def test_case_1():
    path = 'D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 1\edges\edges_tc1_answer_14.txt'
    graph = get_graph_input(path)
    cost = graph.mst_cost()
    assert cost == 14

def assignemnt():
    path = 'D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 1\edges\edges.txt' # -3612829
    graph = get_graph_input(path)
    cost = graph.mst_cost()
    assert cost == -3612829
    print cost

def get_graph_input(path):
    graph = Graph()
    with open(path) as fin:
        next(fin)
        for line in fin:
            if not line:
                break
            head, tail, weight = map(int, line.rstrip().split(' '))
            graph.add_edge(head, tail, weight)
    return graph

def main():
    test_case_0()
    test_case_1()
    assignemnt()
    return

if __name__ == '__main__':
    main()
