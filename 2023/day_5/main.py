# Aliases
# aos to check againt full input.txt file
# aot to check againt test.txt file

input = open(0).read()

def part_one():
    lines = input.strip().split('\n')
    
    seeds = list(map(int, lines[0].split(':')[1].split()))

    seed_to_soil_map = []
    soil_to_fertilizer_map = []
    fertalizer_to_water_map = []
    water_to_light_map = []
    light_to_temperature_map = []
    temperature_to_humidity_map = []
    humidity_to_location_map = []

    # Parse the input
    for index, line in enumerate(lines[1:]):

        if line.startswith('seed-to-soil'):
            for sub_line in lines[index+2:]:
                if sub_line:
                    seed_to_soil_map.append(tuple(map(int,sub_line.split())))
                else:
                    break
        elif line.startswith('soil-to-fertilizer'):
            for sub_line in lines[index+2:]:
                if sub_line:
                    soil_to_fertilizer_map.append(tuple(map(int,sub_line.split())))
                else:
                    break
        elif line.startswith('fertilizer-to-water'):
            for sub_line in lines[index+2:]:
                if sub_line:
                    fertalizer_to_water_map.append(tuple(map(int,sub_line.split())))
                else:
                    break
        elif line.startswith('water-to-light'):
            for sub_line in lines[index+2:]:
                if sub_line:
                    water_to_light_map.append(tuple(map(int,sub_line.split())))
                else:
                    break
        elif line.startswith('light-to-temperature'):
            for sub_line in lines[index+2:]:
                if sub_line:
                    light_to_temperature_map.append(tuple(map(int,sub_line.split())))
                else:
                    break
        elif line.startswith('temperature-to-humidity'):
            for sub_line in lines[index+2:]:
                if sub_line:
                    temperature_to_humidity_map.append(list(map(int,sub_line.split())))
                else:
                    break
        elif line.startswith('humidity-to-location'):
            for sub_line in lines[index+2:]:
                if sub_line:
                    humidity_to_location_map.append(tuple(map(int,sub_line.split())))
                else:
                    break

    min_location = None
    for seed in seeds:
        soil_value = 0
        for row in seed_to_soil_map:
            destination_range_start, source_range_start, range_length = row
            if source_range_start <= seed < source_range_start + range_length:
                soil_value = destination_range_start + (seed - source_range_start)
                break
        else:
            soil_value = seed
                
        fertilizer_value = 0
        for row in soil_to_fertilizer_map:
            destination_range_start, source_range_start, range_length = row
            if source_range_start <= soil_value < source_range_start + range_length:
                fertilizer_value = destination_range_start + (soil_value - source_range_start)
                break
        else:
            fertilizer_value = soil_value
            
        water_value = 0
        for row in fertalizer_to_water_map:
            destination_range_start, source_range_start, range_length = row
            if source_range_start <= fertilizer_value < source_range_start + range_length:
                water_value = destination_range_start + (fertilizer_value - source_range_start)
                break
        else:
            water_value = fertilizer_value
        
        light_value = 0
        for row in water_to_light_map:
            destination_range_start, source_range_start, range_length = row
            if source_range_start <= water_value < source_range_start + range_length:
                light_value = destination_range_start + (water_value - source_range_start)
                break
        else:
            light_value = water_value
        
        temperature_value = 0
        for row in light_to_temperature_map:
            destination_range_start, source_range_start, range_length = row
            if source_range_start <= light_value < source_range_start + range_length:
                temperature_value = destination_range_start + (light_value - source_range_start)
                break
        else:
            temperature_value = light_value
        
        humidity_value = 0
        for row in temperature_to_humidity_map:
            destination_range_start, source_range_start, range_length = row
            if source_range_start <= temperature_value < source_range_start + range_length:
                humidity_value = destination_range_start + (temperature_value - source_range_start)
                break
        else:
            humidity_value = temperature_value
        
        location_value = 0
        for row in humidity_to_location_map:
            destination_range_start, source_range_start, range_length = row
            if source_range_start <= humidity_value < source_range_start + range_length:
                location_value = destination_range_start + (humidity_value - source_range_start)
                break
        else:
            location_value = humidity_value
                
        min_location =  location_value if min_location is None else min(min_location, location_value)
        
    return min_location
        

def part_two():
    inputs, *blocks = input.split('\n\n')
    inputs = list(map(int, inputs.split(':')[1].split()))
    
    seeds_new = []
    
    for i in range(0, len(inputs), 2):
        seeds_new.append((inputs[i], inputs[i] + inputs[i+1]))    
    
    for block in blocks:
        final_blocks = []
        for line in block.splitlines()[1:]:
            final_blocks.append(list(map(int, line.split())))
        
        new = []  
        while len(seeds_new):
            start, end = seeds_new.pop(0)
            for dest_range_start, source_range_start, range_length in final_blocks:
                overlapping_start = max(start, source_range_start)
                overlapping_end = min(end, source_range_start + range_length)
                if overlapping_start < overlapping_end:
                    new.append((overlapping_start - source_range_start + dest_range_start, overlapping_end - source_range_start + dest_range_start))
                    if overlapping_start > start:
                        seeds_new.append((start, overlapping_start))
                    if overlapping_end < end:
                        seeds_new.append((overlapping_end, end))
                    break
            else:
                new.append((start, end))

        seeds_new = new
    
    return min(seeds_new)[0]

print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')