class Octopus:
    def __init__(self, energy):
        self.flashed = False
        self.energy = energy
        self.neighbors = []
        self.flashes = 0

    def flash(self):
        if self.flashed:
            return
        self.flashed = True
        self.flashes += 1
        for neighbor in self.neighbors:
            neighbor.energy += 1
            if neighbor.energy > 9:
                neighbor.flash()


def part1(input_data):
    height = len(input_data)
    width = len(input_data[0])
    grid = [[Octopus(int(y)) for y in x] for x in input_data]
    for j in range(height):
        for i in range(width):
            cell = grid[j][i]
            if j > 0:
                cell.neighbors.append(grid[j - 1][i])
            if j < height - 1:
                cell.neighbors.append(grid[j + 1][i])
            if i > 0:
                cell.neighbors.append(grid[j][i - 1])
            if i < width - 1:
                cell.neighbors.append(grid[j][i + 1])
            if j > 0 and i > 0:
                cell.neighbors.append(grid[j - 1][i - 1])
            if j < height - 1 and i > 0:
                cell.neighbors.append(grid[j + 1][i - 1])
            if j > 0 and i < width - 1:
                cell.neighbors.append(grid[j - 1][i + 1])
            if j < height - 1 and i < width - 1:
                cell.neighbors.append(grid[j + 1][i + 1])

    for i in range(100):
        # Reset flashed for all octopuses and add 1 energy
        for row in grid:
            for octopus in row:
                octopus.flashed = False
                octopus.energy += 1

        for row in grid:
            for octopus in row:
                if octopus.energy > 9:
                    octopus.flash()

        for row in grid:
            for octopus in row:
                if octopus.flashed:
                    octopus.energy = 0

    return sum([sum([y.flashes for y in x]) for x in grid])


def part2(input_data):
    height = len(input_data)
    width = len(input_data[0])
    grid = [[Octopus(int(y)) for y in x] for x in input_data]
    for j in range(height):
        for i in range(width):
            cell = grid[j][i]
            if j > 0:
                cell.neighbors.append(grid[j - 1][i])
            if j < height - 1:
                cell.neighbors.append(grid[j + 1][i])
            if i > 0:
                cell.neighbors.append(grid[j][i - 1])
            if i < width - 1:
                cell.neighbors.append(grid[j][i + 1])
            if j > 0 and i > 0:
                cell.neighbors.append(grid[j - 1][i - 1])
            if j < height - 1 and i > 0:
                cell.neighbors.append(grid[j + 1][i - 1])
            if j > 0 and i < width - 1:
                cell.neighbors.append(grid[j - 1][i + 1])
            if j < height - 1 and i < width - 1:
                cell.neighbors.append(grid[j + 1][i + 1])

    i = 0
    while True:
        i += 1
        # Reset flashed for all octopuses and add 1 energy
        for row in grid:
            for octopus in row:
                octopus.flashed = False
                octopus.energy += 1

        for row in grid:
            for octopus in row:
                if octopus.energy > 9:
                    octopus.flash()

        all_flashed = True
        for row in grid:
            for octopus in row:
                if octopus.flashed:
                    octopus.energy = 0
                else:
                    all_flashed = False
        if all_flashed:
            return i


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
