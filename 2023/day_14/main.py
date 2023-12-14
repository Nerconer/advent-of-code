
grid = tuple(open(0).read().strip().splitlines())

def part_one() -> int:
    global grid
    new_grid = tuple(map("".join, zip(*grid)))
    new_grid = tuple("#".join(["".join(sorted(list(x), reverse=True)) for x in row.split("#")]) for row in new_grid)
    # Reverse the grid back to its original orientation
    new_grid = tuple(map("".join, zip(*new_grid)))
    return sum(row.count("O") * (len(row)-i) for i, row in enumerate(new_grid))

def part_two() -> int:
    def cycle():
        global grid
        for _ in range(4): # 4 rotations: N, W, S, E
            grid = tuple(map("".join, zip(*grid)))
            grid = tuple("#".join(["".join(sorted(list(x), reverse=True)) for x in row.split("#")]) for row in grid)
            grid = tuple(row[::-1] for row in grid)
    
    seen = set(grid)
    grid_list = [grid]
    index = 0
    
    while True:
        index += 1
        cycle()
        if grid in seen:
            break
        seen.add(grid)
        grid_list.append(grid)
    
    first = grid_list.index(grid)

    res = grid_list[(1_000_000_000 - first) % (index - first) + first]
    return sum(row.count("O") * (len(row)-i) for i, row in enumerate(res))

print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')


    
