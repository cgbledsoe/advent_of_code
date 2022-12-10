with open('2022/puzzle_inputs/4.txt') as file:
    strInput = file.read()

pairs = [x.split(',') for x in strInput.split('\n')][:-1]

count = 0
for person in pairs:
    try:
        # range should be +1
        x1, x2 = person[0].split('-')
        y1, y2 = person[1].split('-')
        
        x1 = int(x1)
        x2 = int(x2) + 1
        y1 = int(y1)
        y2 = int(y2) + 1
        set1 = set(range(x1,x2))
        set2 = set(range(y1,y2))
        cond1 = set1.issubset(set2)
        cond2 = set2.issubset(set1)
    except:
        print(person)
    if(cond1 | cond2):
        count += 1
        
# 1 - 584
print(count)


count = 0
for person in pairs:
    try:
        # range should be +1
        x1, x2 = person[0].split('-')
        y1, y2 = person[1].split('-')
        
        x1 = int(x1)
        x2 = int(x2) + 1
        y1 = int(y1)
        y2 = int(y2) + 1
        set1 = set(range(x1,x2))
        set2 = set(range(y1,y2))
        cond1 = len(set1.intersection(set2)) > 0
    except:
        print(person)
    if(cond1):
        count += 1
        
# 2 - 933
print(count)
