import re
from collections import defaultdict

with open('2022/puzzle_inputs/15.txt') as file:
    strInput = file.read()

test_strInput = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

def calculate_manhattan_distance(pos1, pos2):
    dx = abs(pos1[0] - pos2[0])
    dy = abs(pos1[1] - pos2[1])
    return dx + dy

def ineligible_points(sensor, y, list_ineligible_points):
    # sensor is correctly (row, col)
    # y refers to row
    steps_allowed = sensor_distances[sensor]
    nearest_point = (y, sensor[1])
    target_distance = calculate_manhattan_distance(nearest_point, sensor)
    if target_distance < steps_allowed:
        diff = steps_allowed - target_distance
        for col in range(sensor[1]-diff, sensor[1]+diff+1):
            list_ineligible_points.append((y,col))
    elif target_distance == steps_allowed:
        list_ineligible_points.append(nearest_point)
    return list_ineligible_points

positions = [re.findall(r'(-?\d+)', line) for line in strInput.splitlines() if line != '']

max_beacon_distance = defaultdict(lambda: 0)
sensor_distances = defaultdict(lambda: 0)

# x is the column and y is the row..
for row in positions:
    sensor_col, sensor_row, beacon_col, beacon_row  = list(map(int, row))

    sensor = (sensor_row, sensor_col)
    beacon = (beacon_row, beacon_col)
    
    sensor_dist = calculate_manhattan_distance(sensor, beacon)
    
    sensor_distances[sensor] = sensor_dist

    if(sensor_dist > max_beacon_distance[beacon]):
        max_beacon_distance[beacon] = sensor_dist

beacons = set(list(max_beacon_distance.keys()))
locations = []
y = 10 # 2_000_000

# commenting out part 1 because it's taking up too much time
# for sensor in  sensor_distances.keys():
        # ineligible_points(sensor, y, locations)
# unique_locations = set(locations)
# can't put a beacon on another beacon
# 1 - 4737443
# print(len(unique_locations.difference(beacons)))

s = 10_001
for y in range(0,s):
    locations = []
    if(y%10_000 == 0):
        print(f'Checking {y}th row')
    for sensor in  sensor_distances.keys():
        ineligible_points(sensor, y, locations)
    unique_locations = set(locations)
    eligible_locations = []
    for i in range(0,s):
        eligible_locations.append((y,i))
    eligible_set = set(eligible_locations)
    valid_positions = eligible_set.difference(unique_locations)
    if(len(valid_positions) != 0):
        print(valid_positions)
        break

# 8:10 0
# 8:

# part 2
# distress coords must have x and y between 0, 4_000_000
# tuning_freq = (x * 4_000_000) + y
# now i need to find an eligible coordinate in the grid (0,4E6)
# so there is one spot eligible amidst (4E6 x 4E6)
# I need to find where the sensors don't line up..
# I need to find ELIGIBLE locations

# can't put a beacon on another beacon
# find the points outside of the sensor's view
# so their is always another beacon between the sensor and the distress beacon
# so I can make a big array and start to delete parts of it with the existing beacons..this feels too lengthy
# each sensor has a radius around it. 
# def eligible_points(sensor, y, list_ineligible_points):
#     steps_allowed = sensor_distances[sensor]
#     nearest_point = (y, sensor[1])
#     target_distance = calculate_manhattan_distance(nearest_point, sensor)
#     if target_distance < steps_allowed:
#         diff = steps_allowed - target_distance
#         for col in range(sensor[1]-diff, sensor[1]+diff+1):
#             list_ineligible_points.append((y,col))
#     elif target_distance == steps_allowed:
#         list_ineligible_points.append(nearest_point)
#     return list_ineligible_points

# I can grab each sensor's coordinates and then make a radius in 4 directions then find out which ones overlap

# so I have all these sensors and their corresponding radii
# I want to find the point where they don't overlap
# for sensor in sensor_distances.keys():
#     x = sensor_distances[sensor]
#     sensor_row_span = (max(0, sensor[0] - x), min(sensor[0] + x, 4_000_000))

# check each quadrant of the grid to see where there is an empty space
# for each sensor
# find the array height which is 2x the sensor radius
# find the top right position and the bottom left then we'll add this to our existing array

# functional part 1
# too slow for big part 2
# import numpy as np

# def diamond(n):
#     a = np.arange(n)
#     b = np.minimum(a,a[::-1])
#     # this operation is taking WAYY too long
#     return (b[:,None]+b)>=(n-1)//2

# s = 1_000_000 # 20 # 4_000_000
# # move in chunks of 10_000 x 10_000 pairs?
# grid = np.zeros((s,s),dtype=bool)
# for sensor in sensor_distances.keys():
#     # print(sensor, grid.size - grid.sum())
#     sensor_radius = sensor_distances[sensor]
#     side = 1+(2*sensor_radius) # the length of the side of the matrix
#     x0y0 = (sensor[0]-sensor_radius, sensor[1]-sensor_radius) # the location of the top left corner of the matrix
#     sensor_space = diamond(side) # the matrix itself is wrong, it's doubling up rows..
#     # need to trim sensor_space to the size 
#     grid_row_start = max(0,x0y0[0]) # if the sensor is negative then start at 0 in the
#     grid_row_end = min(x0y0[0]+side,s)
#     grid_nrows = grid_row_end-grid_row_start
#     grid_col_start = max(0,x0y0[1])
#     grid_col_end = min(x0y0[1]+side,s)
#     ncols = grid_col_end-grid_col_start
    
#     grid_x0y0 = (grid_row_start, grid_col_start) # this is the modified matrix start point, ensures it is on the grid
#     trim_sensor_space = sensor_space.copy()
#     if(x0y0[0] < 0):
#         # need to cut rows off the top of sensor_space
#         trim_length = abs(x0y0[0])
#         trim_sensor_space = trim_sensor_space[trim_length:,:]
#     if((x0y0[0]+side) > s):
#         # need to cut rowss of the bottom of sensor_space
#         trim_length = abs((x0y0[0]+side)-s)
#         trim_sensor_space = trim_sensor_space[:-trim_length,:]
#     if(x0y0[1] < 0):
#         # need to cut columns off the left side of sensor
#         trim_length = abs(x0y0[1])
#         trim_sensor_space = trim_sensor_space[:,trim_length:]
#     if((x0y0[1]+side) > s):
#         # need to remove rows from right side of sensor
#         trim_length = abs((x0y0[1]+side)-s)
#         trim_sensor_space = trim_sensor_space[:,:-trim_length]
    

#     # diamond_rows = (abs(stl[0]-row_start),nrows)
#     # diamons_cols = (abs(stl[1]-col_start),ncols)
#     # trim_sensor_space = sensor_space[diamond_rows[0]:diamond_rows[1],diamond_cols[0]:diamond_cols[1]]
#     grid[grid_row_start:grid_row_end,grid_col_start:grid_col_end] += trim_sensor_space

# print([grid[i,:] for i in range(grid.shape[0])])
# index = np.where(grid==False)
# print(index) # reverse x and y,
# print((index[1]*4_000_000)+index[0])

# add some print statements
