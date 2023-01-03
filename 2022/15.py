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
y = 2_000_000 # 10

# commenting out part 1 because it's taking up too much time
for sensor in  sensor_distances.keys():
        ineligible_points(sensor, y, locations)

unique_locations = set(locations)
# can't put a beacon on another beacon
ineligible_locations = unique_locations.difference(beacons) 
# 1 - 4737443
print(len(ineligible_locations))

rows = 4_000_001
for y in range(rows):
    locations = []
    if(y%1_000_000 == 0):
        print(f'Checking {y}th row')
    for sensor in  sensor_distances.keys():
        dist = sensor_distances[sensor]
        dist -= abs(y - sensor[0])
        if dist < 0:
            continue
        locations.append((max(sensor[1] - dist, 0), min(s, sensor[1] + dist)))
    locations.sort()

    row_range = (0,0)
    for r in locations:
        if r[0] <= min(row_range[1], r[1]):
            row_range = (row_range[0], max(row_range[1], r[1]))
        else:
            print((row_range[1] + 1) * 4000000 + y)

# 2 - 11482462818989
