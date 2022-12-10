with open('2022/puzzle_inputs/1.txt') as file:
    strInput = file.read()

elf_lists = [x.split() for x in strInput.split('\n\n')]

elf_lists_int = []
for i, elf in enumerate(elf_lists):
    elf_lists_int.append([int(x) for x in elf])

elf_cal_sum = [sum(x) for x in elf_lists_int]

elf_cal_sum.sort()

# 1 - 74918
print(elf_cal_sum[-1])

# 2 - 209914
print(sum(elf_cal_sum[-3:]))
