def get_integer_set_from_file(path):
    testfile = open(path, 'r')
    integers = set()
    while testfile:
        line = testfile.readline().rstrip()
        if not line:
            break
        integers.add(int(line))
    return integers

def find_2sum(integers, lower_bound, upper_bound):
    count = 0
    for t in range(lower_bound, upper_bound + 1):
        for x in integers:
            y = t - x
            if y != x and y in integers:
                count += 1
                break

    return count
