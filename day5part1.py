from dataclasses import dataclass
@dataclass
class seed:
    value: int
    current_value: int
    corresponding_values: dict[str, int]

with open("day5part1.txt") as data:
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

    for s in seed_list:
        seeds.append(seed(s, s, {}))

    for map in maps.keys():
        for numArray in maps[map]:
            fullArray = numArray.split(" ")
            destination = int(fullArray[0])
            source = int(fullArray[1])
            length = int(fullArray[2])
            corresponds: dict[int, int] = {}
            for s in seeds:
                if source <= int(s.current_value) <= source+length:
                    if map not in s.corresponding_values.keys():
                        s.corresponding_values[map] = (int(s.current_value) - source) + destination
                        s.current_value = (int(s.current_value) - source) + destination

        for s in seeds:
            if map not in s.corresponding_values.keys():
                s.corresponding_values[map] = int(s.current_value)

    lowest_val: int = None
    for s in seeds:
        lowest_val = (s.corresponding_values["humidity_to_location"] if lowest_val > s.corresponding_values["humidity_to_location"] else lowest_val) if lowest_val is not None else s.corresponding_values["humidity_to_location"]

print(lowest_val)