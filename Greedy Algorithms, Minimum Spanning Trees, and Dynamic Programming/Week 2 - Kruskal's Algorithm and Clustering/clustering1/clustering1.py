from collections import defaultdict

class DisjointSet:
    def __init__(self):
        self.cluster_amount = 0
        self.parents = defaultdict(dict)

    def in_set(self, value):
        return value in self.parents

    def make_set(self, value):
        self.cluster_amount += 1
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

        self.cluster_amount -= 1

        if self.parents[x_root]['rank'] < self.parents[y_root]['rank']:
            self.parents[x_root]['parent'] = y_root
        else:
            self.parents[y_root]['parent'] = x_root
            if self.parents[x_root]['rank'] == self.parents[y_root]['rank']:
                self.parents[x_root]['rank'] = self.parents[x_root]['rank'] + 1

    def get_cluster_size(self):
        return self.cluster_amount

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

    def max_space_clustering(self, k):
        for vertex in self.vertices:
            self.disjointset.make_set(vertex)

        self.edges.sort(key=lambda e: e.weight)

        for edge in self.edges:
            if self.__has_no_cycles(self.disjointset, edge):
                self.disjointset.union(edge.first, edge.second)

            if self.disjointset.get_cluster_size() < k:
                return edge.weight

    @staticmethod
    def __has_no_cycles(disjointset, edge):
        return disjointset.find(edge.first) != disjointset.find(edge.second)

def read_input(path):
    graph = Graph()
    with open(path) as fin:
        next(fin)
        for line in fin:
            if not line:
                break
            head, tail, weight = map(int, line.rstrip().split(' '))
            graph.add_edge(head, tail, weight)
    return graph

def test_case_1(k):
    path = "D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 2\clustering1\\tc1_answer_100.txt"
    # NOTE: This test case should be with K = 2
    result = read_input(path).max_space_clustering(2)
    assert result == 100

def test_case_2(k):
    path = "D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 2\clustering1\\tc2_answer_3.txt"
    result = read_input(path).max_space_clustering(k)
    assert result == 3

def test_case_3(k):
    path = "D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 2\clustering1\\tc3_answer_99.txt"
    result = read_input(path).max_space_clustering(k)
    assert result == 99

def assignment(k):
    path = "D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 2\clustering1\clustering1.txt"
    result = read_input(path).max_space_clustering(k)
    print result
    assert result == 106 # Answer 106

def main():
    k = 4
    test_case_1(k)
    test_case_2(k)
    test_case_3(k)
    assignment(k)

if __name__ == '__main__':
    main()
