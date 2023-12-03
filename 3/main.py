# Advent of Code - Day 3
import re
number_re = re.compile("[0-9]+")
gear_re = re.compile("\*")

input_file = 'input.txt'


def get_bounds(num_str: str, loc: tuple[int, int], num_lines: int, line_length: int):
    v_range = (max(0, loc[0] - 1), min(num_lines - 1, loc[0] + 1))
    h_range = (max(0, loc[1] - 1), min(line_length - 1, loc[1] + len(num_str)))
    return v_range, h_range


def find_symbol(grid: list[str], bounds):
    for line in range(bounds[0][0], bounds[0][1] + 1):
        for char in range(bounds[1][0], bounds[1][1] + 1):
            if not grid[line][char].isdigit() and grid[line][char] != '.':
                return True
    return False


def find_gear_parts(grid: list[str]):
    # Find the * symbols
    potential_gears = []
    for line_num, line in enumerate(grid):
        star_matches = [match for match in gear_re.finditer(line)]
        potential_gears.extend([(line_num, match.span()[0]) for match in star_matches])

    # Check if there are two numbers adjacent to this star. We determine adjacency by overlapping horizontal
    # spans on the eligible lines. If we detect an adjacency, record the gear part values
    gear_parts = []
    for gear in potential_gears:
        line_range, gear_range = get_bounds('*', gear, len(grid), len(grid[0]))

        potential_gear_parts = []
        for line_idx in range(line_range[0], line_range[1] + 1):
            number_matches = [match for match in number_re.finditer(grid[line_idx])]
            for number in number_matches:
                number_range = (number.span()[0], number.span()[1] - 1)
                if gear_range[0] <= number_range[1] and number_range[0] <= gear_range[1]:
                    potential_gear_parts.append(int(number.group()))

        if len(potential_gear_parts) == 2:
            gear_parts.append((potential_gear_parts[0], potential_gear_parts[1]))

    return gear_parts


def part1():
    # Read in the input data and verify it
    with open(input_file,"r") as input_fp:
        grid_lines = input_fp.read().splitlines()

    line_lengths = [len(line) for line in grid_lines]
    if not all(val == line_lengths[0] for val in line_lengths):
        raise ValueError("Not all grid lines are the same length!")
    line_length = line_lengths[0]

    # Look for the numbers in each line. Find the bounding box around them, and check for any
    # symbol characters. If there is a symbol, add the number to the total
    part_number_total = 0
    for line_num, line in enumerate(grid_lines):
        number_matches = [match for match in number_re.finditer(line)]
        for number in number_matches:
            boundaries = get_bounds(number.group(), (line_num, number.span()[0]), len(grid_lines), line_length)
            if find_symbol(grid_lines, boundaries):
                part_number_total += int(number.group())

    print(f"Part 1: {part_number_total}")


def part2():
    # Read in the input data and verify it
    with open(input_file,"r") as input_fp:
        grid_lines = input_fp.read().splitlines()

    line_lengths = [len(line) for line in grid_lines]
    if not all(val == line_lengths[0] for val in line_lengths):
        raise ValueError("Not all grid lines are the same length!")
    line_length = line_lengths[0]

    # Find the gear parts. If we find * that has two digits in its bounds, record where those digits
    # are, and we'll go find the numbers later
    gear_parts = find_gear_parts(grid_lines)
    gear_ratio_sum = sum([gear1 * gear2 for gear1,gear2 in gear_parts])
    print(f"Part 2: {gear_ratio_sum}")


if __name__ == "__main__":
    part1()
    part2()
