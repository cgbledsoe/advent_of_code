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
        loc = -(abs(mValue[0]) % (n_values-1))
    else:
        loc = mValue[0] % (n_values-1)
    # new for part 2
    mixed_list.insert(loc, mValue)
    # if(value[1] == False):
        # mixed_list.insert(loc, (mValue[0], True))
    # else:
        # mixed_list.insert(loc, (mValue[0], False))
    # end new for part 2
    # so root loc is 0-idx but it becomes positive
    # so negative number turns into positive
    # this correctly tells me where it is but not a good location for comparison
    # 7 - 1
    # not sure why I had to mod by n_values-1..
    # the list length is n but the actual max index is n-1 
    # so if index is greater than n-1 we'll need to wrap around..
    root_loc = (n_values + (0 - idx)) % (n_values-1)
    if ((loc > root_loc) & (idx != 0)):
        idx += 1
    mixed_list.rotate(idx)
    return True

def main(values, mixes, zero_index):
    mixed_list = deque()
    mixed_list.extend(values)

    n_values = len(values)
    # new for part 2
    # look_for = False
    for iter in range(mixes):
        for i, value in enumerate(values):
            move(mixed_list, value, n_values)
            # if((iter % 2) == 0):
                # move(mixed_list, value, n_values)
            # else:
                # value = (value[0], True)
                # move(mixed_list, value, n_values)
        # print(f"Was looking  for {look_for}, now looking for {not look_for}")
        # look_for = not look_for
    # alternate between looking for true and looking for false
    # end new for part 2

    
    rot_root = mixed_list.index((0, zero_index))
    # rot_root = mixed_list.index((0, look_for))
    mixed_list.rotate(-rot_root)
    indxs = [1000%n_values, 2000%n_values, 3000%n_values]
    response = [mixed_list[x][0] for x in indxs]
    print(response)
    return sum(response)


if __name__ == '__main__':
    decryption_key = 811589153
    mixes = 10
    values = [(int(x)*decryption_key,instance) for instance, x in enumerate(strInput.splitlines()) if x != '']
    zero_index = 0 
    for i, value in enumerate(values):
        if value[0] == 0:
            zero_index = i

    # values = [(int(x)*decryption_key,False) for x in test_strInput.splitlines() if x != '']
    # 1 - 872 is too low
    # part 1 -  2275 is correct answer, had to subtract 1 from my modulus with lislt length.
    # not sure why? because I pop out an element?
    # part 2 - 1453556173023 is too low
    # need to enumerate the values rather than use booleans
    # this will make things a lot easier anyways..
    # then non-unique values won't be grabbed.
    # part 2 is 4090409331120
    print(main(values,mixes, zero_index))
