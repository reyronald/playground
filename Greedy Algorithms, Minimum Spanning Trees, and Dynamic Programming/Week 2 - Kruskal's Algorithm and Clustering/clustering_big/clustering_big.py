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

def read_input(path):
    vertices_int = set()
    with open(path) as fin:
        _, number_of_bits = map(int, next(fin).rstrip().split(" "))
        for line in fin:
            if not line:
                break
            line = line.rstrip().replace(" ", "")
            vertices_int.add(int(line, 2))
    return number_of_bits, vertices_int

def generate_bitwise_set(number_of_bits):
    def shift_n_bits(n, base = set([0])):
        nums = set()
        for i in base:
            for j in range(0, n):
                nums.add((1 << j) | i)
        return nums | base
    return shift_n_bits(number_of_bits, shift_n_bits(number_of_bits))

def get_answer(path):
    number_of_bits, vertices_int = read_input(path)
    bitwise_set = generate_bitwise_set(number_of_bits)

    disjointset = DisjointSet()
    for vertex in vertices_int:
        disjointset.make_set(vertex)
        for bitwise in bitwise_set:
            bitwise_result = vertex ^ bitwise
            if bitwise_result in vertices_int:
                if not disjointset.in_set(bitwise_result):
                    disjointset.make_set(bitwise_result)
                disjointset.union(vertex, bitwise_result)
    return disjointset.get_cluster_size()

def test_case_1():
    path = "D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 2\clustering\\tc1_answer_3.txt"
    answer = get_answer(path)
    assert answer == 3

def test_case_2():
    path = "D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 2\clustering\\tc2_answer_2.txt"
    answer = get_answer(path)
    assert answer == 2

def test_case_3():
    path = "D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 2\clustering\\tc3_answer_6.txt"
    answer = get_answer(path)
    assert answer == 6

def assignment():
    path = "D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 2\clustering\clustering_big.txt"
    answer = get_answer(path)
    assert answer == 6118 # 6118 or 13172 (8.93056747874 seconds execution time)
    print answer
    return answer 

def main():
    test_case_1()
    test_case_2()
    test_case_3()
    assignment()

if __name__ == '__main__':
    main()
