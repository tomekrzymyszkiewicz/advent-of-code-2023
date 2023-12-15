import re

with open("input.txt", "r") as f:
    input = f.read().strip().split(",")

label_pattern = re.compile(r"^[a-zA-Z]+")


def aoc_hash(string: str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


def get_focusing_power(instructions: list[str]) -> int:
    boxes = {}
    for inst in instructions:
        label = label_pattern.match(inst).group(0)
        box_id = aoc_hash(label)
        if box_id in boxes:
            if "-" in inst and label in boxes.get(box_id):
                boxes[box_id].pop(label)
            elif "=" in inst:
                boxes[box_id][label] = int("".join(filter(lambda i: i.isdigit(), inst)))
        elif "=" in inst:
            boxes[box_id] = {label: int("".join(filter(lambda i: i.isdigit(), inst)))}
    boxes_sum = 0
    for box_id, lenses in boxes.items():
        box_sum = 0
        for i, lens in enumerate(lenses.values()):
            box_sum += (box_id + 1) * (i + 1) * lens
        boxes_sum += box_sum
    return boxes_sum


print(get_focusing_power(input))
