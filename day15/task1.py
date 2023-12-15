with open("input.txt", "r") as f:
    input = f.read().strip().split(",")


def aoc_hash(string: str) -> int:
    current_value = 0
    for char in string:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    return current_value


print(sum(aoc_hash(string) for string in input))
