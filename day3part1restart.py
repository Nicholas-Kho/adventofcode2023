from dataclasses import dataclass
from typing import List
import string
@dataclass
class number:
    coordinates: List[List[int]]
    value: int
    def symbolAround(self, data: List[List[str]]) -> bool:
        for coord in self.coordinates:
            for x in range(max(0, coord[0]-1), min(len(data), coord[0]+2)):
                for y in range(max(0, coord[1]-1), min(len(data[0]), coord[1]+2)):
                    if isSymbol(data[x][y]):
                        return True
        return False

def isSymbol(text):
    return False if text == "." else text in string.punctuation

with open("day3part1.txt") as data:
    numbers: list[number] = []
    string_list: list[str] = []
    for line in data.readlines():
        string_list.append(line)
    row: int = 0
    for line in string_list:
        digit: str = ""
        col: int = 0
        coords: List[List[int]] = []
        for char in line:
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

    print(sum(num.value for num in numbers if num.symbolAround(string_list)))