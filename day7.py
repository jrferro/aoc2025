# https://adventofcode.com/2025/day/7

from collections import defaultdict

def split_count(filename):
    manifold_strs = open(filename, "r").read().splitlines()
    beam_cols = set([i for i,v in enumerate(manifold_strs[0]) if v == 'S'])
    splits = 0
    for str in manifold_strs[1:]:
        new_cols = set(beam_cols)
        for i,v in enumerate(str):
            if v == '^' and i in beam_cols:
                new_cols.add(i-1)
                new_cols.discard(i)
                new_cols.add(i+1)
                splits += 1
        beam_cols = new_cols
    return splits

def timeline_count(filename):
    manifold_strs = open(filename, "r").read().splitlines()
    timelines = defaultdict(int)
    for i,v in enumerate(manifold_strs[0]):
        if v == 'S':
            timelines[i] = 1
    for str in manifold_strs[1:]:
        for i,v in enumerate(str):
            if v == '^' and i in timelines:
                timelines[i-1] += timelines[i]
                timelines[i+1] += timelines[i]
                timelines[i] = 0
    return sum(timelines.values())

def main():
    print("split count test: ", split_count("day7_test.txt"))
    print("split count input: ", split_count("day7_input.txt"))
    print("timeline count test: ", timeline_count("day7_test.txt"))
    print("timeline count input: ", timeline_count("day7_input.txt"))

if __name__ == "__main__":
    main()
