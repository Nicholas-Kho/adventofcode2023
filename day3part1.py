from dataclasses import dataclass
from typing import List
import re

@dataclass
class number:
    coordinates: List[int]
    value: int

with open("day3part1.txt") as data:
    the_list = []
    symbols = ["*", "#", "+", "$", "@", "/", "%", "=", "-", "_", "&"]
    symbol_indexes = []
    for line in data.readlines():
        the_list.append(line)
        symbol_indexes.append([i for i, symbol in enumerate(line) if symbol in symbols])
    row_length = len(the_list[0])
    col_length = len(the_list)
    print(symbol_indexes)
    c_row = 0
    print(the_list)
    for list in symbol_indexes:

        for symbol_index in list:
            for i in range(max(0, symbol_index - 1), min(row_length, symbol_index + 2)):
                for x in range(max(0, c_row - 1), min(col_length, c_row + 2)):
                    # print(the_list[c_row][symbol_index], the_list[x][i], x, i)

                    if the_list[indexes][symbol_index].isNumeric():
                        iterate_index = symbol_index
                        while iterate_index.isNumeric():
                            iterate_index -= 1
                        number = symbol_indexes[indexes][iterate_index]
                        while iterate_index.isNumeric():
                            iterate_index += 1
                            number = (number * (10 ** len(number))) + symbol_indexes[indexes][iterate_index]
                        print(number)

        c_row += 1