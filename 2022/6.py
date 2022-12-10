with open('2022/puzzle_inputs/6.txt') as file:
    strInput = file.read()

n = 14
for i, letter in enumerate(strInput):
    if i < n:
        continue
    lastn = strInput[i-n:i]
    if len(set(lastn)) == n:
        print(i, lastn)
        break
