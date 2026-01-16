# https://adventofcode.com/2025/day/10

import attrs

@attrs.define
class mach:
    goal: tuple[int] = ()
    buttons: list[list[int]] = []
    joltage: list[int] = []
    state: tuple[int] = ()

    @classmethod
    def from_mach_str(cls, s):
        strs = s.split()
        goal_str = strs[0]
        button_strs = strs[1:-1]
        joltage_str = strs[-1]
        m = mach()
        m.goal = cls.parse_goal_str(goal_str)
        m.buttons = [cls.parse_button_str(s) for s in button_strs]
        m.joltage = cls.parse_joltage_str(joltage_str)
        return m

    @classmethod
    def parse_goal_str(cls, s):
        s = s.strip("[]")
        g = []
        for c in s:
            if c == '#':
                g.append(1)
            else:
                g.append(0)
        return tuple(g)

    @classmethod
    def parse_button_str(cls, s):
        s = s.strip("()")
        ss = s.split(',')
        return [int(n) for n in ss]

    @classmethod
    def parse_joltage_str(cls, s):
        s = s.strip("{}")
        ss = s.split(',')
        return tuple([int(n) for n in ss])

    def apply_state_press(self, state, button):
        new_state = [i for i in state]
        for b in button:
            new_state[b] = 1 ^ new_state[b]
        return tuple(new_state)

    def min_presses(self):
        orig_state = tuple(0 for i in self.goal)
        cur_states = [orig_state]
        all_states = set([orig_state])
        new_states = []
        num_presses = 0
        while num_presses < len(self.buttons):
            num_presses += 1
            for s in cur_states:
                for b in self.buttons:
                    t = self.apply_state_press(s, b)
                    if t == self.goal:
                        return num_presses
                    if t not in all_states:
                        all_states.add(t)
                        new_states.append(t)
            cur_states = new_states
            new_states = []
        return -1

    # This search-based method of accumulating joltage is
    # far too slow.  This needs to be redone using either
    # numpy or sympy.

    def button_has(self, i):
        return [1 if i in b else 0 for b in self.buttons]

    def button_array(self):
        return [self.button_has(i) for i in range(len(self.goal))]

    def apply_joltage_press(self, state, button):
        new_state = [i for i in state]
        for b in button:
            new_state[b] += 1
        return tuple(new_state)
    
    def joltage_overshot(self, state):
        for i,v in enumerate(state):
            if v > self.joltage[i]:
                return True
        return False

    def min_joltage_presses(self):
        orig_state = tuple(0 for i in self.joltage)
        cur_states = [orig_state]
        all_states = set([orig_state])
        new_states = []
        num_presses = 0
        while num_presses < sum(self.joltage):
            num_presses += 1
            for s in cur_states:
                for b in self.buttons:
                    t = self.apply_joltage_press(s, b)
                    if t == self.joltage:
                        print(f"Returning {num_presses} after {len(all_states)} states.")
                        return num_presses
                    if self.joltage_overshot(t):
                        continue
                    if t not in all_states:
                        all_states.add(t)
                        new_states.append(t)
            cur_states = new_states
            new_states = []
        return -1

def min_presses(filename):
    mach_strs = open(filename, "r").read().splitlines()
    tot = 0
    for s in mach_strs:
        m = mach.from_mach_str(s)
        tot += m.min_presses()
    return tot

def min_joltage_presses(filename):
    mach_strs = open(filename, "r").read().splitlines()
    tot = 0
    for s in mach_strs:
        m = mach.from_mach_str(s)
        tot += m.min_joltage_presses()
    return tot

def main():
    print("min presses test: ", min_presses("day10_test.txt"))
    print("min presses input: ", min_presses("day10_input.txt"))
    # print("min joltage presses test: ", min_joltage_presses("day10_test.txt"))
    # print("min joltage presses input: ", min_joltage_presses("day10_input.txt"))

if __name__ == "__main__":
    main()
