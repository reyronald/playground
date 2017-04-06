class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.t = 0
        self.s = None
        self.explored = set()
        self.leaders = {}
        self.f = {}

    def log(self):
        print self.graph

    def scc(self):
        # reversed_graph = self.get_reverse_graph()
        self.dfs_loop()
        self.traspose_graph()
        self.explored = set()
        self.dfs_loop()
        return

    def get_reverse_graph(self):
        reversed_graph = {}
        for vertex in self.graph:
            if vertex not in reversed_graph:
                reversed_graph[vertex] = set()
            for neighbor in self.graph[vertex]:
                if neighbor not in reversed_graph:
                    reversed_graph[neighbor] = set()
                reversed_graph[neighbor].add(vertex)
        return Graph(reversed_graph)

    def dfs_loop(self):
        for vertex in self.graph:
            if vertex not in self.explored:
                self.s = vertex
                self.dfs(vertex)

    def dfs(self, vertex):
        self.explored.add(vertex)
        self.leaders[vertex] = self.s
        for vertex2 in self.graph[vertex]:
            if vertex2 not in self.explored:
                self.dfs(vertex2)
        self.t += 1
        self.f[vertex] = self.t

    def traspose_graph(self):
        graph = {}
        for vertex in self.graph:
            if self.f[vertex] not in graph:
                graph[self.f[vertex]] = set()
            for neighbor in self.graph[vertex]:
                graph[self.f[vertex]].add(self.f[neighbor])
        self.graph = graph



# def dfs(graph, start):
#     visited, stack = set(), [start]
#     while stack:
#         vertex = stack.pop()
#         if vertex not in visited:
#             visited.add(vertex)
#             stack.extend(graph[vertex] - visited)
#     return visited
