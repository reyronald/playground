from heapq import heappush, heappop, heapify

class HuffmanTreeNode:
    def __init__(self, label, weight, left = None, right = None):
        self.label = str(label)
        self.weight = weight
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.label) + ' ' + str(self.weight)

    def is_leaf(self):
        return self.left is None and self.right is None

class HuffmanCode:
    def __init__(self, alphabet):
        alphabet_heap = [(c.weight, c) for c in alphabet]
        heapify(alphabet_heap)
        self.alphabet_heap = alphabet_heap
        self.tree = None
        self.codeword_map = None
        self.max_codeword_length = None
        self.min_codeword_length = None

    def generate_huffman_coding(self):
        self.tree = HuffmanCode._huffman(self.alphabet_heap)
        self.codeword_map = self._generate_codeword_map(self.tree)
        return self

    @staticmethod
    def _huffman(alphabet_heap):
        while len(alphabet_heap) > 1:
            left = heappop(alphabet_heap)[1]
            right = heappop(alphabet_heap)[1]

            top_label = left.label + ',' + right.label
            top_weight = left.weight + right.weight
            top = HuffmanTreeNode(top_label, top_weight, left, right)

            heappush(alphabet_heap, (top.weight, top))
        return heappop(alphabet_heap)[1]

    def _generate_codeword_map(self, node, order=0, codeword_map=None):
        if node.is_leaf():
            if codeword_map is None:
                codeword_map = {}
            codeword_map[node.label] = order
            if self.max_codeword_length is None or order > self.max_codeword_length:
                self.max_codeword_length = order
            if self.min_codeword_length is None or order < self.min_codeword_length:
                self.min_codeword_length = order

        if node.left is not None:
            self._generate_codeword_map(node.left, order + 1)
        if node.right is not None:
            self._generate_codeword_map(node.right, order + 1)

        return codeword_map

def test_case_0():
    alphabet = [
        HuffmanTreeNode('A', 3),
        HuffmanTreeNode('B', 2),
        HuffmanTreeNode('C', 6),
        HuffmanTreeNode('D', 8),
        HuffmanTreeNode('E', 2),
        HuffmanTreeNode('F', 6),
    ]
    huffman_code = HuffmanCode(alphabet).generate_huffman_coding()
    assert huffman_code.min_codeword_length == 2
    assert huffman_code.max_codeword_length == 4

def test_case_1():
    alphabet = [
        HuffmanTreeNode(1, 5),
        HuffmanTreeNode(1, 25),
        HuffmanTreeNode(1, 32),
        HuffmanTreeNode(1, 20),
        HuffmanTreeNode(1, 18),
    ]

    huffman_code = HuffmanCode(alphabet).generate_huffman_coding()
    assert huffman_code.min_codeword_length == 2
    assert huffman_code.max_codeword_length == 3

def test_case_2():
    alphabet = [
        HuffmanTreeNode(2, 37),
        HuffmanTreeNode(3, 59),
        HuffmanTreeNode(4, 43),
        HuffmanTreeNode(5, 27),
        HuffmanTreeNode(6, 30),
        HuffmanTreeNode(7, 96),
        HuffmanTreeNode(8, 96),
        HuffmanTreeNode(9, 71),
        HuffmanTreeNode(10, 8),
        HuffmanTreeNode(11, 76),
    ]
    huffman_code = HuffmanCode(alphabet).generate_huffman_coding()
    assert huffman_code.min_codeword_length == 2
    assert huffman_code.max_codeword_length == 5

def test_case_3():
    alphabet = [
        HuffmanTreeNode(2, 895),
        HuffmanTreeNode(3, 121),
        HuffmanTreeNode(4, 188),
        HuffmanTreeNode(5, 953),
        HuffmanTreeNode(6, 378),
        HuffmanTreeNode(7, 849),
        HuffmanTreeNode(8, 153),
        HuffmanTreeNode(9, 579),
        HuffmanTreeNode(10, 144),
        HuffmanTreeNode(11, 727),
        HuffmanTreeNode(12, 589),
        HuffmanTreeNode(13, 301),
        HuffmanTreeNode(14, 442),
        HuffmanTreeNode(15, 327),
        HuffmanTreeNode(16, 930),
    ]
    huffman_code = HuffmanCode(alphabet).generate_huffman_coding()
    assert huffman_code.min_codeword_length == 3
    assert huffman_code.max_codeword_length == 6

def assignment():
    node_number = 1
    alphabet = []
    with open("D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 3 - Huffman and Max Weighted Independent Set\huffman\huffman.txt") as fin:
        next(fin)
        for line in fin:
            if not line:
                break
            alphabet.append(HuffmanTreeNode(node_number, int(line.rstrip())))
            node_number += 1
    huffman_code = HuffmanCode(alphabet).generate_huffman_coding()
    assert huffman_code.max_codeword_length == 19
    assert huffman_code.min_codeword_length == 9

def main():
    test_case_0()
    test_case_1()
    test_case_2()
    test_case_3()
    assignment()

if __name__ == '__main__':
    main()
