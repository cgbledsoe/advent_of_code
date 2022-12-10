test_strInput = """30373
25512
65332
33549
35390"""

with open('2022/puzzle_inputs/8.txt') as file:
    strInput = file.read()

in_square = [list(x) for x in strInput.split('\n')[:-1]]
print(len(in_square),len(in_square[0]))

import numpy as np
mask = np.zeros((99,99))
square = np.array(in_square, dtype=object)
print(mask.shape, square.shape)

# check visibility from left
def check_visibility(square, mask):
    min_val = 0
    for i, row in enumerate(square):
        for j, value in enumerate(row):
            if j == 0:
                mask[i,j] = 1
                min_value = square[i,j]
            if square[i,j] > min_value:
                mask[i,j] = 1
                min_value = square[i,j]
            
    return square, mask

# rotate array around to check visibility from each side
for i in range(4):
    square, mask = check_visibility(square, mask)
    square = np.rot90(square)
    mask = np.rot90(mask)
    
# 1 - 1814
print(mask.sum())

# find the max scenic score
def rotate_indices(square, index, n):
    idx = index[0]
    idy = index[1]
    for i in range(n):
        idy_new = idx
        idx = square.shape[0]-1-idy
        idy = idy_new
    return idx, idy

def count_trees(square, mask):
    for i, row in enumerate(square):
        for j, col in enumerate(row):
            scores = []
            value = square[i,j]
            # have to rotate 4 times
            for k in range(4):
                idx, idy = rotate_indices(square,(i,j), k)
                if(idy == (square.shape[1]-1)):
                    scores.append(0)
                    square = np.rot90(square)
                    continue
                else:
                    next_value = square[idx,idy+1]
                counter = 1
                while next_value < value:
                    counter += 1
                    if(idy + counter > (square.shape[1]-1)):
                        counter -= 1
                        break
                    else:
                        next_value = square[idx,idy+counter]
                scores.append(counter)
                square = np.rot90(square)
            scenic_score = scores[0]*scores[1]*scores[2]*scores[3]
            mask[i,j] = scenic_score
            # print(value, i, j)
    return square, mask


mask = np.zeros((99,99))
square = np.array(in_square,dtype=np.uint8)

count_trees(square,mask)

# 2 - 330786
print(mask.max())
