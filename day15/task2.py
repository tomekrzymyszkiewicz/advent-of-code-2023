import re

with open("input.txt", "r") as f:
    input = f.read().strip().split(",")

label_pattern = re.compile(r"^[a-zA-Z]+")


def aoc_hash(string: str) -> int:
    current_value = 0
    for char in string:
        current_value = ((current_value + ord(char)) * 17) % 256
    return current_value


def get_focusing_power(instructions: list[str]) -> int:
    boxes = {i: {} for i in range(256)}
    for inst in instructions:
        label = label_pattern.match(inst).group(0)
        box_id = aoc_hash(label)
        if "=" in inst:
            boxes[box_id][label] = int("".join(filter(lambda i: i.isdigit(), inst)))
        if "-" in inst and label in boxes.get(box_id):
            boxes[box_id].pop(label)
    return sum(
        sum((box_id + 1) * (i + 1) * lens for i, lens in enumerate(lenses.values()))
        for box_id, lenses in boxes.items()
    )


print(get_focusing_power(input))
