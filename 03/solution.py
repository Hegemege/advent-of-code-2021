def part1(input_data):
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(input_data[0])):
        digit_total = sum([int(x[i]) for x in input_data])
        gamma_rate += "1" if digit_total / len(input_data) > 0.5 else "0"
        epsilon_rate += "0" if digit_total / len(input_data) > 0.5 else "1"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part2(input_data):
    oxygen_bitmask = ""
    co2_bitmask = ""
    for i in range(len(input_data[0])):
        oxygen_filtered = [x for x in input_data if x.startswith(oxygen_bitmask)]
        co2_filtered = [x for x in input_data if x.startswith(co2_bitmask)]
        oxygen_rating = sum([int(x[i]) for x in oxygen_filtered])
        co2_rating = sum([int(x[i]) for x in co2_filtered])

        if len(oxygen_filtered) > 1:
            oxygen_bitmask += (
                "1" if oxygen_rating / len(oxygen_filtered) >= 0.5 else "0"
            )
        if len(co2_filtered) > 1:
            co2_bitmask += "0" if co2_rating / len(co2_filtered) >= 0.5 else "1"

    # Final filtering
    oxygen_filtered = [x for x in input_data if x.startswith(oxygen_bitmask)]
    co2_filtered = [x for x in input_data if x.startswith(co2_bitmask)]
    return int("".join(oxygen_filtered), 2) * int("".join(co2_filtered), 2)


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data))
        print(part2(input_data))
