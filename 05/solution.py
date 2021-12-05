def part12(lines):
    maxx = max(map(lambda x: max(x[0][0], x[1][0]), lines))
    maxy = max(map(lambda x: max(x[0][1], x[1][1]), lines))
    grid = [[0 for x in range(maxx + 1)] for y in range(maxy + 1)]

    for line in lines:
        (sx, sy), (ex, ey) = line
        dx = ex - sx
        dy = ey - sy
        d = max(abs(dx), abs(dy))
        for i in range(d + 1):
            x = sx + sign(dx) * i
            y = sy + sign(dy) * i
            grid[y][x] += 1

    return sum(map(lambda x: len(list(filter(lambda y: y > 1, x))), grid))


def parse_input(input_data):
    return list(
        map(
            lambda x: list(
                map(lambda y: list(map(int, y.split(","))), x.split(" -> "))
            ),
            input_data,
        )
    )


def sign(x):
    return 0 if x == 0 else (1 if x > 0 else -1)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))

        lines = parse_input(input_data)
        parallel_lines = list(
            filter(lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1], lines)
        )

        print(part12(parallel_lines))
        print(part12(lines))
