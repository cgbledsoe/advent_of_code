with open('2022/puzzle_inputs/14.txt') as file:
    strInput = file.read()


test_strInput = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

# x coord is the column index
# y coord is the row index
lines = [[(eval(y)) for y in x.split(' -> ')] for x in strInput.split('\n') if x != '']

air, source, sand, rock = ['.', '+', 'o', '#']

def interpolate(pt1, pt2):
    # given a pair of points, return all points between them
    same_row = pt1[1] == pt2[1]
    same_col = pt1[0] == pt2[0]
    segment = []
    if(same_row):
        if(pt1[0] < pt2[0]):
            point = pt1
            while point != pt2:
                segment.append(point)
                point = (point[0]+1,point[1])
            segment.append(pt2)
        else:
            point = pt2
            while point != pt1:
                segment.append(point)
                point = (point[0]+1,point[1])
            segment.append(pt1)
    elif(same_col):
        if(pt1[1] < pt2[1]):
            point = pt1
            while point != pt2:
                segment.append(point)
                point = (point[0],point[1]+1)
            segment.append(pt2)
        else:
            point = pt2
            while point != pt1:
                segment.append(point)
                point = (point[0],point[1]+1)
            segment.append(pt1)
    else:
        print('Diagonal line?!',pt1,pt2)
    return segment

def draw_cave(lines):
    min_col, min_row = sand_source
    max_col, max_row = sand_source
    for line in lines:
        for point in line:
            min_col = min(min_col, point[0])
            min_row = min(min_row, point[1])
            max_col = max(max_col, point[0])
            max_row = max(max_row, point[1])
    cave_cols = 1 + (max_col - min_col)
    cave_rows = 1 + (max_row - min_row)
    cave = [[air] * cave_cols for x in range(cave_rows)]
    cave[sand_source[1]][sand_source[0]-min_col] = source

    for line in lines:
        for i in range(len(line[:-1])):
            segments = interpolate(line[i],line[i+1])
            for point in segments:
                cave[point[1]][point[0]-min_col] = rock

    bounds = (max_row,(min_col, max_col))
    return cave, bounds

def add_sand(cave, bounds):
    # modified
    sand_loc = (sand_source[0]-bounds[1][0], sand_source[1])#+1)
    cave[sand_loc[1]][sand_loc[0]] = sand
    return cave, sand_loc

def move_sand(cave, sand_loc, bounds):
    moves = [(0,1),(-1,1),(1,1)]
    for move in moves:
        new_sand_loc = (sand_loc[0] + move[0], sand_loc[1] + move[1])
        if(is_valid_move(cave, new_sand_loc)):
            if(is_in_bounds(cave, new_sand_loc, bounds)):
                cave[sand_loc[1]][sand_loc[0]] = air
                cave[new_sand_loc[1]][new_sand_loc[0]] = sand
                return move_sand(cave, new_sand_loc, bounds)
            else:
                return cave, False
        else:
            continue
    else:
        # being unable to move no longer means stable state. need another check
        if cave[sand_source[1]+1][sand_source[0]-bounds[1][0]+1] == sand:
            return cave, False
        else:
            return cave, True

def is_valid_move(cave, new_sand_loc):
    if(cave[new_sand_loc[1]][new_sand_loc[0]] == air):
        return True
    return False

def is_in_bounds(cave, new_sand_loc, bounds):
    floor = bounds[0]
    left_bound = bounds[1][0]-bounds[1][0]
    right_bound = bounds[1][1]-bounds[1][0]
    if new_sand_loc[1] <= floor:
        if left_bound <= new_sand_loc[0] <= right_bound:
            return True
    return False

sand_source = (500, 0)
cave, bounds = draw_cave(lines)
# part 2 draw a new cave with a floor
n = 150
floor = [(bounds[1][0]-n, bounds[0]+2),(bounds[1][1]+n, bounds[0]+2)]
lines.extend([floor])
cave, bounds = draw_cave(lines)
# end new
[print(''.join(x)) for x in cave]

in_bounds = True
# [print(''.join(x)) for x in cave]
i = 0

cond1 = cave[sand_source[1]+1][sand_source[0]-bounds[1][0]] == sand # below
cond2 = cave[sand_source[1]+1][sand_source[0]-bounds[1][0]-1] == sand # below, left
cond3 = cave[sand_source[1]+1][sand_source[0]-bounds[1][0]+1] == sand # below, right
cond4 = cond2 | cond3

while in_bounds:
    cave, sand_loc = add_sand(cave, bounds)
    cave, in_bounds = move_sand(cave, sand_loc, bounds)
    cave[sand_source[1]][sand_source[0]-bounds[1][0]] = source
    # [print(''.join(x)) for x in cave]
    i += 1
    if(all([cond1, cond4])):
        print(i)
        break
    if i == 150000:
        break
[print(''.join(x)) for x in cave]
# 1 - 888
print(i-1)
# 2 - 26461
print(i+1)

# cave[sand_source[1]+1][sand_source[0]-bounds[1][0]] = 'x'
# cave[sand_source[1]+1][sand_source[0]-bounds[1][0]-1] = 'x'
# cave[sand_source[1]+1][sand_source[0]-bounds[1][0]+1] = 'x'
# [print(''.join(x)) for x in cave]
