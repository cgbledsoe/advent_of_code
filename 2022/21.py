from collections import deque
with open('2022/puzzle_inputs/21.txt') as file:
    strInput = file.read()

test_strInput = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

operators = {
    '+': lambda a, b: a+b,
    '-': lambda a, b: a-b,
    '*': lambda a, b: a*b,
    '/': lambda a, b: a/b,
}

reverse_operators = {
    ('+',True): lambda a, b: a-b,
    ('-',True): lambda a, b: a+b,
    ('*',True): lambda a, b: a/b,
    ('/',True): lambda a, b: a*b,

    ('+',False): lambda a, b: a-b,
    ('-',False): lambda a, b: b-a,
    ('*',False): lambda a, b: a/b,
    ('/',False): lambda a, b: b/a,
}

def main(monkeys):
    # dangerous
    # register = [exec(x) for x in monkeys]
    # print(locals()['root'])

    # instead populate a dictionary with a stack
    monkey_business = {}
    monkey_stack = deque()
    monkey_stack.extend(monkeys)

    while monkey_stack:
        monkey = monkey_stack.popleft()
        key, values = monkey.split('=')
        values_list = values.strip().split(' ')
        # int string is all messed up in the keys and values
        if(len(values_list) == 1):
            monkey_business[key] = int(values_list[0])
        else:
            try:
                if(values_list[1] == '+'):
                    monkey_business[key] = monkey_business[values_list[0]] + monkey_business[values_list[2]]
                elif(values_list[1] == '-'):
                    monkey_business[key] = monkey_business[values_list[0]] - monkey_business[values_list[2]]
                elif(values_list[1] == '*'):
                    monkey_business[key] = monkey_business[values_list[0]] * monkey_business[values_list[2]]
                else:
                    monkey_business[key] = monkey_business[values_list[0]] / monkey_business[values_list[2]]
            except:
                # if I can solve it, add it to the end of the stack
                # this will be infinite because they get added to the loop in the same order..
                monkey_stack.append(monkey)

    # what if I make a stack adding things to the dict
    # the stack has try except and while on the stack it isn't in dict yet..

    return monkey_business

def propagate(key, known_dict, ops_dict):
    while key not in known_dict:
        for ops_key, (a, task, b) in ops_dict.items():
            # iterate over the operations dictionary
            # if the key in the operations dict is already in known dict, continue
            if ops_key in known_dict:
                continue
            # if ops_key isn't in known dict but it's children a and b are then 
            # calculate it and add to known_dict
            if (a in known_dict) and (b in known_dict):
                aa = known_dict[a]
                bb = known_dict[b]
                # if one of the components is none then propagate none up the tree
                if aa is None or bb is None:
                    v = None
                # if neither is none, do the math
                else:
                    v = operators[task](known_dict[a],known_dict[b])
                known_dict[ops_key] = v
 
def main2(monkeys):

    # convert humn to None
    known_monkey_business = {}
    operations = {}
    # i need a new dictionary
    # now walk up the tree and 
    for monkey in monkeys:
        key, values = monkey.split('=')
        values_list = values.strip().split(' ')
        # int string is all messed up in the keys and values
        if(len(values_list) == 1):
            known_monkey_business[key] = int(values_list[0])
        else:
            a, op, b = values_list
            operations[key] = (a, op, b)
    
    known_monkey_business['humn'] = None
    first, _, second = operations['root']

    propagate(first, known_monkey_business, operations)
    propagate(second, known_monkey_business, operations)

    # if the first component in root is none then we want to target it 
    # and we should know the integer value of the second component
    if known_monkey_business[first] is None:
        target = first
        current = known_monkey_business[second]
    else:
        target = second
        current = known_monkey_business[first]

    while target != 'humn':
        # so we don't know what target
        # find the pieces that make up target
        a, op, b = operations[target]

        # if the first piece of target is None
        # reset target to the first piece and subtract out the value of the component b
        if known_monkey_business[a] is None:
            target = a
            current = reverse_operators[(op, True)](current, known_monkey_business[b])
        else:
            target = b
            current = reverse_operators[(op, False)]( current, known_monkey_business[a])

    solution = int(current)
    return solution

if __name__ == '__main__':
    monkeys = [x.replace(":","=") for x in strInput.splitlines() if x != '']
    monkey_business = main(monkeys)
    print(monkey_business['root'])
    print(main2(monkeys))




# part 2
# what number does humn need to yell so that root[0] == root[1] is True
# the number in humn of the input string is now irrelevant
# build a big substitution tree and solve for humn
# start with root
# x == y
# but x  == z*w and z = y-v etc..
# solve for humn..
# so humn becomes an X a symbolic value and then at the end I should get
# 512 + x = 1000 or something like that?

# monkey_business = {} # defaultdict(lambda: )
# monkey_stack = deque()
# monkey_stack.extend(monkeys)

# while monkey_stack:
#     monkey = monkey_stack.popleft()
#     key, values = monkey.split('=')
#     values_list = values.strip().split(' ')
#     # int string is all messed up in the keys and values
#     if key == 'humn':
#         monkey_business[key] = 900000
#     elif(len(values_list) == 1):
#         monkey_business[key] = int(values_list[0])
#     else:
#         try:
#             if key == 'root':
#                 print(monkey_business[values_list[0]],monkey_business[values_list[2]],monkey_business[values_list[0]] == monkey_business[values_list[2]])
#             elif(values_list[1] == '+'):
#                 monkey_business[key] = monkey_business[values_list[0]] + monkey_business[values_list[2]]
#             elif(values_list[1] == '-'):
#                 monkey_business[key] = monkey_business[values_list[0]] - monkey_business[values_list[2]]
#             elif(values_list[1] == '*'):
#                 monkey_business[key] = monkey_business[values_list[0]] * monkey_business[values_list[2]]
#             else:
#                 monkey_business[key] = monkey_business[values_list[0]] / monkey_business[values_list[2]]
#         except:
#             # if I can solve it, add it to the end of the stack
#             # this will be infinite because they get added to the loop in the same order..
#             monkey_stack.append(monkey)
