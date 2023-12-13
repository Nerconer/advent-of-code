input = open(0).read().strip().split('\n\n')

valleys = []

for valley in input:
    valley = valley.splitlines()
    valleys.append(valley)

def reflections(valley, target_diff):
    w = len(valley[0])
    h = len(valley)

    # Horizontal reflections
    for row in range(h):
        diff = 0
        for i in range(h):
            if row - i < 0 or row + i + 1 >= h:
                break
            for j in range(w):
                if valley[row - i][j] != valley[row + i + 1][j]:
                    diff += 1
        if diff == target_diff and (row + 1 < h):
            return (row + 1) * 100
    
    # Vertical reflections
    for col in range(w):
        diff = 0
        for i in range(w):
            if col - i < 0 or col + i + 1 >= w:
                break
            for j in range(h):
                if valley[j][col - i] != valley[j][col + i + 1]:
                    diff += 1
        if diff == target_diff:
            return col + 1
        
    return 0
    
part1, part2 = 0, 0
for valley in valleys:
    part1 += reflections(valley, target_diff=0)
    part2 += reflections(valley, target_diff=1)
    
print(f'Part 1: {part1}')
print(f'Part 2: {part2}')
    
    
    