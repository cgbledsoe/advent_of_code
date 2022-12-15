from itertools import chain
from functools import cmp_to_key

with open('2022/puzzle_inputs/13.txt') as file:
    strInput = file.read()

test_strInput = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""

def compare(left, right):
    if (isinstance(left,int) & isinstance(right, int)):
        if left == right:
            return None
        else:
            return left < right
    elif (isinstance(left, list) & isinstance(right, int)):
        return compare(left, [right])
    elif (isinstance(left, int) & isinstance(right, list)):
        return compare([left], right)
    else:
        for l, r in zip(left, right):
            result = compare(l,r)
            if (result == None):
                continue
            return result
        else:
            if((len(left) == len(right))):
                return None
            else:
                return len(left) < len(right)

packet_list = [x.split('\n') for x in strInput.split('\n\n')]

correct_order = []

for i, packets in enumerate(packet_list):
    pck1, pck2 = packets[:2]
    pck1 = eval(pck1)
    pck2 = eval(pck2)
    correct_sequence = compare(pck1,pck2)
    if(correct_sequence):
        correct_order.append(i+1)

# max is 11325
# 5806
print(sum(correct_order))

packet_list2 = [eval(x) for x in strInput.split('\n') if x!=""]
packet_list2.extend([[[2]],[[6]]])

# hijacked from regionsyx
def proper_compare(l, r):
    c = compare(l, r)
    # False
    # Left > Right
    if c == 0:
        return 1
    # True
    # Left < Right
    if c == 1:
        return -1
    # None
    # Left == Right
    return 0

# the key arg specifies an object which when passed a value returns a value
# the returned value is used to compare items in a list
sorted_packing_list2 = sorted(packet_list2, key=cmp_to_key(proper_compare))
x = sorted_packing_list2.index([[2]])+1
y = sorted_packing_list2.index([[6]])+1

# 23600
print(x*y)


def len_compare(l,r):
    if len(l) < len(r):
        return -1
    elif len(l) > len(r):
        return 1
    else:
        return 0
    
print(sorted(['colin','sarah_jane','albert_einstein','colinb'],key=cmp_to_key(len_compare)))
