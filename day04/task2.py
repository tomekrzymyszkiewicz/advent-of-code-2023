import re

with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    lines = [re.sub(r"\s+", " ", line) for line in lines]

cards = {}
for line in lines:
    id_part, number_part = line.split(":")
    card_id = int(id_part.split(" ")[1])
    winning_numbers_part, given_numbers_part = number_part.split("|")
    winning_numbers = [
        int(number) for number in winning_numbers_part.strip().split(" ")
    ]
    given_numbers = [int(number) for number in given_numbers_part.strip().split(" ")]
    cards[card_id] = [winning_numbers, given_numbers,1]


for card_id, card in cards.items():
    number_of_matches = sum([1 for given_number in card[0] if given_number in card[1]])
    if number_of_matches > 0:
        for id in range(card_id+1,card_id+number_of_matches+1):
            cards[id][2] += card[2]
        

print(sum([card[2] for card in cards.values()]))
