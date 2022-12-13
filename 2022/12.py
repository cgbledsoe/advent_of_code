import heapq

with open('2022/puzzle_inputs/12.txt') as file:
    strInput = file.read()

test_strInput = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

grid = [list(x) for x in strInput.split('\n')]

# print(len(grid),len(grid[0]))

# get start/end coordinates
for i, row in enumerate(grid):
    if('S' in row):
        start_row = i
        start_col = row.index('S')
    if('E' in row):
        end_row = i
        end_col = row.index('E')

# print(start_row, start_col, grid[start_row][start_col])
# print(end_row, end_col, grid[end_row][end_col])

# convert alphabet grid to numeric
# start is of height 0 (min) and end is of height 25 (max)
decoder = {'S':0,'E':25}
for i in range(97,123):
    letter = chr(i)
    decoder[letter] = i-97

num_grid = [[decoder[y] for y in x] for x in grid]
[print(x) for x in num_grid]

print()

# down, right, up, left
moves = [(1,0),(0,1),(-1,0),(0,-1)]

# this determines if an edge exists..
# can only move up 1, down as many as possible
def is_valid_move(curr_index,move):
    current_position = num_grid[curr_index[0]][curr_index[1]]
    try:
        next_position = num_grid[curr_index[0]+move[0]][curr_index[1]+move[1]]
    except:
        return False
    if((current_position - next_position) > 1):
        return False
    return True

def make_move(curr_index, move):
    next_position = (curr_index[0]+move[0],curr_index[1]+move[1])
    return next_position


# dijkstras from https://bradfieldcs.com/algos/graphs/dijkstras-algorithm/
def calculate_distances(graph, starting_vertex):
    # distances becomes an array
    # distances = {vertex: float('infinity') for vertex in graph}
    graph_shape = (len(graph),len(graph[0]))
    distances = [[float('infinity')] * graph_shape[1] for _ in range(graph_shape[0])] # [[float('infinity')] * graph_shape[1]] * graph_shape[0]
    distances[starting_vertex[0]][starting_vertex[1]] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex[0]][current_vertex[1]]:
            continue
        
        neighbors = []
        for move in moves:
            can_move = is_valid_move(current_vertex, move)
            if can_move:
                neighbors.append(make_move(current_vertex, move))

        for neighbor in neighbors:
            distance = current_distance + 1

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor[0]][neighbor[1]]:
                distances[neighbor[0]][neighbor[1]] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

starting_vertex = (end_row, end_col)
distance_grid = calculate_distances(num_grid, starting_vertex)
[print(x) for x in distance_grid]
# 1 - 394
print(distance_grid[start_row][start_col])

min_distance = distance_grid[start_row][start_col]
for row, entries in enumerate(num_grid):
    for col, value in enumerate(entries):
        if value == 0:
            min_distance = min(min_distance, distance_grid[row][col])

print(min_distance)

# rather than from a defined starting point, find min distance from any of the letter a's or any 0s
# mask the num_grid to get all 0s
# then use that mask to mask the distance grid

