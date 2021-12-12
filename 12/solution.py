class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.neighbors = []

    def walk(self, path):
        path += [self.symbol]
        if self.symbol == "end":
            return [path]

        neighbor_paths = []
        for neighbor in self.neighbors:
            if neighbor.symbol == "start":
                continue
            if neighbor.symbol.islower() and neighbor.symbol in path:
                continue

            neighbor_path = neighbor.walk(path[:])
            neighbor_paths += neighbor_path

        return neighbor_paths

    def walk_part2(self, path):
        path += [self.symbol]
        if self.symbol == "end":
            return [path]

        neighbor_paths = []
        for neighbor in self.neighbors:
            if neighbor.symbol == "start":
                continue
            if (
                neighbor.symbol != "end"
                and neighbor.symbol.islower()
                and neighbor.symbol in path
                and path_visited_small_cave_twice(path)
            ):
                continue

            neighbor_path = neighbor.walk_part2(path[:])
            neighbor_paths += neighbor_path

        return neighbor_paths


def part1(input_data):
    nodes = {}
    for line in input_data:
        a, b = line.split("-")
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)

        nodes[a].neighbors.append(nodes[b])
        nodes[b].neighbors.append(nodes[a])

    # Pathfind from start, find all paths to end
    paths = nodes["start"].walk([])
    return len(paths)


def part2(input_data):
    nodes = {}
    for line in input_data:
        a, b = line.split("-")
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)

        nodes[a].neighbors.append(nodes[b])
        nodes[b].neighbors.append(nodes[a])

    # Pathfind from start, find all paths to end
    paths = nodes["start"].walk_part2([])
    return len(paths)


def path_visited_small_cave_twice(path):
    visited = {}
    for node in path:
        if node not in visited:
            visited[node] = 0
        visited[node] += 1
        if node.islower() and visited[node] > 1:
            return True
    return False


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
