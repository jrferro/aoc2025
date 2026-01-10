# https://adventofcode.com/2025/day/9

import shapely

def init_sizes(locs):
    sizes = []
    for loc in locs:
        for nbr in locs:
            if loc == nbr:
                continue
            size = (abs(loc[0]-nbr[0]) + 1) * (abs(loc[1]-nbr[1]) + 1)
            sizes.append([size, loc, nbr])
    sizes.sort(key = lambda d: d[0], reverse=True)
    return sizes

def max_rect(filename):
    loc_strs = open(filename, "r").read().splitlines()
    locs = [[int(c) for c in l.split(",")] for l in loc_strs]
    sizes = init_sizes(locs)
    return sizes[0][0]

def max_green_rect(filename):
    loc_strs = open(filename, "r").read().splitlines()
    locs = [[int(c) for c in l.split(",")] for l in loc_strs]
    green_floor = shapely.Polygon(locs)
    sizes = init_sizes(locs)
    for try_rect in sizes:
        rect = shapely.Polygon([(try_rect[1][0], try_rect[1][1]),
                                (try_rect[1][0], try_rect[2][1]),
                                (try_rect[2][0], try_rect[2][1]),
                                (try_rect[2][0], try_rect[1][1])])
        if shapely.within(rect, green_floor):
            return try_rect[0]

def main():
    print("max rect test: ", max_rect("day9_test.txt"))
    print("max rect input: ", max_rect("day9_input.txt"))
    print("max green rect test: ", max_green_rect("day9_test.txt"))
    print("max green rect input: ", max_green_rect("day9_input.txt"))

if __name__ == "__main__":
    main()
