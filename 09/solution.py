import functools


def part1(input_data):
    risk_level = 0
    height = len(input_data)
    width = len(input_data[0])
    for j in range(height):
        for i in range(width):
            cell = input_data[j][i]
            if j > 0 and input_data[j - 1][i] <= cell:
                continue
            if j < height - 1 and input_data[j + 1][i] <= cell:
                continue
            if i > 0 and input_data[j][i - 1] <= cell:
                continue
            if i < width - 1 and input_data[j][i + 1] <= cell:
                continue

            risk_level += cell + 1

    return risk_level


class Cell:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.visited = False

    def get_size(self):
        if self.visited:
            return 0
        self.visited = True

        return 1 + sum(map(lambda x: x.get_size(), self.neighbors))


def part2(input_data):
    # Floodfill every area that is not 9 and find their size
    basins = []

    # First build a cell grid with neighbor links
    height = len(input_data)
    width = len(input_data[0])
    grid = [[Cell(y) for y in x] for x in input_data]
    for j in range(height):
        for i in range(width):
            cell = grid[j][i]
            if cell.value == 9:
                continue

            if j > 0 and grid[j - 1][i].value != 9:
                cell.neighbors.append(grid[j - 1][i])
            if j < height - 1 and grid[j + 1][i].value != 9:
                cell.neighbors.append(grid[j + 1][i])
            if i > 0 and grid[j][i - 1].value != 9:
                cell.neighbors.append(grid[j][i - 1])
            if i < width - 1 and grid[j][i + 1].value != 9:
                cell.neighbors.append(grid[j][i + 1])

    for j in range(height):
        for i in range(width):
            cell = grid[j][i]
            if cell.value == 9 or cell.visited:
                continue

            # Floodfill
            basin_size = cell.get_size()
            basins.append(basin_size)

    return functools.reduce(lambda a, b: a * b, sorted(basins)[::-1][:3])


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        input_data = list(map(lambda x: [int(y) for y in x], input_data))
        print(part1(input_data))
        print(part2(input_data))
