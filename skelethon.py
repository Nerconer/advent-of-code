def read_input_file(input_file: str):
    with open(input_file, 'r') as f:
        input_data = f.read().strip().splitlines()
    return input_data

def part_one(input_file: str):
    pass

def part_two(input_file: str):
    pass


if __name__ == '__main__':
    input_file = './input.txt'
    input_file = './sample.txt'
    
    print(f"{'='*40} Part 1 {'='*40}")
    print(part_one(input_file))
    
    print(f"{'='*40} Part 2 {'='*40}")
    print(part_two(input_file))
