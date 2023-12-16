grid = open(0).read().strip().splitlines()

def get_num_energized_tiles(beam_start: tuple):
    beams = {beam_start}
    energized_tiles = {(beam_start[0], beam_start[1])}
    history = {beam_start}

    while beams:
        beam = beams.pop()
        i, j, from_direction = beam
                
        # If the beam is out of bounds, ignore it
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]):
            continue
        
        # If a previous beam has already been here with the same direction, ignore it
        if beam in history and len(history) > 1:
            continue
        
        history.add(beam)
        energized_tiles.add((i, j))
        
        ch = grid[i][j]
        
        # Check horizontal and vertical shared cases first
        if (ch == '|') and (from_direction == 'Right' or from_direction == 'Left'):
            beams.add((i - 1, j, 'Up'))
            beams.add((i + 1, j, 'Down'))
        elif (ch == '-') and (from_direction == 'Up' or from_direction == 'Down'):
            beams.add((i, j - 1, 'Left'))
            beams.add((i, j + 1, 'Right'))
        
        elif from_direction == 'Right':
            if ch == '/':
                beams.add((i - 1, j, 'Up'))
            elif ch == '\\':
                beams.add((i + 1, j, 'Down'))
            elif ch == '.' or ch == '-':
                beams.add((i, j + 1, 'Right'))
        elif from_direction == 'Left':
            if ch == '/':
                beams.add((i + 1, j, 'Down'))
            elif ch == '\\':
                beams.add((i - 1, j, 'Up'))
            elif ch == '.' or ch == '-':
                beams.add((i, j - 1, 'Left'))
        elif from_direction == 'Up':
            if ch == '/':
                beams.add((i, j + 1, 'Right'))
            elif ch == '\\':
                beams.add((i, j - 1, 'Left'))
            elif ch == '.' or ch == '|':
                beams.add((i - 1, j, 'Up'))
        elif from_direction == 'Down':
            if ch == '/':
                beams.add((i, j - 1, 'Left'))
            elif ch == '\\':
                beams.add((i, j + 1, 'Right'))
            elif ch == '.' or ch == '|':
                beams.add((i + 1, j, 'Down'))
        
    return len(energized_tiles)

def part_one() -> int:
    return get_num_energized_tiles(beam_start=(0, 0, 'Right'))  

def part_two() -> int:
    max_value = 0
    # Generate beams from the top row going downwards
    for j in range(len(grid[0])):
        max_value = max(max_value, get_num_energized_tiles(beam_start=(0, j, 'Down')))
    
    # Generate beams from the bottom row going upwards
    for j in range(len(grid[-1])):
        max_value = max(max_value, get_num_energized_tiles(beam_start=(len(grid) - 1, j, 'Up')))
    
    # Generate beams from the leftmost column going rightwards
    for i in range(len(grid)):
        max_value = max(max_value, get_num_energized_tiles(beam_start=(i, 0, 'Right')))
    
    # Generate beams from the rightmost column going leftwards
    for i in range(len(grid)):
        max_value = max(max_value, get_num_energized_tiles(beam_start=(i, len(grid[i]) - 1, 'Left')))

    return max_value
   
print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')