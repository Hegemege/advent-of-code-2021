def part12(input_data, days):
    fish = {x: 0 for x in range(9)}

    for age in input_data:
        fish[age] += 1

    for i in range(days):
        new_fish = {x: 0 for x in range(9)}
        for age in range(9):
            if age == 0:
                new_fish[6] += fish[age]
                new_fish[8] += fish[age]
            else:
                new_fish[age - 1] += fish[age]

        fish = new_fish

    return sum(fish.values())


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        input_data = list(map(int, input_data[0].split(",")))
        print(part12(input_data, 80))
        print(part12(input_data, 256))
