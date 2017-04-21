from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        self.s = None
        self.f = []
        self.t = 0
        self.finishing_order = []
        self.scc_count = defaultdict(lambda: 0)

    def add_edge(self, tail, head):
        self.graph[head].add(tail)

        if self.graph[tail] is None:
            self.graph[tail] = set()

    def find_scc(self):
        # First DFS Pass
        self.f = [0]*(len(self.graph) + 1)
        def on_finish(start):
            """ Only relevant for first DFS Pass """
            self.t += 1
            self.f[start] = self.t
            self.finishing_order.append(start)
        self.dfs_loop(lambda: [(yield vertex) for vertex in self.graph], on_finish=on_finish)

        # Second DFS Pass
        self.traspose_graph()
        finishing_order = self.finishing_order[::-1]
        f = self.f[:]
        self.scc_count = defaultdict(lambda: 0)
        def on_start():
            """ Only relevant for second DFS Pass """
            if self.s:
                self.scc_count[self.s] = self.scc_count[self.s] + 1
        self.dfs_loop(lambda: [(yield f[vertex]) for vertex in finishing_order], on_start=on_start)

        # Calculating Result
        sccs = self.scc_count.values()
        sccs.sort(reverse=True)
        del sccs[5:]
        sccs = sccs + [0]*(5-len(sccs))
        return ','.join(map(str, sccs))

    def dfs_loop(self, get_vector, on_start=lambda: None, on_finish=lambda *x: None):
        explored = set()
        for vertex in get_vector():
            if vertex not in explored:
                # Only relevant for second DFS Pass
                self.s = vertex
                self.dfs_recursive(vertex, explored, on_start, on_finish)

    def dfs_recursive(self, start, explored, on_start, on_finish):
        explored.add(start)

        # Only relevant for second DFS Pass
        on_start()

        for neighbor in self.graph[start]:
            if neighbor not in explored:
                self.dfs_recursive(neighbor, explored, on_start, on_finish)

        # Only relevant for first DFS Pass
        on_finish(start)

    def traspose_graph(self):
        temp_graph = defaultdict(set)
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                temp_graph[self.f[neighbor]].add(self.f[vertex])
        self.graph = temp_graph

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
