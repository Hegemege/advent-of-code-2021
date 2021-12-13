def fold(grid, axis, fold_index):
    width = len(grid[0])
    height = len(grid)
    if axis == "x":
        folded_grid = [[False for x in range(fold_index)] for y in range(height)]
        for y in range(height):
            for x in range(width):
                if x == fold_index:
                    continue
                flipped_x = fold_index - abs(fold_index - x)
                folded_grid[y][flipped_x] = folded_grid[y][flipped_x] or grid[y][x]
        return folded_grid
    else:
        folded_grid = [[False for x in range(width)] for y in range(fold_index)]
        for y in range(height):
            if y == fold_index:
                continue
            for x in range(width):
                flipped_y = fold_index - abs(fold_index - y)
                folded_grid[flipped_y][x] = folded_grid[flipped_y][x] or grid[y][x]
        return folded_grid


def part12(input_data):
    points = []
    fold_lines = []
    for line in input_data:
        if line.startswith("f"):
            fold_lines.append(line.replace("fold along ", ""))
        elif "," in line:
            x, y = line.split(",")
            points.append([int(x), int(y)])

    width = max(list(zip(*points))[0]) + 1
    height = max(list(zip(*points))[1]) + 1

    grid = [[False for x in range(width)] for y in range(height)]

    for point in points:
        grid[point[1]][point[0]] = True

    for index, fold_line in enumerate(fold_lines):
        axis, fold_index = fold_line.split("=")
        grid = fold(grid, axis, int(fold_index))
        if index == 0:
            print(sum(map(sum, grid)))

    for row in grid:
        print("".join(map(lambda x: "#" if x else ".", row)))


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        part12(input_data)
