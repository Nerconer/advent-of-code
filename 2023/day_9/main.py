lines = open(0).read().strip().splitlines()

history = []
for lines in lines:
    history.append(list(map(int,lines.split())))
    
def part_one() -> int:
    final_list = []
    sequence = []
    for row in history:
        sequence.append(row)
        for row_two in sequence:
            tmp = []
            for sequence_row in range(1, len(row_two)):
                tmp.append(row_two[sequence_row] - row_two[sequence_row - 1])
            sequence.append(tmp)
            if all([x == 0 for x in tmp]):
                # Add a zero to the end of each row
                sequence[-1].append(0)
                for sequence_row_index in reversed(range(len(sequence) -1)):
                    sequence[sequence_row_index].append(sequence[sequence_row_index][-1] + sequence[sequence_row_index +1][-1])
                final_list.append(sequence[0])
                sequence = []
                break
        
    return sum(row[-1] for row in final_list)
        

def part_two() -> int:
    final_list = []
    sequence = []
    for row in history:
        sequence.append(row)
        for row_two in sequence:
            tmp = []
            for sequence_row_index in range(len(row_two) -1, 0, -1):
                tmp.insert(0,row_two[sequence_row_index] - row_two[sequence_row_index - 1])
            sequence.append(tmp)
            if all([x == 0 for x in tmp]):
                # Add a zero to the end of each row
                sequence[-1].append(0)
                for sequence_row_index in reversed(range(len(sequence) -1)):
                    sequence[sequence_row_index].insert(0,sequence[sequence_row_index][0] - sequence[sequence_row_index +1][0])
                final_list.append(sequence[0])
                sequence = []
                break
        
    return sum(row[0] for row in final_list)
    
print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')
    
