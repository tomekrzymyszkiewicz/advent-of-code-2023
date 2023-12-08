import re

with open("input.txt", "r") as f:
    input = re.sub(r" |=|\(|\)|,", "", f.read()).splitlines()
instructions = input[0]
map_rules = {i[:3]: {"L": i[3:6], "R": i[6:9]} for i in input[2:]}

current_node = "AAA"
move_counter = 0
while current_node != "ZZZ":
    current_instruction = instructions[move_counter % len(instructions)]
    current_node = map_rules.get(current_node).get(current_instruction)
    move_counter += 1

print(move_counter)
