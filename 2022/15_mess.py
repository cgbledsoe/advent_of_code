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

# min_row, max_row, min_col, max_col = [0, 0, 0, 0]

max_beacon_distance = defaultdict(lambda: 0)
sensor_distances = defaultdict(lambda: 0)
# for a given beacon what is the max distance a given sensor is away
# then for each beacon's max distance we can check for a list of coordinates, how many coordinates are less than that distance

# x is the column and y is the row..
for row in positions:
    sensor_col, sensor_row, beacon_col, beacon_row  = list(map(int, row))

    # min_row = min(min_row, sensor_row, beacon_row)
    # max_row = max(max_row, sensor_row, beacon_row)
    # min_col = min(min_col, sensor_col, beacon_col)
    # max_col = max(max_col, sensor_col, beacon_col)
    
    sensor = (sensor_row, sensor_col)
    beacon = (beacon_row, beacon_col)
    
    sensor_dist = calculate_manhattan_distance(sensor, beacon)
    
    sensor_distances[sensor] = sensor_dist

    if(sensor_dist > max_beacon_distance[beacon]):
        max_beacon_distance[beacon] = sensor_dist
    

# given a row, find the distance between all sensors/beacons and the elements in that row
# what positions are closer to a beacon than sensors
# what values of x produce a manhattan distance that is smaller than the nearest beacons
# find the max distance in the dictionary

# beacon can't be placed closer than the nearest sensor..

# sensor finds the nearest beacon
# if a sensor detects a beacon, you know there are no others beacons that close or closer to the sensor
# no beacon allowed if distance from new spot to sensor is less than distance of sensor to nearest beacon
# if a beacon is already there don't count it

max_d = max(list(sensor_distances.values())) #max(distance, key=distance.get)
y = 2_000_000
i = 0
# for x in range(min_col-max_d, max_col+max_d):
#     for sensor in sensor_distances.keys():
#         index_dist = calculate_manhattan_distance((y,x),sensor)
#         if(index_dist <= sensor_distances[sensor]):
#             if (y,x) not in set(max_beacon_distance.keys()):
#                 i+=1
#             # can't increment more than once per spot..
#             break

# print(i)
beacons = set(list(max_beacon_distance.keys()))
locations = []
for sensor in  sensor_distances.keys():
    ineligible_points(sensor, y, locations)

# can't put a beacon on another beacon
unique_locations = set(locations)

# 1 - 4737443
print(len(unique_locations.difference(beacons)))

# rather than check all indexes on the row
# check all beacons to see how much of 2_000_000 they touch?
# so the distance of the beacon past the row is equal to the number of squares
# but if there is overlap then I can't use that alone..
# symmetric about the column
# iterate over each beacon, find the difference between the sensor_distance and distance to the row in the same column
# then append to a list, make that list a set and at the end take the length of the set

# still has to be keyed off the sensor, because the furthest distance the beacon travels doesn't help
# there could be a beacon in between the nearest beacon and the further reaching beacon..

# (15,-2) has a max_d of 7 units
# 10,-2 is 5 units away
# so 10,-2 is off limits 10,-3 10,-4 10,-1 and 10,0
# so the range(col-diff,col+diff+1)


# part 2
# distress coords must have x and y between 0, 4_000_000
# tuning_freq = (x * 4_000_000) + y
# now i need to find an eligible coordinate in the grid (0,4E6)
