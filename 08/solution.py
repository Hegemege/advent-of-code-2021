import itertools


def part1(input_data):
    return sum(
        map(
            lambda x: sum(
                map(
                    lambda y: len(y) == 2 or len(y) == 3 or len(y) == 4 or len(y) == 7,
                    x.split(" | ")[1].split(" "),
                )
            ),
            input_data,
        )
    )


def part2(input_data):
    entries = list(map(lambda x: x.split(" | "), input_data))
    return sum(map(get_entry_output, entries))


def get_entry_output(entry):
    clues = entry[0].split(" ")
    outputs = entry[1].split(" ")
    output_digits = [None, None, None, None]

    segment_map = [
        [0, 1, 2, 4, 5, 6],
        [2, 5],
        [0, 2, 3, 4, 6],
        [0, 2, 3, 5, 6],
        [1, 2, 3, 5],
        [0, 1, 3, 5, 6],
        [0, 1, 3, 4, 5, 6],
        [0, 2, 5],
        [0, 1, 2, 3, 4, 5, 6],
        [0, 1, 2, 3, 5, 6],
    ]

    digit_possibilities = [[], [], [1], [7], [4], [2, 3, 5], [0, 6, 9], [8]]

    # Brute force all wire connections, 7! is only 5040
    permutations = itertools.permutations("abcdefg")
    for permutation in permutations:
        # Make sure all 10 digits form correctly with the given permutation
        satisfied_digits = [False for i in range(10)]
        for clue in clues:
            for possible_digit in digit_possibilities[len(clue)]:
                if satisfied_digits[possible_digit]:
                    continue

                clue_segments = sorted(list(map(lambda x: permutation.index(x), clue)))
                digit_segments = segment_map[possible_digit]
                if clue_segments == digit_segments:
                    satisfied_digits[possible_digit] = True

        if sum(satisfied_digits) == 10:
            digits = ""
            for output in outputs:
                output_segments = sorted(
                    list(map(lambda x: permutation.index(x), output))
                )
                for i in range(10):
                    digit_segments = segment_map[i]
                    if output_segments == digit_segments:
                        digits += str(i)
                        break

            return int(digits)

    exit(1)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
