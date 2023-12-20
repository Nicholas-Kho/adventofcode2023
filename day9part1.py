patterns = open("day9part1.txt").read().split("\n")

for line in patterns:
    pattern_indexes = line.split()
    first_differences = []
    differences = {}
    total_difference = 1
    time = 0

    for i in range(0, len(pattern_indexes) - 1, 1):
        print("asdf")

    while total_difference != 0:
        time += 1
        for i in range(0, differences(differences.keys()[-1]) - 1, 1):
        # print(int(pattern_indexes[i+1]), int(pattern_indexes[i]))
            differences[time] = []
            first_differences.append(int(pattern_indexes[i+1]) - int(pattern_indexes[i]))
    print(first_differences)