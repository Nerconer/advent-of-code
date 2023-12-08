import re

input = open(0).read().split('\n\n')

number_of_stacks = int(input[0].split('\n')[-1].split()[-1])

stacks = [ [] for _ in range(number_of_stacks) ]
    
for row in input[0].splitlines()[0:-1]:
    stack = []
    for index, elem in enumerate(range(0, len(row), 4)):
        if row[elem:elem+4] != '    ' and row[elem:elem+4] != '   ':
            stacks[index].append(row[elem:elem+4].replace('[', '').replace(']', ''))

for stack in stacks:
    stack.reverse()
      
stacks_part_two = [x[:] for x in stacks]
commands = input[1].splitlines()

def part_one() -> str:
    for command in commands:
        m, f, t = map(int, re.findall('\\d+', command))
        
        while(m):
            val = stacks[f-1].pop().strip()
            stacks[t-1].append(val)
            m -= 1

    result = ""
    for stack in stacks:
        result += stack.pop()
        
    return result

def part_two() -> str:
    for command in commands:
        m, f, t = map(int, re.findall('\\d+', command))
        
        arr = []
        while(m):
            elem = stacks_part_two[f-1].pop().strip()
            arr.append(elem)
            m -= 1
        arr.reverse()
        for elem in arr:
            stacks_part_two[t-1].append(elem)

    result = ""
    for stack in stacks_part_two:
        result += stack.pop()
        
    return result

print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')