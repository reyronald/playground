from median import get_integer_array_from_file, find_median

ROOT = "D:/repos/playground/Graph Search, Shortest Paths, and Data Structures/median/"

RESULT = find_median(get_integer_array_from_file(ROOT + "tc1.txt"))
assert RESULT == 142

RESULT = find_median(get_integer_array_from_file(ROOT + "tc2.txt"))
assert RESULT == 9335

RESULT = find_median(get_integer_array_from_file(ROOT + "Median.txt"))
assert RESULT == 1213

print RESULT
