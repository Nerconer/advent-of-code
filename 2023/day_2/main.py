from math import prod

def read_input_file(input_file: str):
    with open(input_file, 'r') as f:
        input_data = f.read().splitlines()
    return input_data

def part_one(input_file: str) -> int:
    input_data = read_input_file(input_file)
    
    cubes_limit = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    
    sum_ids = 0
    
    for game in input_data:

        game_id = game.split(':')[0].replace('Game ', '')
        game = game.split(':')[1].strip()
        game_sets = game.split(';')
        
        valid_set = True
        
        for game_set in game_sets:            
            cubes = game_set.split(', ')     
            valid_throw = True
            for cube in cubes:
                cube = cube.strip()
                cube_number = int(cube.split(' ')[0].strip())
                cube_color = cube.split(' ')[1]
                                
                if cube_number > cubes_limit[cube_color]:
                    valid_throw = False
                    break
                
            if not valid_throw:
                valid_set = False
                break
        
        if valid_set:
            sum_ids += int(game_id)
    
    return sum_ids


def part_two(input_file: str) -> int:
    input_data = read_input_file(input_file)
    
    total_sum = 0
    
    for game in input_data:

        game_id = game.split(':')[0].replace('Game ', '')
        game = game.split(':')[1].strip()
        game_sets = game.split(';')
        
        biggest_cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        
        for game_set in game_sets:
            cubes = game_set.split(', ')

            for cube in cubes:
                cube = cube.strip()
                cube_number = int(cube.split(' ')[0].strip())
                cube_color = cube.split(' ')[1]
                
                if cube_number > biggest_cubes[cube_color]:
                    biggest_cubes[cube_color] = cube_number
                                    
        total_sum += prod(biggest_cubes.values())
        
    return total_sum



if __name__ == '__main__':
    input_file = './input.txt'
    
    print(f"{'='*10} Part 1 {'='*10}")
    print(part_one(input_file))
    
    print(f"{'='*10} Part 2 {'='*10}")
    print(part_two(input_file))