# from aocd import get_data
import re

# strInput = get_data(day=5, year=2022)
with open('2022/puzzle_inputs/5.txt', 'r') as file:
    strInput = file.read()


def move_crates(state, from_pos, to_pos, num_crates=1, crane_model=9000):
    # single crate model
    if crane_model == 9000:
        for crate in range(num_crates):
            grab = state[from_pos].pop()
            state[to_pos].append(grab)
        return True
    # crane 9001 can grab multiple crates at once
    elif crane_model == 9001:
        grab = []
        for crate in range(num_crates):
            grab.append(state[from_pos].pop())
        grab.reverse()
        state[to_pos].extend(grab)
        return True
    else:
        return False

# initial state
crate_state = [[],
              ['F','C','J','P','H','T','W'],
              ['G','R','V','F','Z','J','B','H'],
              ['H','P','T','R'],
              ['Z','S','N','P','H','T'],
              ['N','V','F','Z','H','J','C','D'],
              ['P','M','G','F','W','D','Z'],
              ['M','V','Z','W','S','J','D','P'],
              ['N','D','S'],
              ['D','Z','S','F','M']]

# extract instructions from procedure
instructions = [re.findall('\d+',x) for x in strInput.split('\n')]

# execute instructions
for instruction in instructions[:-1]:
    num_crates = int(instruction[0])
    from_position = int(instruction[1])
    to_position = int(instruction[2])
    move_crates(crate_state, from_position, to_position, num_crates, crane_model=9000)
        
response = ""
for stack in crate_state[1:]:
    response += stack[-1]

print(response)
