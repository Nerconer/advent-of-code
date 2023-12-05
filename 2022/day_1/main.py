input = open(0).read().split('\n\n')

data = []
for line in input:
    data.append(list(map(int,line.split('\n'))))
    
total_calories = []
for calories_list in data:
    total_calories.append(sum(calories_list))

sorted_calories = sorted(total_calories)

top_three_calories = sum(sorted_calories[-3:])

print(f'Part 1: {max(total_calories)}')
print(f'Part 2: {top_three_calories}')

