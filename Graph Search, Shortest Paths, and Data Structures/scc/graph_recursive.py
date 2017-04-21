from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.reversed_graph = defaultdict(set)
        self.s = None
        self.f = []
        self.t = 0
        self.finishing_order = []
        self.scc_count = defaultdict(lambda: 0)

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
                self.dfs_reverse_recur(vertex, explored)

    def dfs_loop_second(self):
        self.traspose_graph()
        explored = set()
        finishing_order = self.finishing_order[:]
        f = self.f[:]
        while finishing_order:
            vertex = f[finishing_order.pop()]
            if vertex not in explored:
                self.s = vertex
                self.dfs_reverse_recur(vertex, explored)

    def dfs_reverse_recur(self, start, explored):
        explored.add(start)

        if self.s:
            self.scc_count[self.s] = self.scc_count[self.s] + 1

        for neighbor in self.reversed_graph[start]:
            if neighbor not in explored:
                self.dfs_reverse_recur(neighbor, explored)

        self.t += 1
        self.f[start] = self.t
        self.finishing_order.append(start)

    def traspose_graph(self):
        for vertex in self.reversed_graph:
            for neighbor in self.reversed_graph[vertex]:
                self.graph[self.f[neighbor]].add(self.f[vertex])
        self.reversed_graph = self.graph

######################################

def create_from_dict(graph):
    instance = Graph()
    for vertex in graph:
        for neighbor in graph[vertex]:
            instance.add_edge(vertex, neighbor)
    return instance

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
