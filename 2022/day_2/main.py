# Opponent
# A -> Rock
# B -> Paper
# C -> Scissors

# You (Part 1)
# X -> Rock
# Y -> Paper
# Z -> Scissors

# You (Part 2)
# X -> Need to lose
# Y -> Need to draw
# Z -> Need to win

shape_points_list = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

games = open(0).read().splitlines()

def part_one():
    points = 0
    for game in games:
        opponent, you = game.split()
        round_shape_points = shape_points_list[you]
        game_points = 0
        if you == 'X': # Rock
            if opponent == 'A': # Rock
                game_points = 3 # Draw
            elif opponent == 'B': # Paper
                game_points = 0 # Lose
            elif opponent == 'C': # Scissors
                game_points = 6 # Win
        elif you == 'Y': # Paper
            if opponent == 'A': # Rock
                game_points = 6 # Win
            elif opponent == 'B': # Paper
                game_points = 3 # Draw
            elif opponent == 'C': # Scissors
                game_points = 0 # Lose
        elif you == 'Z': # Scissors
            if opponent == 'A': # Rock
                game_points = 0 # Lose
            elif opponent == 'B': # Paper
                game_points = 6 # Win
            elif opponent == 'C': # Scissors
                game_points = 3 # Draw

        points += (game_points + round_shape_points)
    
    return points


def part_two():
    points = 0
    for game in games:
        opponent, you = game.split()
        game_points = 0
        shape_points = 0
        if opponent == 'A': # Rock
            if you == 'X': # Need to lose
                game_points = 0
                shape_points = shape_points_list['Z']
            elif you == 'Y': # Need to draw
                game_points = 3
                shape_points = shape_points_list['X']
            elif you == 'Z': # Need to win
                game_points = 6
                shape_points = shape_points_list['Y']
        elif opponent == 'B': # Paper
            if you == 'X': # Need to lose
                game_points = 0
                shape_points = shape_points_list['X']
            elif you == 'Y': # Need to draw
                game_points = 3
                shape_points = shape_points_list['Y']
            elif you == 'Z': # Need to win
                game_points = 6
                shape_points = shape_points_list['Z']
        elif opponent == 'C': # Scissors
            if you == 'X': # Need to lose
                game_points = 0
                shape_points = shape_points_list['Y']
            elif you == 'Y': # Need to draw
                game_points = 3
                shape_points = shape_points_list['Z']
            elif you == 'Z': # Need to win
                game_points = 6
                shape_points = shape_points_list['X']
                
        points += (game_points + shape_points)
        
    return points
                
print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')
        

