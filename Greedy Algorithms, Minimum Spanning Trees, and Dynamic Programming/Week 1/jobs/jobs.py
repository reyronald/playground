class Job:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length

    def __repr__(self):
        return repr((self.weight, self.length))

def get_jobs_input():
    path = 'D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 1\jobs\jobs.txt'
    # path = 'D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 1\jobs\jobs_tc1_answer_68615_67247.txt'
    # path = 'D:\\repos\playground\Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming\Week 1\jobs\jobs_tc2_answer_32780_32104.txt'
    jobs = []
    with open(path) as fin:
        next(fin)
        for line in fin:
            if not line:
                break
            weight, length = map(int, line.rstrip().split(' '))
            jobs.append(Job(weight, length))
    return jobs

def get_completion_time_sum(jobs):
    completion_time_sum = 0
    completion_time = 0
    for job in jobs:
        completion_time += job.length
        completion_time_sum += job.weight * completion_time
    return completion_time_sum

def main():
    jobs = get_jobs_input()
    jobs.sort(key=lambda j: -j.weight)

    diff_completion_time = get_completion_time_sum(sorted(jobs, key=lambda j: j.weight - j.length, reverse = True))
    ratio_completion_time = get_completion_time_sum(sorted(jobs, key=lambda j: j.weight*1.0/j.length, reverse = True))

    print 'Diff ' + str(diff_completion_time) # Answer 69119377652
    print 'Ratio ' + str(ratio_completion_time) # Answer 67311454237

if __name__ == '__main__':
    main()
