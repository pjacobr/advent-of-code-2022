with open('input-problem4.txt', 'r') as file:
    data = file.read()

pairs = data.splitlines()

number_of_matches = []
for line in pairs:
    pair_1, pair_2 = line.split(',')
    pair_1_lower, pair_1_upper = pair_1.split('-')
    pair_2_lower, pair_2_upper = pair_2.split('-')
    # as int
    pair_1_lower = int(pair_1_lower)
    pair_1_upper = int(pair_1_upper)
    pair_2_lower = int(pair_2_lower)
    pair_2_upper = int(pair_2_upper)

    # check if pair 1 lower is less than pair 2 lower
    if pair_1_lower <= pair_2_lower and pair_1_upper >= pair_2_upper:
        number_of_matches.append(line)
    elif pair_2_lower <= pair_1_lower and pair_2_upper >= pair_1_upper:
        number_of_matches.append(line)


# part 2
number_of_matches = []
for line in pairs:
    pair_1, pair_2 = line.split(',')
    pair_1_lower, pair_1_upper = pair_1.split('-')
    pair_2_lower, pair_2_upper = pair_2.split('-')
    # as int
    pair_1_lower = int(pair_1_lower)
    pair_1_upper = int(pair_1_upper)
    pair_2_lower = int(pair_2_lower)
    pair_2_upper = int(pair_2_upper)

    # check if pair 1 lower is less than pair 2 lower
    if pair_1_lower <= pair_2_lower and pair_1_upper >= pair_2_lower:
        number_of_matches.append(line)
    elif pair_1_lower <= pair_2_upper and pair_1_upper >= pair_2_upper:
        number_of_matches.append(line)
    elif pair_2_lower <= pair_1_lower and pair_2_upper >= pair_1_lower:
        number_of_matches.append(line)
    elif pair_2_lower <= pair_1_upper and pair_2_upper >= pair_1_upper:
        number_of_matches.append(line)




