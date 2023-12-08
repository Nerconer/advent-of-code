lines = open(0).read().splitlines()

def solve(is_part_one: bool = False):
    def get_hand_strength(hand: str) -> int:
        hand_dict: dict = { card: hand.count(card) for card in hand }
        values = sorted(hand_dict.values(), reverse=True)   
        max_tuple = max(hand_dict.items(), key=lambda item: item[1])
 
        if not is_part_one:
            values[0] = max_tuple[1] + values[1] if max_tuple[0] == 'J' and len(values) > 1 else values[0] + hand.count('J')
      
        match values[0]:
            case 1:
                return 0
            case 2:
                return 1 if values[1] == 1 else 2
            case 3:
                return 3 if values[1] == 1 else 4
            case 4:
                return 5
            case _:
                return 6
    
    plays = []

    for line in lines:
        hand, bid = line.split()
        hand_strength: int = get_hand_strength(hand)    
        plays.append((hand_strength, hand, int(bid)))
        
    letter_map = { 'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E' } if is_part_one else { 'J': '.', 'T': 'B', 'Q': 'C', 'K': 'D', 'A': 'E' }
    plays.sort(key=lambda x: (x[0], [letter_map.get(card, card) for card in x[1]]))
    total_winnings = sum(rank * bid for rank, (*_, bid) in enumerate(plays, 1))
    return total_winnings
    
    
print(f'Part 1: {solve(True)}')
print(f'Part 2: {solve(False)}')
