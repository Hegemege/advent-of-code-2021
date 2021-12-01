def part1(input_data):
    return sum([input_data[i + 1] > x for i, x in enumerate(input_data[:-1])])


def part2(input_data):
    return part1(
        [
            x + input_data[i + 1] + input_data[i + 2]
            for i, x in enumerate(input_data[:-2])
        ]
    )


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        input_data = list(map(int, input_data))
        print(part1(input_data))
        print(part2(input_data))
