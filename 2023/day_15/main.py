sequence = open(0).read().strip().split(',')

def hash(text):
    total = 0
    for char in text:
        total = ((ord(char) + total) * 17) % 256
    return total

def part_one() -> int:
    return sum(hash(step) for step in sequence)

def part_two() -> int:
    boxes = {}
    for step in sequence:
        label, operation = (step.split('-')[0], '-') if '-' in step else (step.split('=')[0], '=')
                
        if operation == '=':
            focal = step[-1:]
            label_and_focal = f'{label} {focal}'
            if hash(label) not in boxes:
                boxes[hash(label)] = [label_and_focal]
            # Label already exists in the box
            else:
                if any(elem.startswith(label) for elem in boxes[hash(label)]):
                    boxes[hash(label)] = [label_and_focal if elem.startswith(label) else elem for elem in boxes[hash(label)]]
                else:
                    boxes[hash(label)].append(label_and_focal)
                    
        elif operation == '-':
            if hash(label) in boxes:
                boxes[hash(label)] = [elem for elem in boxes[hash(label)] if not elem.startswith(label)]
 
    return sum((int(box) + 1) * i * int(elem[-1:]) for box in boxes for i, elem in enumerate(boxes[box], 1))

print(f'Part 1: {part_one()}')
print(f'Part 2: {part_two()}')