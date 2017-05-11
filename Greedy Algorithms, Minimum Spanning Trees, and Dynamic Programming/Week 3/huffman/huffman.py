from heapq import heappush, heappop, heapify

class Character:
    def __init__(self, label, weight, left = None, right = None):
        self.label = str(label)
        self.weight = weight
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.label) + ' ' + str(self.weight)

    def is_leaf(self):
        return self.left is None and self.right is None

class HuffmanTree:
    def __init__(self, input):
        ordered_input = [(c.weight, c) for c in input]
        heapify(ordered_input)
        self.ordered_input = ordered_input
        self.tree = None
        self.codeword_map = None
        self.max_codeword_length = None
        self.min_codeword_length = None

    def generate_huffman_tree(self):
        self.tree = HuffmanTree.huffman(self.ordered_input)
        self.codeword_map = self._walk_tree(self.tree)
        return self

    def _walk_tree(self, node, order = 0, result = {}):
        if node.is_leaf():
            result[node.label] = order
            if self.max_codeword_length is None or order > self.max_codeword_length:
                self.max_codeword_length = order
            if self.min_codeword_length is None or order < self.min_codeword_length:
                self.min_codeword_length = order

        if node.left is not None:
            self._walk_tree(node.left, order + 1)
        if node.right is not None:
            self._walk_tree(node.right, order + 1)

        return result

    @staticmethod
    def huffman_recursive(ordered_input):
        if not ordered_input or len(ordered_input) == 1:
            return heappop(ordered_input)[1]

        first = heappop(ordered_input)[1]
        second = heappop(ordered_input)[1]

        top = Character(first.label + ',' + second.label, first.weight + second.weight, first, second)

        heappush(ordered_input, (top.weight, top))

        return HuffmanTree.huffman(ordered_input)

    @staticmethod
    def huffman(ordered_input):
        while True:
            if len(ordered_input) == 1:
                return heappop(ordered_input)[1]

            first = heappop(ordered_input)[1]
            second = heappop(ordered_input)[1]

            top = Character(first.label + ',' + second.label, first.weight + second.weight, first, second)

            heappush(ordered_input, (top.weight, top))

def test_case_0():
    input = set([
        Character('A', 3),
        Character('B', 2),
        Character('C', 6),
        Character('D', 8),
        Character('E', 2),
        Character('F', 6),
    ])

    tree = HuffmanTree(input).generate_huffman_tree()
    assert tree.min_codeword_length == 2
    assert tree.max_codeword_length == 4

def test_case_1():
    input = [
        Character(1, 5),
        Character(1, 25),
        Character(1, 32),
        Character(1, 20),
        Character(1, 18),
    ]

    tree = HuffmanTree(input).generate_huffman_tree()
    assert tree.min_codeword_length == 2
    assert tree.max_codeword_length == 3

def test_case_2():
    input = [
        Character(1, 10),
        Character(2, 37),
        Character(3, 59),
        Character(4, 43),
        Character(5, 27),
        Character(6, 30),
        Character(7, 96),
        Character(8, 96),
        Character(9, 71),
        Character(10, 8),
        Character(11, 76),
    ]
    tree = HuffmanTree(input).generate_huffman_tree()
    assert tree.min_codeword_length == 2
    assert tree.max_codeword_length == 6

def test_case_3():
    input = [
        Character(1, 15),
        Character(2, 895),
        Character(3, 121),
        Character(4, 188),
        Character(5, 953),
        Character(6, 378),
        Character(7, 849),
        Character(8, 153),
        Character(9, 579),
        Character(10, 144),
        Character(11, 727),
        Character(12, 589),
        Character(13, 301),
        Character(14, 442),
        Character(15, 327),
        Character(16, 930),
    ]
    tree = HuffmanTree(input).generate_huffman_tree()
    assert tree.min_codeword_length == 3
    assert tree.max_codeword_length == 7

def assignment():
    node_number = 1
    input = []
    with open("D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 3\huffman\huffman.txt") as fin:
        next(fin)
        for line in fin:
            if not line:
                break
            input.append(Character(node_number, int(line.rstrip())))
            node_number += 1
    tree = HuffmanTree(input).generate_huffman_tree()
    assert tree.min_codeword_length == 9
    assert tree.max_codeword_length == 19

def main():
    test_case_0()
    test_case_1()
    test_case_2()
    test_case_3()
    assignment()

if __name__ == '__main__':
    main()
