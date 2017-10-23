def knapsack(knapsack_size, items):
    grid = [[0 for x in range(knapsack_size+1)] for y in range(len(items)+1)]

    for idx, (value, weight) in enumerate(items):
        i = idx + 1
        for j in range(knapsack_size+1):
            if weight > j:
                grid[i][j] = grid[i-1][j]
            else:
                grid[i][j] = max(grid[i-1][j], grid[i-1][j-weight] + value)
    return grid[-1][-1]

def knapsack_big(knapsack_size, items):
    memo = [0 for cap in range(knapsack_size+1)]

    for value, weight in items:
        subproblem = []
        for j in range(knapsack_size+1):
            if j - weight < 0:
                subproblem.append(memo[j])
            else:
                subproblem.append(max(memo[j], memo[j - weight] + value))
        memo = subproblem
    return memo[-1]

def test_case_0():
    knapsack_size = 6
    items = [[3, 4], [2, 3], [4, 2], [4, 3]]
    answer = knapsack_big(knapsack_size, items)
    assert answer == 8

def read(path):
    items = []
    with open(path) as fin:
        line = next(fin)
        knapsack_size, number_of_items = map(int, line.rstrip().split(' '))
        for line in fin:
            if not line:
                break
            items.append(map(int, line.rstrip().split(' ')))
    return knapsack_size, items

def assignment_1():
    knapsack_size, items = read("D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 4 - Knapsack\knapsack\knapsack1.txt")
    answer = knapsack_big(knapsack_size, items)
    print answer
    assert answer == 2493893

def assignment_2():
    knapsack_size, items = read("D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 4 - Knapsack\knapsack\knapsack_big.txt")
    answer = knapsack_big(knapsack_size, items)
    print answer
    assert answer == 4243395

def main():
    test_case_0()
    assignment_1()
    assignment_2()

if __name__ == '__main__':
    main()
