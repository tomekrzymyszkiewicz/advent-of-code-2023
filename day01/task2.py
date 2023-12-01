import re

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
matching_words = [*numbers.values(), *numbers.keys()]

pattern = re.compile(r"|".join(matching_words))
pattern_reversed = re.compile(r"|".join([word[::-1] for word in matching_words]))


def find_digit(pattern: re.Pattern, numbers_dict: dict, string: str) -> int:
    digit = pattern.search(string).group()
    return int(numbers_dict.get(digit, digit))


def get_number(string: str) -> int:
    return 10 * find_digit(pattern, numbers, string) + find_digit(
        pattern_reversed, numbers_reversed, string[::-1]
    )


with open("input.txt", "r") as f:
    lines = f.readlines()

number = sum(get_number(line) for line in lines)
print(number)
