from collections import defaultdict

class Graph:
    # INFINITY = float('inf')
    INFINITY = 1000000

    def __init__(self):
        self.graph = defaultdict(set)
        self.vertices = set()

    def add_edge(self, head, tail, weight):
        self.graph[head].add((tail, weight))
        self.vertices.add(head)
        self.vertices.add(tail)

    def dijkstra(self, start):
        unvisited_nodes, dist, prev = self.__initialize(start)

        while unvisited_nodes:
            min_node = self.__minimum_distance(dist, unvisited_nodes)

            if dist[min_node] == Graph.INFINITY:
                break

            for vertex, weight in self.graph[min_node]:
                alt = dist[min_node] + weight
                if alt < dist[vertex]:
                    dist[vertex] = alt
                    prev[vertex] = min_node

            unvisited_nodes.remove(min_node)

        return dist

    def __initialize(self, start):
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
