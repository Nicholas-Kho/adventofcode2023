from dataclasses import dataclass
from typing import List
from math import prod
@dataclass
class number:
    coordinates: List[List[int]]
    value: int

@dataclass
class gear:
    coord: List[int]
    def numAdjacent(self, num: number, surroundings: List[List[int]]) -> bool:
        for numCoords in num.coordinates:
            if numCoords in surroundings:
                return True
        return False

    def numberAround(self, data: List[List[str]], numbers: List[number]) -> int:
        surroundings: List[List[int]] = []
        for x in range(max(0, self.coord[0]-1), min(len(data), self.coord[0]+2)):
            for y in range(max(0, self.coord[1]-1), min(len(data[0]), self.coord[1]+2)):
                surroundings.append([x, y])

        return prod(num.value for num in numbers if self.numAdjacent(num, surroundings)) if (len([num for num in numbers if self.numAdjacent(num, surroundings)]) > 1) else 0

with open("day3part2.txt") as data:
    numbers: list[number] = []
    string_list: list[str] = []
    gears: List[gear] = []
    for line in data.readlines():
        string_list.append(line)

    row: int = 0
    for line in string_list:
        digit: str = ""
        col: int = 0
        coords: List[List[int]] = []
        for char in line:
            if char == "*":
                gears.append(gear([row, col]))
            if char.isdigit() is False and len(digit) > 0:
                numbers.append(number(coords, int(digit)))
                digit = ""
                coords = []
            else:
                if char.isdigit() and char != ".":
                    digit += char
                    coords.append([row, col])
            col += 1
        row += 1

    print(sum(g.numberAround(string_list, numbers) for g in gears))