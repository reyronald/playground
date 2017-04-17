import heapq

def get_integer_array_from_file(path):
    testfile = open(path, 'r')
    integers = []
    while testfile:
        line = testfile.readline().rstrip()
        if not line:
            break
        integers.append(int(line))
    return integers

def find_median(integers):
    lows = [-integers.pop(0)] # extract max
    result = -lows[0]

    highs = [integers.pop(0)]

    if -lows[0] > highs[0]:
        lows[0], highs[0] = -highs[0], -lows[0]

    result += -lows[0]

    for integer in integers:
        low = -lows[0]
        high = highs[0]

        if integer < low:
            heapq.heappush(lows, -integer)
        elif integer > high:
            heapq.heappush(highs, integer)
        else:
            heapq.heappush(lows, -integer)

        # Rebalancing
        if len(lows) - len(highs) > 1:
            temp = -heapq.heappop(lows)
            heapq.heappush(highs, temp)

        if len(highs) > len(lows):
            temp = heapq.heappop(highs)
            heapq.heappush(lows, -temp)

        result += -lows[0]

    return result % 10000
