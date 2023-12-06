import datetime

input = open(0).read().splitlines()

def part_one() -> int:
    times = input[0].split(':')[1]
    distances = (input[1].split(':')[1])

    times = list(map(int, times.split()))
    distances = list(map(int, distances.split()))

    total_result = 1

    for num_race in range(len(times)):
        num_ways = 0
        for i in range (1, times[num_race]):
            current_speed = i
            time_left = times[num_race] - i
            distance = current_speed * time_left
            if (distance > distances[num_race]):
                num_ways += 1
        total_result *= num_ways
    return total_result
        
def part_two():
    times = input[0].split(':')[1]
    distances = (input[1].split(':')[1])
    
    times = times.split()
    distances = distances.split()
    
    total_time = int(''.join(times))
    total_distance = int(''.join(distances))
    
    total_combinations = 0
    
    # Only need to check half of the total time since the other half is just a mirror
    for i in range(1, (total_time//2)):
        current_speed = i
        time_left = total_time - i
        
        distance = current_speed * time_left
        
        if (distance > total_distance):
                total_combinations += 1
    
    total_combinations *= 2
    
    return total_combinations + 1
    
part_one_start = datetime.datetime.now()
print(f'Part 1: {part_one()}')
part_one_end = datetime.datetime.now()
print(f'Part 1 execution time: {(part_one_end - part_one_start).total_seconds() * 1000} ms\n')

print(f'Part 2: {part_two()}')
part_two_end = datetime.datetime.now()
print(f'Part 2 execution time: {(part_two_end - part_one_end).total_seconds() * 1000} ms')
        