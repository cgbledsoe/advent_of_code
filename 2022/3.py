with open('2022/puzzle_inputs/3.txt') as file:
    strInput = file.read()

prior_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority = {}
for i, letter in enumerate(prior_str):
    priority[letter] = i + 1

rucksacks = strInput.split('\n')[:-1]

priority_values = []
for sack in rucksacks:
    size = int(len(sack)/2)
    compartment1 = set(sack[:size])
    compartment2 = set(sack[size:])
    priority_values.append(priority[compartment1.intersection(compartment2).pop()])
    
# 1 - 7446
print(sum(priority_values))

priority_values = []
for i, sack1 in enumerate(rucksacks[::3]):
    sack1 = set(sack1)
    sack2 = set(rucksacks[(3*i)+1])
    sack3 = set(rucksacks[(3*i)+2])
    # intersect 1/2 and 2/3
    sack12 = sack1.intersection(sack2)
    sack23 = sack2.intersection(sack3)
    # intersection of the intersections
    priority_values.append(priority[sack12.intersection(sack23).pop()])
    
# 2- 2646
print(sum(priority_values))
