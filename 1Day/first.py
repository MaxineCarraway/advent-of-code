import sys

with open(sys.argv[1], 'r') as f:
    lines = [list(map(int, line.split())) for line in f.readlines()]

list1 = []
list2 = []
for line in lines:
    list1.append(line[0])
    list2.append(line[1])

list1.sort()
list2.sort() 


# part1 = lines
part1 = sum(abs(x1 - x2) for x1, x2 in zip(list1, list2))
print(f"Part 1: {part1}")

# This sum loops through each item in list1 (using x) 
# then creates a new listbased on the sum inside () 
# the comprehension list will include only elements that match 'x' 
# 'len' is counting the list generated by the last step 'x'
# 'x *' multiples the element from list 1 by how many times it appears in list2 
# 'sum()' is adding up everything calculated for each 'x' in list1
part2 = sum(x * len([y for y in list2 if y == x]) for x in list1) 
print(f"Part 2: {part2}") 