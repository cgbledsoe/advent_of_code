from collections import deque

with open('2022/puzzle_inputs/20.txt') as file:
    strInput = file.read()

test_strInput = """1
2
-3
3
-2
0
4"""

def move(mixed_list, value, n_values):
    idx = mixed_list.index(value)
    mixed_list.rotate(-idx)
    mValue = mixed_list.popleft()
    if mValue[0] < 0:
        loc = -(abs(mValue[0]) % n_values)
    else:
        loc = mValue[0] % n_values
    mixed_list.insert(loc, (mValue[0], True))
    root_loc = 0 - idx
    if loc > root_loc:
        idx += 1
    mixed_list.rotate(idx)
    return True

def main(values):
    mixed_list = deque()
    mixed_list.extend(values)

    n_values = len(values)
    for i, value in enumerate(values):
        move(mixed_list, value, n_values)
    
    rot_root = mixed_list.index((0, True))
    mixed_list.rotate(-rot_root)
    indxs = [1000%n_values, 2000%n_values, 3000%n_values]
    response = [mixed_list[x][0] for x in indxs]
    print(response)
    return sum(response)

values = [(int(x),False) for x in strInput.splitlines() if x != '']

# mixed_list = deque()
# mixed_list.extend(values)

# # print(' '.join([str(x[0]) for x in mixed_list]))

# n_values = len(values)
# for i, value in enumerate(values):
#     # root is always 0 index at this point
#     # if i > 0:
#         # root = mixed_list[0][0]
#     idx = mixed_list.index(value)
#     # rotate value to left side of list
#     mixed_list.rotate(-idx)
#     mValue = mixed_list.popleft()
#     if mValue[0] < 0:
#         loc = -(abs(mValue[0]) % n_values)
#     else:
#         loc = mValue[0] % n_values
#     mixed_list.insert(loc, (mValue[0], True))
#     # if it gets inserted between the original home/root and the end it will mess up the rotation
#     # print(' '.join([str(x[0]) for x in mixed_list]))
#     root_loc = 0 - idx# mixed_list.index((root, False)) # change from 1 to root pre-rotation
#     # print(f"{value[0]=}, {idx=}, {loc=}, {root_loc=}")
#     if loc > root_loc:
#         idx += 1
#     mixed_list.rotate(idx)
#     # print(' '.join([str(x[0]) for x in mixed_list]))
#     # print()

rot_root = mixed_list.index((0, True))
mixed_list.rotate(-rot_root)
indxs = [1000%n_values, 2000%n_values, 3000%n_values]
response = [mixed_list[x][0] for x in indxs]
print(response)
sum(response)

def test_example1():
    test_case = deque()
    test_case.extend([(1, False), (2, False), (-3, False), (3, False), (-2, False), (0, False), (4, False)])
    solution = deque()
    solution.extend([(2, False), (1, True), (-3, False), (3, False), (-2, False), (0, False), (4, False)])
    assert move(test_case, (1, False), len(test_case)) == solution

test_example1()

def test_example2():
    assert move([2, 1, -3, 3, -2, 0, 4], 2) == [1, -3, 2, 3, -2, 0, 4]

def test_example3():
    assert move([1, -3, 2, 3, -2, 0, 4], -3) == [1, 2, 3, -2, -3, 0, 4]

def test_example4():
    assert move([1, 2, 3, -2, -3, 0, 4], 3) == [1, 2, -2, -3, 0, 3, 4]

def test_example5():
    assert move([1, 2, -2, -3, 0, 3, 4], -2) == [1, 2, -3, 0, 3, 4, -2]

def test_example6():
    assert move([1, 2, -3, 0, 3, 4, -2], 0) == [1, 2, -3, 0, 3, 4, -2]

def test_example7():
    assert move([1, 2, -3, 0, 3, 4, -2], 4) == [1, 2, -3, 4, 0, 3, -2]

def test_example8():
    assert move([1, 2, -3, 3, 0, 4, -2], 3) == [3, 1, 2, -3, 0, 4, -2]

def test_example9():
    assert move([1, 2, -3, 3, 0, 4, -2], -2) == [1, 2, -3, 3, -2, 0, 4]

def test_example10():
    assert move([4, -2, 5, 6, 7, 8, 9], -2) == [4, 5, 6, 7, 8, -2, 9]

def test_example11():
    assert move([4, 5, -2, 6, 7, 8, 9], -2) == [4, 5, 6, 7, 8, 9, -2]

def test_example12():
    assert move([4, 5, 6, 7, -2, 8, 9], -2) == [4, 5, -2, 6, 7, 8, 9]

def test_example13():
    assert move([4, 5, 6, 7, -2, 8, 0], 0) == [4, 5, 6, 7, -2, 8, 0]

print(main(values))
