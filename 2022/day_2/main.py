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

games = open(0).read().splitlines()

def part_one():
    points = 0
    for game in games:
        opponent, you = game.split()
        if you == 'X': # Rock
            points += 1
            if opponent == 'A': # Rock
                points += 3 # Draw
            elif opponent == 'C': # Scissors
                points += 6 # Win
        elif you == 'Y': # Paper
            points += 2
            if opponent == 'A': # Rock
                points += 6 # Win
            elif opponent == 'B': # Paper
                points += 3 # Draw
        elif you == 'Z': # Scissors
            points += 3
            if opponent == 'B': # Paper
                points += 6 # Win
            elif opponent == 'C': # Scissors
                points += 3 # Draw
        
    return points


def part_two():
    points = 0
    for game in games:
        opponent, you = game.split()
        if opponent == 'A': # Rock
            if you == 'X': # Need to lose
                points += 0 + 3
            elif you == 'Y': # Need to draw
                points += 3 + 1
            elif you == 'Z': # Need to win
                points += 6 + 2
        elif opponent == 'B': # Paper
            if you == 'X': # Need to lose
                points += 0 + 1
            elif you == 'Y': # Need to draw
                points += 3 + 2
            elif you == 'Z': # Need to win
                points += 6 + 3
        elif opponent == 'C': # Scissors
            if you == 'X': # Need to lose
                points += 0 + 2
            elif you == 'Y': # Need to draw
                points += 3 + 3
            elif you == 'Z': # Need to win
                points += 6 + 1
        
    return points
                
print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')
        

