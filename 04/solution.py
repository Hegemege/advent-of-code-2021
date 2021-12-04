def part1(input_data):
    numbers, boards = parse_input(input_data)

    for number in numbers:
        # Put number on all boards
        for board in boards:
            for row in board:
                for i in range(len(row)):
                    if number == row[i]:
                        row[i] = "x"

        # Check for bingo
        for board in boards:
            for row in board:
                if "".join(row) == "xxxxx":
                    return int(number) * unmarked_sum(board)
            for column in zip(*board):
                if "".join(column) == "xxxxx":
                    return int(number) * unmarked_sum(board)


def part2(input_data):
    numbers, boards = parse_input(input_data)

    board_scores = [0 for x in boards]
    last_index = None

    for number in numbers:
        # Put number on all boards
        for board in boards:
            for row in board:
                for i in range(len(row)):
                    if number == row[i]:
                        row[i] = "x"

        # Check for bingo
        for i, board in enumerate(boards):
            for row in board:
                if "".join(row) == "xxxxx" and board_scores[i] == 0:
                    board_scores[i] = int(number) * unmarked_sum(board)
                    last_index = i
            for column in zip(*board):
                if "".join(column) == "xxxxx" and board_scores[i] == 0:
                    board_scores[i] = int(number) * unmarked_sum(board)
                    last_index = i

    return board_scores[last_index]


def unmarked_sum(board):
    return sum(
        map(
            lambda x: sum(map(lambda y: int(y) if y != "x" else 0, x)),
            board,
        )
    )


def parse_input(input_data):
    numbers = input_data[0].split(",")
    boards = []
    for i in range(1, len(input_data), 6):
        rows = input_data[i + 1 : i + 6]
        rows = list(
            map(lambda x: list(filter(lambda y: len(y) > 0, x.split(" "))), rows)
        )
        boards.append(rows)

    return numbers, boards


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
