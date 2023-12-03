# Advent of Code - Day 2
import math
import re

input_file = 'input.txt'
game_re = re.compile("Game ([0-9]+)")
draw_re = re.compile("([0-9]+) (red|green|blue)")


def part1():
    bag_contents = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    with open(input_file, "r") as input:
        game_id_sum = 0
        for line in input:
            game_number = int(game_re.match(line).groups()[0])
            draws = line.split(':', maxsplit=1)[1]
            try:
                draw_info = draw_re.findall(draws)
                for color_info in draw_info:
                    if bag_contents[color_info[1]] < int(color_info[0]):
                        raise ValueError("Bag Invalid")
            except ValueError as e:
                continue
            game_id_sum += game_number

    print(f"Part 1: {game_id_sum}")


def part2():
    with open(input_file, "r") as input:
        power_sum = 0
        for line in input:
            game_number = int(game_re.match(line).groups()[0])
            draws = line.split(':', maxsplit=1)[1]
            required_bag = {
                'red': 0,
                'green': 0,
                'blue': 0
            }

            draw_info = draw_re.findall(draws)
            for color_info in draw_info:
                required_bag[color_info[1]] = max(required_bag[color_info[1]], int(color_info[0]))
            power_sum += math.prod([v for k,v in required_bag.items()])

    print(f"Part 2: {power_sum}")


if __name__ == "__main__":
    part1()
    part2()
