import re

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    lines = [re.sub(r"\s+", " ", line) for line in lines]

cards = {}
for line in lines:
    id_part, number_part = line.split(":")
    card_id = id_part.split(" ")[1]
    winning_numbers_part, given_numbers_part = number_part.split("|")
    winning_numbers = [
        int(number) for number in winning_numbers_part.strip().split(" ")
    ]
    given_numbers = [int(number) for number in given_numbers_part.strip().split(" ")]
    cards[card_id] = [winning_numbers, given_numbers]


total_points = 0
for card_id, card in cards.items():
    points_counter = 0
    for given_number in card[1]:
        if given_number in card[0]:
            points_counter += 1
    if points_counter > 0:
        total_points += int(2 ** (points_counter - 1))

print(total_points)
