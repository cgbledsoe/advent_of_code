def decode_head_move(line):
    decoder = {'U':(-1,0),
              'R':(0,1),
              'L':(0,-1),
              'D':(1,0)}
    direction, steps = line.split(' ')
    dRow, dCol = decoder[direction]
    return (dRow, dCol), int(steps)

def tail_move_required(head, tail):
    row_displacement = abs(head[0]-tail[0])
    col_displacement = abs(head[1]-tail[1])
    if((row_displacement > 1) or (col_displacement > 1)):
        return True
    return False

def determine_tail_move(head, tail):
    row_displacement = head[0] - tail[0]
    col_displacement = head[1] - tail[1]
    # abs_displacement = 
    # at this point I know the absolute displacement requires a move
    # now just to tell what type of move
    if((col_displacement == 0) or (row_displacement == 0)):
        # row/cols
        coords = (row_displacement/2, col_displacement/2)
    else:
        # diagonals
        if(abs(row_displacement) > abs(col_displacement)):
            coords = (row_displacement/2, col_displacement)
        elif(abs(row_displacement) == abs(col_displacement)):
            coords = (row_displacement/2, col_displacement/2)
        else:
            coords = (row_displacement, col_displacement/2)
    return coords

def move(object, coords):
    dRow, dCol = coords
    object = (object[0] + dRow, object[1] + dCol)
    return object

def count_distinct_locs(prev_locs):
    unique_prev_locs = set(prev_locs)
    return len(unique_prev_locs)

def unit_tests():
    # rows/columns
    assert determine_tail_move((0,0),(-2,0)) == (1,0)
    assert determine_tail_move((0,0),(2,0)) == (-1,0)
    assert determine_tail_move((0,0),(0,-2)) == (0,1)
    assert determine_tail_move((0,0),(0,2)) == (0,-1)

    # wide diagonals
    assert determine_tail_move((0,0),(-2,1)) == (1,-1)
    assert determine_tail_move((0,0),(-2,-1)) == (1,1)
    assert determine_tail_move((0,0),(2,1)) == (-1,-1)
    assert determine_tail_move((0,0),(2,-1)) == (-1,1)
    
    # tall diagonals
    assert determine_tail_move((0,0),(1,-2)) == (-1,1)
    assert determine_tail_move((0,0),(-1,-2)) == (1,1)
    assert determine_tail_move((0,0),(1,2)) == (-1,-1)
    assert determine_tail_move((0,0),(-1,2)) == (1,-1)

    # symmetric large diagonal
    assert determine_tail_move((0,0),(-2,2)) == (1,-1)
    assert determine_tail_move((0,0),(-2,-2)) == (1,1)
    assert determine_tail_move((0,0),(2,2)) == (-1,-1)
    assert determine_tail_move((0,0),(2,-2)) == (-1,1)

# confirm moves make sense
unit_tests()

with open('2022/puzzle_inputs/9.txt') as file:
    strInput = file.read()

# now the head moves and then the 9 tails, I have to keep track of the last tail
head = (0,0)
num_tails = 9 # 1-6522, 9-2717
tails = [(0,0)] * num_tails

previous_tail_locs = [tails[-1]]

test_strInput = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

test2_strInput = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

max_d = 0
for n, line in enumerate(strInput.split('\n')[:-1]):
    dHead, steps = decode_head_move(line)
    for step in range(steps):
        head = move(head, dHead)
        for i, tail in enumerate(tails):
            if i == 0:
                if(tail_move_required(head, tail)):
                    dTail = determine_tail_move(head, tail)
                    tails[i] = move(tail, dTail)
                    if(i==(num_tails-1)):
                        previous_tail_locs.append(tails[i])
            else:
                if(tail_move_required(tails[i-1], tail)):
                    dTail = determine_tail_move(tails[i-1], tail)
                    tails[i] = move(tail, dTail)
                    max_dnew = max(max_d,(abs(tails[i-1][0]-tails[i][0])+abs(tails[i-1][1]-tails[i][1])))
                    if((max_dnew != max_d)):# & (max_dnew > 3)):
                        print(n, line, i, tails[i-1],tail,dTail, tails[i], max_dnew)
                    max_d = max_dnew
                    if(i==(num_tails-1)):
                        previous_tail_locs.append(tails[i])

print(count_distinct_locs(previous_tail_locs))
print(max_d)
# 2839 is wrong
# frame 83 is introducing error this was where deviation x == deviation y == 2
