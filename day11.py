# https://adventofcode.com/2025/day/11

import attrs

@attrs.define
class rack():
    g = attrs.field(factory=dict)
    memo = attrs.field(factory=dict)

    def add_node(self, fro, tos):
        self.g[fro] = tos

    def count_paths(self, fro, to):
        if fro == to:
            return 1
        if fro not in self.g:
            return 0
        if (fro, to) in self.memo:
            return self.memo[(fro, to)]
        ct = sum([self.count_paths(n, to) for n in self.g[fro]])
        self.memo[(fro, to)] = ct
        return ct

def num_paths(filename):
    node_strs = open(filename, "r").read().splitlines()
    r = rack()
    for n in node_strs:
        ns = n.split()
        r.add_node(ns[0][:-1], ns[1:])
    return r.count_paths("you", "out")

def num_filtered_paths(filename):
    node_strs = open(filename, "r").read().splitlines()
    r = rack()
    for n in node_strs:
        ns = n.split()
        r.add_node(ns[0][:-1], ns[1:])
    fft_dac = r.count_paths("fft", "dac")
    dac_fft = r.count_paths("dac", "fft")
    if fft_dac:
        svr_fft = r.count_paths("svr", "fft")
        dac_out = r.count_paths("dac", "out")
        return svr_fft * fft_dac * dac_out
    elif dac_fft:
        svr_dac = r.count_paths("svr", "dac")
        fft_out = r.count_paths("fft", "out")
        return svr_dac * dac_fft * fft_out
    else:
        return 999999

def main():
    print("num paths test: ", num_paths("day11_test.txt"))
    print("num paths input: ", num_paths("day11_input.txt"))
    print("num filtered paths test: ", num_filtered_paths("day11_test2.txt"))
    print("num filtered paths input: ", num_filtered_paths("day11_input.txt"))

if __name__ == "__main__":
    main()
