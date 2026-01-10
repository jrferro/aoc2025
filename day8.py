# https://adventofcode.com/2025/day/8

# I'm desperately abusing the fact that this is a one-off puzzle, and
# not making a class for the locations.  Instead, a loc is a list of
# [ID, X, Y, Z, CIRC], and we depend on lists being mutable to update
# CIRC whenever circuits are merged.  The circuits dict is also
# updated to keep track of all locs that are in each circuit.

def init_dists(locs):
    dists = []
    for loc in locs:
        for nbr in locs:
            if loc == nbr or loc[0] > nbr[0]:
                continue
            dist = ((loc[1]-nbr[1])**2 +
                    (loc[2]-nbr[2])**2 +
                    (loc[3]-nbr[3])**2)
            dists.append([dist, loc, nbr])
    dists.sort(key = lambda d: d[0])
    return dists

def merge_circuit(a, b, circuits):
    to = a[4]
    fro = b[4]
    if to == fro:
        return
    for l in circuits[fro]:
        l[4] = to
    circuits[to].extend(circuits[fro])
    del circuits[fro]

def circuit_sizes(filename, njoins):
    loc_strs = open(filename, "r").read().splitlines()
    locs = []
    circuits = {}
    for i,v in enumerate(loc_strs):
        loc = [i] + [int(c) for c in v.split(",")] + [i]
        locs.append(loc)
        circuits[i] = [loc]
    dists = init_dists(locs)
    for j in dists[:njoins]:
        merge_circuit(j[1], j[2], circuits)
    sizes = [len(c) for c in circuits.values()]
    sizes.sort(reverse=True)
    return sizes[0]*sizes[1]*sizes[2]

def circuit_walldist(filename):
    loc_strs = open(filename, "r").read().splitlines()
    locs = []
    circuits = {}
    for i,v in enumerate(loc_strs):
        loc = [i] + [int(c) for c in v.split(",")] + [i]
        locs.append(loc)
        circuits[i] = [loc]
    dists = init_dists(locs)
    for j in dists:
        merge_circuit(j[1], j[2], circuits)
        if len(circuits) == 1:
            return j[1][1]*j[2][1]

def main():
    print("circuit size test: ", circuit_sizes("day8_test.txt", 10))
    print("circuit size input: ", circuit_sizes("day8_input.txt", 1000))
    print("circuit walldist test: ", circuit_walldist("day8_test.txt"))
    print("circuit walldist input: ", circuit_walldist("day8_input.txt"))

if __name__ == "__main__":
    main()
