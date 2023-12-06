input = open(0).read().splitlines()

total_pairs = []
for line in input:
    pairs = []
    first_elf, second_elf = line.split(',')
    pairs.append(list(map(int, first_elf.split('-'))))
    pairs.append(list(map(int, second_elf.split('-'))))
    total_pairs.append(pairs)

def part_one():
    num_fully_contained = 0
    for pairs in total_pairs:
        start_first, end_first = pairs[0]
        start_second, end_second = pairs[1]
        
        # First fully contains second
        if start_first <= start_second and end_first >= end_second:
            num_fully_contained += 1
        # Second fully contains first
        elif start_first >= start_second and end_first <= end_second:
            num_fully_contained += 1
    return num_fully_contained

def part_two():
    num_partially_contained = 0
    for pairs in total_pairs:
        start_first, end_first = pairs[0]
        start_second, end_second = pairs[1]
        
        overlap_start = max(start_first, start_second)
        overlap_end = min(end_first, end_second)
        
        if overlap_start <= overlap_end:
            num_partially_contained += 1

    return num_partially_contained
            
print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')