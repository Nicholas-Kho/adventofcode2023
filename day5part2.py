from dataclasses import dataclass
@dataclass
class seed:
    value: int
    current_value: int
    corresponding_values: dict[str, int]

with open("day5part2.txt") as data:
    temp = data.readlines()
    text: list[str] = []
    maps: dict[str, list[str]] = {}
    seeds: list[seed] = []
    for line in temp[2:]:
        text.append(line)
        if not line[0].isnumeric():
            maps[line[:len(line)-6].replace("-", "_")] = []
        else:
            maps[list(maps.keys())[-1]].append(line[:len(line)-1])
    seed_list: list[str] = temp[0][7:len(temp[0])-1].split(" ")
    firstSeeds: list[str] = seed_list[::2]
    secondSeeds: list[str] = seed_list[1::2]
    seed_set = set()
    seed_test: list[list[int]] = []
    for i in range(len(firstSeeds)):
        seed_test.append([int(firstSeeds[i]), int(firstSeeds[i]) + int(secondSeeds[i])])
    print(seed_test)