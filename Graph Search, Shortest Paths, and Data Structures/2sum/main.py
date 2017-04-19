from two_sum import get_integer_set_from_file, find_2sum

INTEGER_SET = {-3, -1, 1, 2, 9, 11, 7, 6, 2}
RESULT = find_2sum(INTEGER_SET, 3, 10)
assert RESULT == 8

INTEGER_SET = {-2, 0, 0, 4}
RESULT = find_2sum(INTEGER_SET, 0, 4)
assert RESULT == 2

INTEGER_SET = {0, 1, 2, 3, 4, 5, 6}
RESULT = find_2sum(INTEGER_SET, 3, 4)
assert RESULT == 2

INTEGER_SET = {0, 1, 2, 3, 4, 5, 6}
RESULT = find_2sum(INTEGER_SET, 30, 40)
assert RESULT == 0

ROOT = "D:/repos/playground/Graph Search, Shortest Paths, and Data Structures/2sum/"
INTEGER_SET = get_integer_set_from_file(ROOT + "algo1-programming_prob-2sum.txt")
RESULT = find_2sum(INTEGER_SET, -10000, 10000)
assert RESULT == 427 # 6582.4 seconds

print RESULT
