def part1(input_data, n):
    patterns = {}
    polymer = input_data[0]

    for i in range(2, len(input_data)):
        line = input_data[i]
        key, value = line.split(" -> ")
        patterns[key] = value

    for _ in range(n):
        new_polymer = ""
        for i in range(len(polymer) - 1):
            new_polymer += polymer[i]
            pair = polymer[i : i + 2]
            if pair in patterns:
                new_polymer += patterns[pair]
        new_polymer += polymer[-1]

        polymer = new_polymer

    totals = {}
    for symbol in polymer:
        if symbol not in totals:
            totals[symbol] = 0
        totals[symbol] += 1

    return max(totals.values()) - min(totals.values())


def part2(input_data, n):
    patterns = {}
    polymer = input_data[0]

    for i in range(2, len(input_data)):
        line = input_data[i]
        key, value = line.split(" -> ")
        patterns[key] = value

    # We can simply calculate the number each pair of symbols is being used
    # as there is obviously not enough memory to store the whole string, or time
    # to iterate it
    pair_counts = {}
    for i in range(len(polymer) - 1):
        pair = polymer[i : i + 2]
        if pair not in pair_counts:
            pair_counts[pair] = 0
        pair_counts[pair] += 1

    # Build a substitution map of all source pairs to target pairs
    # e.g. AB -> C becomes the kvp: AB -> [AC, CB]
    substitution_map = {}
    for pattern, addition in patterns.items():
        first_pair = pattern[0] + addition
        second_pair = addition + pattern[1]
        substitution_map[pattern] = [first_pair, second_pair]

    # Find the substitute pairs for each pair and add the same amount of each
    # e.g. BBB with the rule BB -> N becomes BNBNB, and has originally 2 pairs of BB,
    # becoming 2 pairs of BM and 2 pairs of NB and so on
    for _ in range(n):
        new_pair_counts = {}
        for pair, count in pair_counts.items():
            substitutions = substitution_map[pair]
            for substitution in substitutions:
                if substitution not in new_pair_counts:
                    new_pair_counts[substitution] = 0
                new_pair_counts[substitution] += count

        pair_counts = new_pair_counts

    symbol_counts = {}
    for pair, count in pair_counts.items():
        for symbol in pair:
            if symbol not in symbol_counts:
                symbol_counts[symbol] = 0
            symbol_counts[symbol] += count

    # symbol_counts now contains every symbol twice, since the first symbol of a pair is
    # the second symbol of another pair
    # The only exception is the first symbol and last symbol in the string, as they
    # don't have another pair - so add one extra of those. We know what the first and last
    # symbols are, because they can not change in this iterative process
    first_symbol = polymer[0]
    last_symbol = polymer[-1]

    for symbol, count in symbol_counts.items():
        symbol_counts[symbol] = int(count / 2)
        if symbol == first_symbol:
            symbol_counts[symbol] += 1
        if symbol == last_symbol:
            symbol_counts[symbol] += 1

    return max(symbol_counts.values()) - min(symbol_counts.values())


if __name__ == "__main__":
    with open("input", "r") as input_file:
        input_data = list(map(lambda x: x.strip(), input_file.readlines()))
        print(part1(input_data, 10))
        print(part2(input_data, 40))
