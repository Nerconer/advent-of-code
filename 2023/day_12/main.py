from functools import cache

input = open(0).read().strip().splitlines()

def solve(part=1) -> int:
    @cache
    def count(cfg: str, nums: tuple):
        # Base case 1: We have no more strings and nums is empty, success
        if cfg == "":
            return 1 if nums == () else 0
        
        # Base case 2: Empty tuple and no more broken strings left, success
        if nums == ():
            return 0 if '#' in cfg else 1
        
        total = 0
        if cfg[0] in '.?':
            total += count(cfg[1:], nums)
        
        # Check nums[0] is smaller or equal to the length of the remaining string
        # Make sure there are not working inside the group
        # Check length matches and there is no broken string at the end since two groups can't be next to each other
        if (nums[0] <= len(cfg)) and ('.' not in cfg[:nums[0]]) and (nums[0] == len(cfg) or cfg[nums[0]] != '#'):
            total += count(cfg[nums[0] + 1:], nums[1:])

        return total

    total = 0
    for row in input:
        configs, nums = row.split()
        nums = tuple(map(int,nums.split(',')))
        
        #Unfold
        factor = 1 if part == 1 else 5
        
        configs = "?".join([configs] * factor)
        nums *= factor
                
        total += count(configs, nums)
                
    return total
    
print(f'Part 1: {solve(1)}')
print(f'Part 2: {solve(2)}')
    