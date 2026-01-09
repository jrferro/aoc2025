# https://adventofcode.com/2025/day/3

def max_joltage(bank, batt_ct):
    if batt_ct < 1:
        return 0
    max = 0
    for t in range(len(bank) - batt_ct + 1):
        if int(bank[t]) > max:
            max = int(bank[t])
            pos = t
    extra_joltage = max_joltage(bank[pos+1:], batt_ct-1)
    return max * (10 ** (batt_ct - 1)) + extra_joltage

def total_joltage(filename, batt_ct):
    banks = open(filename, "r").read().splitlines()
    jolts = [max_joltage(bank, batt_ct) for bank in banks]
    return sum(jolts)

def main():
    print("2 battery joltage test: ", total_joltage("day3_test.txt", 2))
    print("2 battery joltage input: ", total_joltage("day3_input.txt", 2))
    print("12 battery joltage test: ", total_joltage("day3_test.txt", 12))
    print("12 battery joltage input: ", total_joltage("day3_input.txt", 12))

if __name__ == "__main__":
    main()
