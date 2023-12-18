input = open(0).read().strip().splitlines()

def get_vertices(part=1):
    starting_point = (int(0), int(0))
    vertices = [starting_point]
    path_length = 0
    
    for line in input:
        direction, distance, hex = line.split(' ')
        
        if part == 2:
            distance = int(hex[2:7], 16)
            direction = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}[int(hex[-2])]
        
        distance = int(distance)
        last_point = vertices[-1]
        path_length += distance
        
        if direction == 'R':
            vertices.append((last_point[0], last_point[1] + distance))
        elif direction == 'L':
            vertices.append((last_point[0], last_point[1] - distance))
        elif direction == 'D':
            vertices.append((last_point[0]  + distance, last_point[1]))
        elif direction == 'U':
            vertices.append((last_point[0] - distance, last_point[1]))

    return vertices, path_length

def shoelace(vertices):
    res = 0
    for i in range(0,len(vertices) - 1, 2):
        p1 = vertices[i]
        p2 = vertices[i + 1]
        res += p1[0] * p2[1] - p2[0] * p1[1]
    
    return abs(res)

vertices, path_length = get_vertices(1)
print(f'Part 1: {shoelace(vertices) + path_length//2 +1}')
vertices, path_length = get_vertices(2)
print(f'Part 2: {shoelace(vertices) + path_length//2 +1}')