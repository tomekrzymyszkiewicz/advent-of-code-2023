from itertools import combinations

with open("input.txt", "r") as f:
    lines = [line.split() for line in f.read().strip().splitlines()]
    springs_list = [
        [chars, list(map(int, numbers.split(",")))] for chars, numbers in lines
    ]


def is_arrangement_possible(
    arrangement: tuple, springs_string: str, damaged_lengths: list[int]
) -> bool:
    hash_count = 0

    for i, (arr_pos, segment_len) in enumerate(zip(arrangement, damaged_lengths)):
        if i < len(arrangement) - 1 and arr_pos + segment_len >= arrangement[i + 1]:
            return False
        elif i == len(arrangement) - 1 and arr_pos + segment_len > len(springs_string):
            return False
        for char in springs_string[arr_pos : arr_pos + segment_len]:
            if not char in "?#":
                return False
            if char == "#":
                hash_count += 1
    if hash_count < springs_string.count("#"):
        return False
    return True


def count_arrangements(springs: list) -> int:
    springs_string, damaged_lengths = springs
    possible_start_positions = list(
        combinations(
            range(len(springs_string) - damaged_lengths[-1] + 2), len(damaged_lengths)
        )
    )
    count = 0
    for arrangement in possible_start_positions:
        if is_arrangement_possible(arrangement, springs_string, damaged_lengths):
            count += 1
    return count


print(sum([count_arrangements(springs) for springs in springs_list]))
