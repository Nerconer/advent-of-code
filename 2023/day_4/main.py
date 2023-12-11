lines = open(0).read().strip().splitlines()

# Part 1
total_points = 0
# Part 2
card_list = [1] * len(lines)

for index, full_line in enumerate(lines):
    card_matches = 0
    winning_numbers, user_numbers = [k.split() for k in full_line.split(':')[1].strip().split(' | ')]
    
    for number in user_numbers:
        if number in winning_numbers:
            card_matches += 1
    
    for card_match in range(card_list[index]):
        for ii in range(card_matches):
            card_list[index+ ii + 1] +=1

    if card_matches == 0:
        continue
    total_points += 2 ** (card_matches - 1)
     
total_scratch_cards = sum(card_list)
    
print(f'Part 1: {total_points}')
print(f'Part 2: {total_scratch_cards}')