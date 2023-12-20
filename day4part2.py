import re
from typing import List
with open ("day4part2.txt") as data:
    copies: List[int] = []
    cards: List[int] = []
    for line in data.readlines():
        firstArray: List[str] = re.split(r'\s+', (line.split("|")[0][8:-1]))
        secondArray: List[str] = re.split(r'\s+', (line.split("|")[1][1:len(line.split("|")[1])-1]))
        matches = (len([num for num in firstArray if num in secondArray]))

        if matches > len(copies):
            copies.extend(1 for i in range(matches + 1))
        cards.append(copies[len(cards)])
        print(cards, len(cards), matches, copies)
        for i in range(len(cards), matches + 1, 1):
            copies[i] += 1
        print(copies)
    print(sum(cards))