block1, block2 = open(0).read().strip().split('\n\n')

workflows = {}
for workflow in block1.splitlines():
    name, rest = workflow[:-1].split('{')
    rules = rest.split(',')
    workflows[name] = ([], rules.pop())
    for rule in rules:
        comparison, target = rule.split(':')
        key = comparison[0]
        cmp = comparison[1]
        number = int(comparison[2:])
        workflows[name][0].append((key, cmp, number, target))
        
def part_one():
    def accepted_item(item: dict, name = 'in') -> bool:
        if name == 'R':
            return False
        if name == 'A':
            return True
        
        rules, fallback = workflows[name]
        
        for key, cmp, number, target in rules:
            if eval(f'{item[key]} {cmp} {number}'):
                return accepted_item(item, target)
        
        return accepted_item(item, fallback)
    
    
    total = 0 
    for rating in block2.splitlines():
        item = {}
        for variable in rating.strip('{').strip('}').split(','):
            char, value = variable.split('=')
            item[char] = int(value)
        
        if accepted_item(item):
            total += sum(item.values())
            
    return total

def part_two():
    ranges = {key: (1, 4000) for key in "xmas"}

    def count_ranges(ranges: dict, name = 'in') -> int:
        if name == 'R':
            return 0
        if name == 'A':
            product = 1
            for lo, hi in ranges.values():
                product *= hi - lo + 1
            return product
        
        rules, fallback = workflows[name]
        
        total = 0
        
        for key, cmp, number, target in rules:
            lo, hi = ranges[key]
            if cmp == '<':
                T = (lo, min(hi, number - 1))
                F = (max(lo, number), hi)
            else:
                T = (max(lo, number + 1), hi)
                F = (lo, min(hi, number))
            if T[0] <= T[1]:
                copy = dict(ranges)
                # Update the range
                copy[key] = T
                total += count_ranges(copy, target)
            if F[0] <= F[1]:
                ranges = dict(ranges)
                ranges[key] = F
            # T range has covered all of the possible values, skip the rest of the rules
            else:
                break
        # If we've reached the end of the rules, and there are still ranges left, we need to check the fallback
        else:
            total += count_ranges(ranges, fallback)
                
        return total

    return count_ranges(ranges)

print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')
    