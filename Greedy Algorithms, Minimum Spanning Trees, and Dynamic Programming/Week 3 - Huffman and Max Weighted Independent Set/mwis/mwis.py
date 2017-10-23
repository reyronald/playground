# Good documentation on this problem:
# https://wincent.com/wiki/Computing_the_Maximum_Weighted_Independent_Set_of_a_graph_path
 
def mwis(vertices):
    # Memoization Step
    max_weights = [0, vertices[1]]
    for i in range(2, len(vertices)):
        max_weights.append(max(max_weights[i-1], max_weights[i-2] + vertices[i]))

    # Reconstruction step
    reconstructed_path = []
    i = len(max_weights) - 1
    while i >= 1:
        # if max_weights[i-1] >= max_weights[i-2] + vertices[i]:
        #     i -= 1
        # else:
        #     reconstructed_path.append(i)
        #     i -= 2

        if max_weights[i] == max_weights[i-1]:
            i -= 1
        else:
            reconstructed_path.append(i)
            i -= 2

    return max_weights[-1], reconstructed_path

def get_answer(reconstructed_path):
    vertices_to_check = [1, 2, 3, 4, 17, 117, 517, 997]
    answer = ''
    for vertex in vertices_to_check:
        answer += '1' if vertex in reconstructed_path else '0'
    return answer

def test_case_0():
    vertices = [1, 4, 5, 4]
    max_weight, reconstructed_path = mwis(vertices)
    assert max_weight == 8
    assert reconstructed_path == [2,4]

def test_case_1():
    vertices = [10, 280, 618, 762, 908, 409, 34, 59, 277, 246, 779]
    max_weight, reconstructed_path = mwis(vertices)
    assert max_weight == 2616
    assert reconstructed_path == [3, 5, 7, 9, 11]

def test_case_2():
    vertices = [10, 460, 250, 730, 63, 379, 638, 122, 435, 705, 84]
    max_weight, reconstructed_path = mwis(vertices)
    assert max_weight == 2533
    assert reconstructed_path == [2, 4, 7, 10]

def read_input():
    vertices = [None]
    with open("e:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 3 - Huffman and Max Weighted Independent Set\mwis\mwis.txt") as fin:
        next(fin)
        for line in fin:
            if not line:
                break
            vertices.append(int(line.rstrip()))
    return vertices

def assignment():
    vertices = read_input()
    max_weight, reconstructed_path = mwis(vertices)
    answer = get_answer(reconstructed_path)
    assert max_weight == 2955353732
    assert answer == '10100110'

def main():
    test_case_0()
    # test_case_1()
    # test_case_2()
    assignment()

if __name__ == '__main__':
    main()
