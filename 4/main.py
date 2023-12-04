# Advent of Code - Day 3
import re

number_re = re.compile("[0-9]+")

input_file = 'input.txt'


def part1():
    with open(input_file, "r") as input_fp:
        total_score = 0
        for card in input_fp:
            card_values = card.split(':', maxsplit=1)[1].strip().split('|', maxsplit=2)
            winning_numbers = [int(value) for value in number_re.findall(card_values[0])]
            uncovered_values = [int(value) for value in number_re.findall(card_values[1])]
            matching_values = [value for value in winning_numbers if value in uncovered_values]
            if matching_values:
                total_score += 2 ** (len(matching_values) - 1)

    print(f"Part 1: {total_score}")


def part2():
    cards = dict()
    with open(input_file, "r") as input_fp:
        for game, card in enumerate(input_fp, start=1):
            card_values = card.split(':', maxsplit=1)[1].strip().split('|', maxsplit=2)
            winning_numbers = [int(value) for value in number_re.findall(card_values[0])]
            uncovered_values = [int(value) for value in number_re.findall(card_values[1])]
            cards[game] = (winning_numbers, uncovered_values)

    total_cards_won = len(cards)
    cards_to_check = [i for i in range(1, len(cards) + 1)]
    while cards_to_check:
        newly_won_cards = []
        for idx in cards_to_check:
            matching_values = [value for value in cards[idx][0] if value in cards[idx][1]]
            if matching_values:
                total_cards_won += len(matching_values)
                newly_won_cards.extend(range(idx + 1, idx + len(matching_values) + 1))
        cards_to_check = newly_won_cards

    print(f"Part 2: {total_cards_won}")


if __name__ == "__main__":
    part1()
    part2()
