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
        Q, dist, prev = self.initialize(start)

        while Q:
            min_node = self.minimum_distance(dist, Q)

            if dist[min_node] == Graph.INFINITY:
                break

            Q.remove(min_node)

            for vertex, weight in self.graph[min_node]:
                alt = dist[min_node] + weight
                if alt < dist[vertex]:
                    dist[vertex] = alt
                    prev[vertex] = min_node

        return dist

    def initialize(self, start):
        Q = set([start])
        dist = dict()
        prev = dict()
        for vertex in self.vertices:
            dist[vertex] = Graph.INFINITY
            prev[vertex] = None
            Q.add(vertex)

        dist[start] = 0

        return Q, dist, prev

    def minimum_distance(self, dist, Q):
        min_node = None
        for vertex in Q:
            if min_node is None or dist[vertex] < dist[min_node]:
                min_node = vertex
        return min_node
