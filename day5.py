# https://adventofcode.com/2025/day/5

def parse_range(line):
    a, b = line.split('-')
    return [int(a), int(b)]

def fresh_ct(filename):
    db_strs = open(filename, "r").read().split("\n\n")
    ranges = [parse_range(s) for s in db_strs[0].splitlines()]
    queries = [int(s) for s in db_strs[1].splitlines()]
    ct = 0
    for q in queries:
        for r in ranges:
            if q >= r[0] and q <= r[1]:
                ct += 1
                break
    return ct

def fresh_range(filename):
    db_strs = open(filename, "r").read().split("\n\n")
    ranges = [parse_range(s) for s in db_strs[0].splitlines()]
    ranges.sort(key = lambda r: r[0])
    condensed = [ranges[0]]
    for r in ranges[1:]:
        if r[0] <= condensed[-1][1]:
            if r[1] > condensed[-1][1]:
                condensed[-1][1] = r[1]
        else:
            condensed.append(r)
    size = 0
    for r in condensed:
        size += (r[1] - r[0] + 1)
    return size

def main():
    print("fresh count test: ", fresh_ct("day5_test.txt"))
    print("fresh count input: ", fresh_ct("day5_input.txt"))
    print("fresh range test: ", fresh_range("day5_test.txt"))
    print("fresh range input: ", fresh_range("day5_input.txt"))

if __name__ == "__main__":
    main()
