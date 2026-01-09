DIAL_SIZE = 100
START_POS = 50

def turn_amt(insn):
    dir = insn[0:1]
    amt = int(insn[1:])
    if dir == "L":
        amt = -amt
    return amt

def end_positions(amts, cur, modulus):
    positions = [cur]
    for amt in amts:
        cur = (cur + amt) % modulus
        positions.append(cur)
    return positions

def end_pos_ct(filename):
    insns = open(filename, "r").read().splitlines()
    amts = map(turn_amt, insns)
    positions = end_positions(amts, START_POS, DIAL_SIZE)
    return positions.count(0)

def count_zeros(amts, cur, modulus):
    zeros = []
    for amt in amts:
        clicks = abs((cur + amt) // modulus)
        # If we *leave* zero by going left, don't count it.
        if cur == 0 and amt < 0:
            clicks -= 1
        cur = (cur + amt) % modulus
        # If we *arrive at* zero by going left, *do* count it.
        if cur == 0 and amt < 0:
            clicks += 1
        zeros.append(clicks)
    return zeros

def during_pos_ct(filename):
    insns = open(filename, "r").read().splitlines()
    amts = map(turn_amt, insns)
    zeros = count_zeros(amts, START_POS, DIAL_SIZE)
    return sum(zeros)

def main():
    print("end count test: ", end_pos_ct(f"day1_test.txt"))
    print("end count input: ", end_pos_ct(f"day1_input.txt"))
    print("during count test: ", during_pos_ct(f"day1_test.txt"))
    print("during count input: ", during_pos_ct(f"day1_input.txt"))

if __name__ == "__main__":
    main()
