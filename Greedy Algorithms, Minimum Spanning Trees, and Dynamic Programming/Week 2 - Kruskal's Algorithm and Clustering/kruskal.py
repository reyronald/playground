from collections import defaultdict

class DisjointSet:
    def __init__(self):
        self.parents = defaultdict(dict)

    def make_set(self, value):
        self.parents[value] = {'parent': value, 'rank':0}

    def find(self, value):
        if self.parents[value]['parent'] == value:
            return value
        return self.find(self.parents[value]['parent'])

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.parents[x_root]['rank'] < self.parents[y_root]['rank']:
            self.parents[x_root]['parent'] = y_root
        elif self.parents[x_root]['rank'] > self.parents[y_root]['rank']:
            self.parents[y_root]['parent'] = x_root
        else:
            self.parents[y_root]['parent'] = x_root
            self.parents[x_root]['rank'] = self.parents[x_root]['rank'] + 1

class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    def __repr__(self):
        return str(self.first) + '-' + str(self.second) + ' ' + str(self.weight)

class Graph:
    def __init__(self):
        self.edges = list()
        self.vertices = set()
        self.graph = defaultdict(set)
        self.disjointset = DisjointSet()

    def add_edge(self, first, second, weight):
        edge = Edge(first, second, weight)
        self.edges.append(edge)
        self.vertices.add(first)
        self.vertices.add(second)
        self.graph[first].add(edge)
        self.graph[second].add(edge)

    def mst(self):
        for v in self.vertices:
            self.disjointset.make_set(v)

        self.edges.sort(key=lambda e: e.weight)

        tree = set()
        for edge in self.edges:
            if self.__has_no_cycles(self.disjointset, edge):
                tree.add(edge)
                self.disjointset.union(edge.first, edge.second)

        return tree

    @staticmethod
    def __has_no_cycles(disjointset, edge):
        return disjointset.find(edge.first) != disjointset.find(edge.second)

def main():
    graph = Graph()
    graph.add_edge('a', 'e', 1)
    graph.add_edge('a', 'b', 3)
    graph.add_edge('b', 'c', 5)
    graph.add_edge('b', 'e', 4)
    graph.add_edge('c', 'e', 6)
    graph.add_edge('c', 'd', 2)
    graph.add_edge('e', 'd', 7)

    tree = graph.mst()

if __name__ == '__main__':
    main()
