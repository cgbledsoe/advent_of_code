with open('2022/puzzle_inputs/10.txt') as file:
    strInput = file.read()

def decode_operation(line):
    decoder = {'noop':1,
               'addx':2}

    parse_line = line.split(' ')
    operation = parse_line[0]
    n_cycles = decoder[operation]
    modifier = 0
    if(n_cycles > 1):
        modifier = parse_line[1]
    return operation, n_cycles, int(modifier)

interesting_cycles = [20, 60, 100, 140, 180, 220]
interesting_register = []

register = 1
current_cycle = 0

max_register = 1

# screen = ['.'*40]*6
screen_1d = ['.']*240

for line in strInput.split('\n')[:-1]:
    operation, n_cycles, register_modifier = decode_operation(line)
    for cycle in range(n_cycles):
        if((current_cycle%40) in [register-1, register, register+1]):
            screen_1d[current_cycle] = "#"
        current_cycle += 1
        if(current_cycle in interesting_cycles):
            interesting_register.append(register)
        if((operation == 'addx') & (cycle == 1)):
            register += register_modifier
        max_register = max(max_register, register)
            

signal_strength = [(interesting_cycles[i] * interesting_register[i]) for i in range(len(interesting_cycles))]

# 1 - 17940
print(sum(signal_strength))
print(max_register)
print(current_cycle)


# screen = ['.'*40]*6
# screen_1d = ['.'*240]

def print_screen(screen):
    return [print(row) for row in screen]

screen_2d = []
for i in range(6):
    screen_2d.append(''.join(screen_1d)[(40*i):(40*(i+1))])

print_screen(screen_2d)

# screen is 6, 40 0-indexed
# crt draws 1 pixel each clock cycle
# cycles are 1-indexed cycle 1 draws position 0 and cycle 40 draws position 39
# draw # if lit sprite or . if dark sprite
# sprite is a kernel that is 3 wide and 1 tall, the middle pixel is the one of interest
# x register sets the position of the middle of the sprite's 3 pixels
# so the CRT and sprite get out of alignment based on the register vlaue

# when the index of the CRT is on the sprite then we draw something

# register is the screen index
# crt_index is new variable that is represented by dividing the cycle count by 


# max_register is 39 (1-39, because it's middle the 0 and 40 are taken care of with the kernel tails)
# max crt_index is 240, that's how many cycles we do..
# crt_index % 240 or 239
# then % 40 or 39 gives row
#  then crt_index%40 or 39 gives column
# if crt_index in [register-1,register,register+1]:
    # screen

# register = 1
# current_cycle = 0
# crt_index = current_cycle

# for line in strInput.split('\n')[:-1]:
#     operation, n_cycles, register_modifier = decode_operation(line)
#     for cycle in range(n_cycles):
#         current_cycle += 1
#         if(current_cycle in interesting_cycles):
#             interesting_register.append(register)
#         if((operation == 'addx') & (cycle == 1)):
#             register += register_modifier
