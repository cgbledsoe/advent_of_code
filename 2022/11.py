import math
import yaml  

with open('2022/puzzle_inputs/11.txt') as file:
    strInput = file.read()

split_strInput = strInput.split('Test: ')
fixed_strInput = ''.join(['Test:\n    Function: '+split_strInput[i] if i>0 else split_strInput[i] for i in range(len(split_strInput))])

state = yaml.safe_load(fixed_strInput)

monkeys = list(state.keys())
items_inspected = [0]*len(monkeys)
modulo_product = 1

# clean up yaml and set global variables
for monkey in monkeys:
    items = state[monkey]['Starting items']
    if type(items) == str:
        items = items.split(',')
        items = list(map(int, items))
    elif type(items) == int:
        items = [items]
    state[monkey]['Starting items'] = items
    modulo_product *= int(state[monkey]['Test']['Function'].split(' ')[-1])

def perform_monkey_business(monkey_state, monkey_index):
    # i think pop(0) is going slow, maybe try to reverse the list and pop?
    # pop is o(n2)
    # change this to a for loop and then clear the list at the end
    # while monkey_state['Starting items']:
        # item = monkey_state['Starting items'].pop(0)
    # still taking too long, I think new is growing way too big
    # how can I keep it small without messing up the modulo operation?
    # try dividing by the modulo? makes sense for multiply but not for add ops
    for item in monkey_state['Starting items']:
        items_inspected[monkey_index] += 1
        modulo = int(monkey_state['Test']['Function'].split(' ')[-1])
        old = item % modulo_product
        if(rounds == 10_000):    
            new = eval(monkey_state['Operation'].split('=')[-1])
        else:
            new = math.floor(eval(monkey_state['Operation'].split('=')[-1])/3)
        if(new%modulo == 0):
            new_monkey = int(monkey_state['Test']['If true'].split(' ')[-1])
            state[monkeys[new_monkey]]['Starting items'].append(new)
        else:
            new_monkey = int(monkey_state['Test']['If false'].split(' ')[-1])
            state[monkeys[new_monkey]]['Starting items'].append(new)
    state[monkeys[monkey_index]]['Starting items'] = []
    return True

rounds = 20
for i in range(rounds):
    for j, monkey in enumerate(monkeys):
        perform_monkey_business(state[monkey],j)
    if(i%1000 == 0):
        print(f"Round {i} completed!")

print(items_inspected)
items_inspected.sort(reverse=True)

# 1 - 117,624
# 2 - 16792940265
print(items_inspected[0]*items_inspected[1])

# rather than pop(0) which is O(n2)
# iterating and then clearing the list O(n)
# limit large numbers by dividing by something that all tests have in common
# the quotient of the mega modulo is shared

