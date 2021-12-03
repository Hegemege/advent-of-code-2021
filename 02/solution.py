def part1(input_data):
    horizontal = sum([x[1] for x in input_data if x[0] == "forward"])
    depth = sum([x[1] for x in input_data if x[0] == "down"]) - sum(
        [x[1] for x in input_data if x[0] == "up"]
    )
    return horizontal * depth


def part2(input_data):
    aim = 0
    horizontal = 0
    depth = 0
    for command in input_data:
        if command[0] == "forward":
            horizontal += command[1]
            depth += command[1] * aim
        elif command[0] == "down":
            aim += command[1]
        elif command[0] == "up":
            aim -= command[1]
    return horizontal * depth


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        input_data = list(map(lambda x: x.split(" "), input_data))
        input_data = [[x[0], int(x[1])] for x in input_data]
        print(part1(input_data))
        print(part2(input_data))
