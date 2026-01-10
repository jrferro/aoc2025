# https://adventofcode.com/2025/day/5

from functools import reduce
import operator

def transpose(ary):
    return [[ary[j][i] for j in range(len(ary))] for i in range(len(ary[0]))]

def eval_math(nums, ops):
    answers = []
    for problem, op in enumerate(ops):
        if op == '+':
            ans = reduce(operator.add, nums[problem], 0)
        else:
            ans = reduce(operator.mul, nums[problem], 1)
        answers.append(ans)
    return answers

def add_math_simple(filename):
    math_strs = open(filename, "r").read().splitlines()
    math_ops = math_strs[-1].split()
    math_nums = [[int(i) for i in s.split()] for s in math_strs[:-1]]
    math_nums = transpose(math_nums)
    return sum(eval_math(math_nums, math_ops))

def extract_nums_gross(math_strs):
    ops = math_strs[-1]
    strs = math_strs[:-1]
    nums = []
    op_positions = [i for i,v in enumerate(ops) if v != ' '] + [len(ops) + 1]
    for p in range(len(op_positions) - 1):
        digits = [s[op_positions[p] : op_positions[p+1] - 1] for s in strs]
        digits = transpose(digits)
        ns = [int(''.join(ds)) for ds in digits]
        nums.append(ns)
    return nums

def add_math_gross(filename):
    math_strs = open(filename, "r").read().splitlines()
    math_ops = math_strs[-1].split()
    math_nums = extract_nums_gross(math_strs)
    return sum(eval_math(math_nums, math_ops))

def main():
    print("simple math test: ", add_math_simple("day6_test.txt"))
    print("simple math input: ", add_math_simple("day6_input.txt"))
    print("gross math test: ", add_math_gross("day6_test.txt"))
    print("gross math input: ", add_math_gross("day6_input.txt"))

if __name__ == "__main__":
    main()
