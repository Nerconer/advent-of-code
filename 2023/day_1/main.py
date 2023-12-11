input_data = open(0).read().strip().splitlines()

def part_one()-> int:
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

def part_two()-> int:
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
    print(f'Part 1: {part_one()}')
    print(f'Part 2: {part_two()}')