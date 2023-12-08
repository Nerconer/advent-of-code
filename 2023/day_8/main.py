import re
import sys
from math import lcm

sys.setrecursionlimit(50000)
    
def part_one(nodes_raw: list[str], instructions: str) -> None:
    def find_node_recursive(current_node_id: str, target_node: str, nodes: dict, steps: int, instructions: str, instruction_index: int):
        if current_node_id == target_node:
            return steps
                
        if instruction_index == len(instructions):
            instruction_index = 0        
            
        current_instruction = instructions[instruction_index]
            
        if current_instruction == 'L':
            return find_node_recursive(nodes[current_node_id][0], target_node, nodes, steps+1, instructions, instruction_index+1)
        elif current_instruction == 'R':
            return find_node_recursive(nodes[current_node_id][1], target_node, nodes, steps+1, instructions, instruction_index+1)
        
    def find_node_iterative(current_node_id: str, target_node: str, nodes: dict, instructions: str):
        steps = 0
        instruction_index = 0
        while True:
            steps += 1
            if instruction_index == len(instructions):
                instruction_index = 0
            
            current_instruction = instructions[instruction_index]
            
            if current_instruction == 'L':
                current_node_id = nodes[current_node_id][0]
            elif current_instruction == 'R':
                current_node_id = nodes[current_node_id][1]
                            
            if current_node_id == target_node:
                return steps
            
            instruction_index += 1  
    
    nodes = {}
    for node in nodes_raw:
        parent, left, right = re.findall("([A-Z]{3})", node)
        nodes[parent] = [left, right]  
    
    initial_node = 'AAA'
    target_node = 'ZZZ'

    steps = 0
    steps = find_node_recursive(initial_node, target_node, nodes, steps, instructions, 0)
    print(f"Part 1 recursive: {steps}")

    steps = find_node_iterative(initial_node, target_node, nodes, instructions)
    print(f"Part 1 iterative: {steps}")
    
def part_two(nodes_raw: list[str], instructions: str) -> None:
    def find_node(current_node_id: str, target_node: str, nodes: dict, instructions: str) -> int:
        steps = 0
        instruction_index = 0
        while True:
            steps += 1
            if instruction_index == len(instructions):
                instruction_index = 0
            
            current_instruction = instructions[instruction_index]
            instruction_index += 1  
            
            if current_instruction == 'L':
                current_node_id = nodes[current_node_id][0]
            elif current_instruction == 'R':
                current_node_id = nodes[current_node_id][1]
                            
            if current_node_id.endswith(target_node):
                return steps       
    
    nodes = {}
    for node in nodes_raw:
        parent, left, right = re.findall("([A-Z1-9]{3})", node)
        nodes[parent] = [left, right]
        
    # Return a list of all nodes that end with 'A'
    node_list = [node for node in list(nodes.keys()) if node.endswith('A') ]
        
    step_list = []
    for node in node_list:
        step_list.append(find_node(node, 'Z', nodes, instructions))

    print(f'Part 2: {lcm(*step_list)}')
        
    
lines = open(0).read().strip().splitlines()

instructions = lines[0]
nodes_raw = lines[2:]
       
part_one(nodes_raw, instructions)
part_two(nodes_raw, instructions)

    


