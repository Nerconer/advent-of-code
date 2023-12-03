def read_input_file(input_file: str):
    with open(input_file, 'r') as f:
        input_data = f.read().strip().splitlines()
    return input_data


def solve(input_file: str) -> tuple[int, int]:
    input_data = read_input_file(input_file)
        
    total_sum = 0
    total_gear_ratios = 0
    
    rows = len(input_data)
    cols = len(input_data[0])
    
    is_symbol = lambda x: x != '.' and not x.isdigit()
    
    for i in range(rows):
        for j in range(cols):
            element = input_data[i][j]
                        
            check_diagonal_top_left = True
            check_diagonal_top_right = True
            check_diagonal_bottom_left = True
            check_diagonal_bottom_right = True
            
            adjacents = []
            
            if is_symbol(element):                
                right_char = input_data[i][j+1]
                
                # Check if right char is a digit
                if right_char.isdigit():
                    number = input_data[i][j+1:].split('.')[0]
                    total_sum += int(number)
                    adjacents.append(int(number))
                    
                left_char = input_data[i][j-1]
                
                # Check if left char is a digit
                if left_char.isdigit():
                    number = input_data[i][:j].split('.')[-1]
                    total_sum += int(number)
                    adjacents.append(int(number))
                
                # Only check top if not first row 
                if i > 0:
                    # Check if top char is a digit
                    top_char = input_data[i-1][j]
                    # Check left
                    if top_char.isdigit():
                        right_side = input_data[i-1][j+1:].split('.')[0]
                        if right_side.isdigit():
                            check_diagonal_top_right = False
                            
                        left_char = input_data[i-1][:j+1].split('.')[-1]
                        if left_char.isdigit():
                            check_diagonal_top_left = False
                        number = int(left_char + right_side)
                        total_sum += number
                        adjacents.append(number)
                else:
                    check_diagonal_top_left = False
                    check_diagonal_top_right = False
                        
                #Only check bottom if not last row
                if i < rows - 1:
                    # Check if bottom char is a digit
                    bottom_char = input_data[i+1][j]
                    # Check left
                    if bottom_char.isdigit():
                        right_side = input_data[i+1][j+1:].split('.')[0]
                        if right_side.isdigit():
                            check_diagonal_bottom_right = False
                            
                        left_char = input_data[i+1][:j+1].split('.')[-1]
                        if left_char.isdigit():
                            check_diagonal_bottom_left = False
                        number = int(left_char + right_side)
                        total_sum += number
                        adjacents.append(number)
                else:
                    check_diagonal_bottom_left = False
                    check_diagonal_bottom_right = False
                    
                # Check diagonal top left
                if check_diagonal_top_left:
                    diagonal_top_left = input_data[i-1][j-1]
                    if diagonal_top_left.isdigit():
                        number = input_data[i-1][:j].split('.')[-1]
                        total_sum += int(number)
                        adjacents.append(int(number))
                        
                # Check diagonal top right
                if check_diagonal_top_right:
                    diagonal_top_right = input_data[i-1][j+1]
                    if diagonal_top_right.isdigit():
                        number = input_data[i-1][j+1:].split('.')[0]
                        total_sum += int(number)
                        adjacents.append(int(number))
                        
                # Check diagonal bottom left
                if check_diagonal_bottom_left:
                    diagonal_bottom_left = input_data[i+1][j-1]
                    if diagonal_bottom_left.isdigit():
                        number = input_data[i+1][:j].split('.')[-1]
                        total_sum += int(number)
                        adjacents.append(int(number))
                        
                # Check diagonal bottom right
                if check_diagonal_bottom_right:
                    diagonal_bottom_right = input_data[i+1][j+1]
                    if diagonal_bottom_right.isdigit():
                        number = input_data[i+1][j+1:].split('.')[0]
                        total_sum += int(number) 
                        adjacents.append(int(number))
                        
                if len(adjacents) == 2:
                    total_gear_ratios += adjacents[0] * adjacents[1]
        
    return total_sum, total_gear_ratios


if __name__ == '__main__':
    input_file = './input.txt'
    
    total_sum, total_gear_ratios = solve(input_file)
        
    print(f"{'='*10} Part 1 {'='*10}")
    print(total_sum)
    
    print(f"{'='*10} Part 2 {'='*10}")
    print(total_gear_ratios)