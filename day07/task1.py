from collections import Counter
from functools import cmp_to_key

with open("input.txt", "r") as f:
    hands = [[line.split()[0], int(line.split()[1])] for line in f.readlines()]


def get_hand_type(hand: str) -> int:
    match sorted(Counter(hand).values()):
        case [5]:  # Five of a kind
            return 7
        case [1, 4]:  # Four of a kind
            return 6
        case [2, 3]:  # Full house
            return 5
        case [1, 1, 3]:  # Three of a kind
            return 4
        case [1, 2, 2]:  # Two pairs
            return 3
        case [1, 1, 1, 2]:  # One pair
            return 2
        case [1, 1, 1, 1, 1]:  # High card
            return 1
    return -1


def get_card_value(card: str) -> int:
    values = "AKQJT98765432"
    if card in values:
        return values.index(card)
    else:
        return -1


def compare_hands_by_cards(first_hand: str, second_hand: str) -> bool:
    for first_hand_card, second_hand_card in zip(first_hand, second_hand):
        first_hand_card_value = get_card_value(first_hand_card)
        second_hand_card_value = get_card_value(second_hand_card)
        if first_hand_card_value < second_hand_card_value:
            return 1
        elif first_hand_card_value > second_hand_card_value:
            return -1
    return 0


def compare_hands(first_hand: str, second_hand: str) -> int:
    first_hand_type = get_hand_type(first_hand)
    second_hand_type = get_hand_type(second_hand)
    if first_hand_type > second_hand_type:
        return 1
    elif first_hand_type < second_hand_type:
        return -1
    else:
        return compare_hands_by_cards(first_hand, second_hand)


def compare_hand_bid_pairs(
    first_hand_bid_pair: [str, int], second_hand_bid_pair: [str, int]
) -> bool:
    return compare_hands(first_hand_bid_pair[0], second_hand_bid_pair[0])


hands_sorted = sorted(hands, key=cmp_to_key(compare_hand_bid_pairs))
total_winnings = sum(hand[1] * i for i, hand in enumerate(hands_sorted, 1))
print(f"{total_winnings}")
