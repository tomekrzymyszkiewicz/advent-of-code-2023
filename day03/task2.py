import string

with open("input.txt", "r") as f:
    lines = f.read().split("\n")


def is_gear(char: str) -> bool:
    return char == "*"


def get_whole_part_number(x: int, y: int) -> int:
    part_number_start_index = y
    part_number_end_index = y
    while (
        part_number_start_index > 0 and lines[x][part_number_start_index - 1].isdigit()
    ):
        part_number_start_index -= 1
    while (
        part_number_end_index < len(lines[0]) - 1
        and lines[x][part_number_end_index + 1].isdigit()
    ):
        part_number_end_index += 1
    return int(lines[x][part_number_start_index : part_number_end_index + 1]), range(
        part_number_start_index, part_number_end_index + 2
    )


def part_numbers(part_x: int, part_y: int) -> [int]:
    part_numbers = []
    numbers_scanned = {i: [] for i in range(part_x - 1, part_x + 2)}
    for x in range(part_x - 1, part_x + 2):
        for y in range(part_y - 1, part_y + 2):
            if lines[x][y].isdigit() and y not in numbers_scanned[x]:
                number, y_index_range = get_whole_part_number(x, y)
                numbers_scanned[x].extend(y_index_range)
                part_numbers.append(number)
    return part_numbers


part_numbers_sum = 0
for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if is_gear(char):
            part_numbers_list = part_numbers(x, y)
            if len(part_numbers_list) == 2:
                part_numbers_sum += part_numbers_list[0] * part_numbers_list[1]

print(part_numbers_sum)
