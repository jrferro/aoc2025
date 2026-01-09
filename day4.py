# https://adventofcode.com/2025/day/4

DIRS = [
    [-1, -1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [0, 1],
    [-1, 1],
    [-1, 0]
]

def is_roll(grid, y, x):
    if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
        return False
    return grid[y][x] == '@'

def num_nbr_rolls(grid, y, x):
    nbr_rolls = [is_roll(grid, y+dir[0], x+dir[1]) for dir in DIRS]
    return nbr_rolls.count(True)

def free_roll_positions(grid):
    result = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if is_roll(grid, y, x) and num_nbr_rolls(grid, y, x) < 4:
                result.append([y, x])
    return result

def free_rolls_ct(filename):
    grid = open(filename, "r").read().splitlines()
    free_rolls = free_roll_positions(grid)
    return len(free_rolls)

def free_rolls_removal(filename):
    grid = open(filename, "r").read().splitlines()
    # Make grid assignable
    for y in range(len(grid)):
        grid[y] = list(grid[y])
    removals = 0
    free_rolls = free_roll_positions(grid)
    while len(free_rolls) > 0:
        removals += len(free_rolls)
        for roll in free_rolls:
            grid[roll[0]][roll[1]] = 'x'
        free_rolls = free_roll_positions(grid)
    return removals

def main():
    print("free rolls count test: ", free_rolls_ct("day4_test.txt"))
    print("free rolls count input: ", free_rolls_ct("day4_input.txt"))
    print("free rolls removal test: ", free_rolls_removal("day4_test.txt"))
    print("free rolls removal input: ", free_rolls_removal("day4_input.txt"))

if __name__ == "__main__":
    main()
