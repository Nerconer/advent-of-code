def read_input_file(input_file: str)->list[str]:
    with open(input_file, 'r') as f:
        input_data = f.read().splitlines()
    return input_data

def part_one(input_file: str)-> int:
    input_data = read_input_file(input_file)
    
    total_sum = 0
    
    for line in input_data:
        first_digit = ""
        last_digit = ""
        
        for index in range(len(line)):
            left_cursor = line[index]
            right_cursor = line[-index-1]
            
            if not first_digit and left_cursor.isdigit():
                first_digit = left_cursor
            if not last_digit and right_cursor.isdigit():
                last_digit = right_cursor
        
        if not first_digit:
            first_digit = last_digit
        elif not last_digit:
            last_digit = first_digit
    
        total_sum += int(first_digit + last_digit)  
    
    return total_sum

def part_two(input_file: str)-> int:
    input_data = read_input_file(input_file)
    
    total_sum = 0
    
    numbers = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    
    for line in input_data:
        first_digit = ""
        last_digit = ""
        
        for index in range(len(line)):
            left_cursor = line[index]
            right_cursor = line[-index-1]
            
            if not first_digit and left_cursor.isdigit():
                first_digit = left_cursor
                
            if not last_digit and right_cursor.isdigit():
                last_digit = right_cursor
                
            for key in numbers.keys():
                if not first_digit and line[index:].startswith(key):
                    first_digit = numbers[key]

                if index == 0:
                    if not last_digit and line.endswith(key):
                        last_digit = numbers[key]
                        
                if not last_digit and line[:-index].endswith(key):
                    last_digit = numbers[key]
            
            # Break if both digits are found    
            if first_digit and last_digit:
                break
        
        if not first_digit:
            first_digit = last_digit
            
        elif not last_digit:
            last_digit = first_digit
                
        number = int(first_digit + last_digit)
        total_sum += number
    
    return total_sum


if __name__ == '__main__':
    input_file = './input.txt'
    
    print(f"{'='*10} Part 1 {'='*10}")
    print(part_one(input_file))
    
    print(f"{'='*10} Part 2 {'='*10}")
    print(part_two(input_file))