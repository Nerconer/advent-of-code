from math import lcm
from collections import deque

input = open(0).read().strip().splitlines()

class Module:
    def __init__(self, name, type, outputs):
        self.name: str = name
        self.type: str = type
        self.outputs: list[str] = outputs
        
        if type == '%':
            self.memory = "off"
        else:
            self.memory = {}
    
    def __repr__(self):
        return f"Module(name={self.name}, type={self.type}, outputs={','.join(self.outputs)}, memory={self.memory})"



def solve(part=1):
    modules: dict[str, Module] = {}
    broadcaster_targets = []

    for line in input:
        module, outputs = line.split(' -> ')
        outputs = outputs.split(', ')
        if module == 'broadcaster':
            broadcaster_targets = outputs
        else:
            type = module[0] # &, %
            module_name = module[1:]
            modules[module_name] = Module(module_name, type, outputs)

    for name, module in modules.items():
        for output in module.outputs:
            if output in modules and modules[output].type == '&':
                modules[output].memory[name] = "low"
            
    count_low_pulses = 0
    count_high_pulses = 0

    # (Part 2) Find the penultimate module, the last one is 'rx'
    (penultimate_module,) = [name for name, module in modules.items() if 'rx' in module.outputs]

    # (Part 2) Find all modules that are connected to the penultimate module
    # Penultimate module will send a single low pulse when all of these modules are on
    cycle_lengths = {}
    seen = { name: 0 for name, module in modules.items() if penultimate_module in module.outputs }

    button_presses = 0
    while True:
        button_presses += 1
        
        if part == 1 and button_presses > 1000:
            return count_low_pulses * count_high_pulses
        
        count_low_pulses += 1 # Each time we pulse the button, it sends a low pulse
        queue = deque([('broadcaster', x, 'low') for x in broadcaster_targets])
        
        while queue:
            origin, target, pulse = queue.popleft()
            
            if pulse == "low":
                count_low_pulses += 1
            else:
                count_high_pulses += 1
                
            if target not in modules:
                continue
        
            target_module: Module = modules[target]
            
            if target_module.name == penultimate_module and pulse == "high":
                seen[origin] += 1
                
                if origin not in cycle_lengths:
                    cycle_lengths[origin] = button_presses
                else:
                    assert button_presses == cycle_lengths[origin] * seen[origin]
                
                if all(seen.values()):
                    return lcm(*cycle_lengths.values())
            
            # Flip-flop module
            if target_module.type == "%":
                if pulse == "low":
                    # Toggle the memory
                    target_module.memory = "on" if target_module.memory == "off" else "off"
                    outgoing_pulse = "high" if target_module.memory == "on" else "low"
                    # Send a pulse to all outputs
                    for output in target_module.outputs:
                        queue.append((target_module.name, output, outgoing_pulse))
                        
            # Conjunction module
            elif target_module.type == "&":
                target_module.memory[origin] = pulse
                outgoing_pulse = "low" if all(value == "high" for value in target_module.memory.values()) else "high"
                for output in target_module.outputs:
                    queue.append((target_module.name, output, outgoing_pulse))
               
print(f"Part 1: {solve(part=1)}")
print(f"Part 2: {solve(part=2)}")