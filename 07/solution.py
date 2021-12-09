import math


def part1(input_data):
    minx = min(input_data)
    maxx = max(input_data)
    lowest_fuel = math.inf
    for i in range(minx, maxx + 1):
        total_fuel = sum(map(lambda x: abs(x - i), input_data))
        if total_fuel < lowest_fuel:
            lowest_fuel = total_fuel

    return lowest_fuel


def part2(input_data):
    minx = min(input_data)
    maxx = max(input_data)
    lowest_fuel = math.inf
    for i in range(minx, maxx + 1):
        total_fuel = sum(map(lambda x: sum(range(1, abs(x - i) + 1)), input_data))
        if total_fuel < lowest_fuel:
            lowest_fuel = total_fuel

    return lowest_fuel


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        input_data = list(map(int, input_data[0].split(",")))
        print(part1(input_data))
        print(part2(input_data))
