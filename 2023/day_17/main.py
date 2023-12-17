from heapq import heappop, heappush
grid = [list(map(int, line.strip())) for line in open(0)]

def solve(part=1):
    seen = set()
    priority_queue = [(0, 0, 0, 0, 0, 0)] # (heat_loss, i, j, direction i, direction j, steps)

    while priority_queue:
        hl, i, j, di, dj, steps = heappop(priority_queue)
        
        #If we are at the bottom right corner, print the heat loss and break
        if (i, j) == (len(grid) - 1, len(grid[0]) - 1):
            return hl
        
        # If already seen, ignore. Don't need to check heap loss because it will increase in a loop
        if (i, j, di, dj, steps) in seen:
            continue
        
        seen.add((i, j, di, dj, steps))
        
        max_consecutive_steps = 3 if part == 1 else 10
        
        # If did not reach max consecutive steps in the same direction and not standing on the starting point, add to heap
        if steps < max_consecutive_steps and (di, dj) != (0, 0):
            # Continue in the same direction
            next_i = i + di
            next_j = j + dj
            # If next position is out of bounds, ignore it
            if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                heappush(priority_queue, (hl + grid[next_i][next_j], next_i, next_j, di, dj, steps + 1))
        
        if (steps >= 4 or (di, dj) == (0, 0)) or part == 1:
            # Try all 4 directions
            for next_di, next_dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (next_di, next_dj) != (di, dj) and (next_di, next_dj) != (-di, -dj):
                    next_i = i + next_di
                    next_j = j + next_dj
                    # If next position is out of bounds, ignore it
                    if 0 <= next_i < len(grid) and 0 <= next_j < len(grid[0]):
                        # Set steps to 1 because we are changing direction
                        heappush(priority_queue, (hl + grid[next_i][next_j], next_i, next_j, next_di, next_dj, 1))
                    
print(f'Part 1: {solve(1)}')
print(f'Part 2: {solve(2)}')
    
