import re
from math import lcm

with open("input.txt", "r") as f:
    input = re.sub(r" |=|\(|\)|,", "", f.read()).splitlines()
instructions = input[0]
map_rules = {i[:3]: {"L": i[3:6], "R": i[6:9]} for i in input[2:]}

start_nodes = [k for k in map_rules.keys() if k.endswith("A")]
paths_lengths = []
for start_node in start_nodes:
    current_node = start_node
    move_counter = 0
    while not current_node.endswith("Z"):
        current_instruction = instructions[move_counter % len(instructions)]
        current_node = map_rules.get(current_node).get(current_instruction)
        move_counter += 1
    paths_lengths.append(move_counter)
print(lcm(*paths_lengths))
