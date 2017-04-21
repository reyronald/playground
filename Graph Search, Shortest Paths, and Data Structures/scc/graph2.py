from collections import defaultdict

class Graph:
    @staticmethod
    def create_from_dict(graph):
        instance = Graph()
        for vertex in graph:
            for neighbor in graph[vertex]:
                instance.add_edge(vertex, neighbor)
        return instance

    @staticmethod
    def create_from_file(path):
        instance = Graph()
        testfile = open(path, 'r')
        while testfile:
            line = testfile.readline().rstrip()
            if not line:
                break
            vertex, neighbor = line.split(" ")
            instance.add_edge(int(vertex), int(neighbor))
        return instance

    def __init__(self):
        self.number_of_vertices = 0
        self.graph = defaultdict(set)
        self.reversed_graph = defaultdict(set)
        self.s = None
        self.f = []
        self.t = 0
        self.leaders = {}
        self.finishing_order = []
        self.scc_count = {}

    def add_edge(self, tail, head):
        self.reversed_graph[head].add(tail)

        if self.reversed_graph[tail] is None:
            self.reversed_graph[tail] = set()

    def find_scc(self):
        self.f = [0]*(len(self.reversed_graph) + 1)
        self.dfs_loop_reverse()
        self.dfs_loop_second()
        sccs = self.scc_count.values()
        sccs.sort(reverse=True)
        del sccs[5:]
        sccs = sccs + [0]*(5-len(sccs))
        return ','.join(map(str, sccs))

    def dfs_loop_reverse(self):
        explored = set()
        for vertex in self.reversed_graph:
            if vertex not in explored:
                self.dfs_reverse(vertex, explored)

    def dfs_reverse(self, start, explored):
        stack = [start]
        explored.add(start)
        explored_order = []

        while stack:
            vertex = stack.pop()
            explored_order.append(vertex)
            for neighbor in self.reversed_graph[vertex]:
                if neighbor not in explored:
                    stack.append(neighbor)
                    explored.add(neighbor)

        while explored_order:
            vertex = explored_order.pop()
            if not self.reversed_graph[vertex] - explored:
                self.t += 1
                self.f[vertex] = self.t
                self.finishing_order.append(vertex)

    def dfs_loop_second(self):
        self.traspose_graph()
        explored = set()
        while self.finishing_order:
            vertex = self.f[self.finishing_order.pop()]
            if vertex not in explored:
                self.s = vertex
                self.dfs(vertex, explored)

    def dfs(self, start, explored):
        stack = [start]
        explored.add(start)
        self.leaders[start] = self.s
        while stack:
            self.scc_count[self.s] = self.scc_count[self.s] + 1 if self.s in self.scc_count else 1
            vertex = stack.pop()
            for neighbor in self.graph[vertex]:
                if neighbor not in explored:
                    explored.add(neighbor)
                    stack.append(neighbor)

    def traspose_graph(self):
        for vertex in self.reversed_graph:
            for neighbor in self.reversed_graph[vertex]:
                self.graph[self.f[neighbor]].add(self.f[vertex])
