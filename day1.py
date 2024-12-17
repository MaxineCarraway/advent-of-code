import sys

with open(sys.argv[1], 'r') as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]

list1 = []
list2 = []
for line in lines:
    list1.append(line[0])
    list2.append(line[1])

# part1 = lines
part1 = list1
print(f"Part 1: {part1}")

part2 = list2
print(f"Part 2: {part2}")