
rucksacks = open(0).read().splitlines()

def part_one():
    shared = []
    for rucksack in rucksacks:
        first = rucksack[:len(rucksack)//2]
        second = rucksack[len(rucksack)//2:]
        
        for ff in first:
            if ff in second:
                if ord('a') <= ord(ff) <= ord('z'):
                    shared.append(ord(ff) - ord('a') + 1)
                else:
                    shared.append(ord(ff) - ord('A') + 26 + 1)
                break
    return sum(shared)

def part_two():
    groups = []
    for i in range(0, len(rucksacks), 3):
        groups.append(rucksacks[i:i+3])
    
    shared = []
    for group in groups:
        first = group[0]
        second = group[1]
        third = group[2]
        
        for ff in first:
            if ff in second and ff in third:
                if ord('a') <= ord(ff) <= ord('z'):
                    shared.append(ord(ff) - ord('a') + 1)
                else:
                    shared.append(ord(ff) - ord('A') + 26 + 1)
                break
        
    return sum(shared)
            
print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')
