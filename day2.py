# https://adventofcode.com/2025/day/2

import itertools

def is_pair(id):
    idstr = str(id)
    idlen = len(idstr)
    if idlen % 2 != 0:
        return False
    if idstr[:idlen // 2] * 2 == idstr:
        return True
    return False

def find_pairs(id_range):
    id_start,id_end = [int(id) for id in id_range.split('-')]
    id_pairs = [id for id in range(id_start, id_end+1) if is_pair(id)]
    return id_pairs

def is_tuple(id):
    idstr = str(id)
    idlen = len(idstr)
    for replen in range(1, idlen // 2 + 1):
        if idlen % replen != 0:
            continue
        if idstr[:replen] * (idlen // replen) == idstr:
            return True
    return False

def find_tuples(id_range):
    id_start,id_end = [int(id) for id in id_range.split('-')]
    id_tuples = [id for id in range(id_start, id_end+1) if is_tuple(id)]
    return id_tuples

def pattern_sum(filename, patterner):
    id_ranges = open(filename, "r").read().strip().split(',')
    match_lists = [patterner(id_range) for id_range in id_ranges]
    matches = list(itertools.chain(*match_lists))
    return sum(matches)

def main():
    print("pattern pairs test: ", pattern_sum("day2_test.txt", find_pairs))
    print("pattern pairs input: ", pattern_sum("day2_input.txt", find_pairs))
    print("pattern tuples test: ", pattern_sum("day2_test.txt", find_tuples))
    print("pattern tuples input: ", pattern_sum("day2_input.txt", find_tuples))

if __name__ == "__main__":
    main()
