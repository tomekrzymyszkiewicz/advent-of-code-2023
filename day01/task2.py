import re

with open("input.txt", "r") as f:
    lines = f.readlines()


def find_digit(pattern: re.Pattern, numbers_dict: dict, string: str) -> int:
    digit = pattern.search(string).group()
    return int(numbers_dict.get(digit, digit))


numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}
numbers_reversed = {k[::-1]: v for k, v in numbers.items()}

matching_words = [*map(str, numbers.values()), *numbers.keys()]
matching_words_reverse = [word[::-1] for word in matching_words]

pattern = re.compile(r"|".join(map(re.escape, matching_words)))
pattern_reversed = re.compile(r"|".join(map(re.escape, matching_words_reverse)))

number = sum(
    [
        find_digit(pattern, numbers, line) * 10
        + find_digit(pattern_reversed, numbers_reversed, line[::-1])
        for line in lines
    ]
)
print(number)
