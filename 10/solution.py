class Block:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []
        self.parent = None


def part1(input_data):
    openers = "([{<"
    closers = ")]}>"
    error_score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    opener_closer = {"(": ")", "[": "]", "{": "}", "<": ">"}

    total_error_score = 0

    for line in input_data:
        stack = Block("")
        for symbol in line:
            if symbol in openers:
                block = Block(symbol)
                stack.children.append(block)
                block.parent = stack
                stack = block
            elif symbol in closers:
                if symbol == opener_closer[stack.symbol]:
                    stack = stack.parent
                else:
                    total_error_score += error_score[symbol]
                    break

    return total_error_score


def part2(input_data):
    openers = "([{<"
    closers = ")]}>"
    autocomplete_score = {")": 1, "]": 2, "}": 3, ">": 4}
    opener_closer = {"(": ")", "[": "]", "{": "}", "<": ">"}

    scores = []

    for line in input_data:
        stack = Block("")
        corrupt = False
        for symbol in line:
            if symbol in openers:
                block = Block(symbol)
                stack.children.append(block)
                block.parent = stack
                stack = block
            elif symbol in closers:
                if symbol == opener_closer[stack.symbol]:
                    stack = stack.parent
                else:
                    # Skip corrupted
                    corrupt = True
                    break

        if corrupt:
            continue

        completion_string = ""
        while True:
            completion_string += opener_closer[stack.symbol]
            stack = stack.parent
            if stack.parent is None:
                break

        score = 0
        for completion_symbol in completion_string:
            score *= 5
            score += autocomplete_score[completion_symbol]

        scores.append(score)

    return sorted(scores)[int(len(scores) / 2)]


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
