import re
with open ("day4part2.txt") as data:
    copies: list[int] = []
    cards: list[int] = []
    for line in data.readlines():
        firstArray: list[str] = re.split(r'\s+', (line.split("|")[0][8:-1]))
        secondArray: list[str] = re.split(r'\s+', (line.split("|")[1][1:len(line.split("|")[1])-1]))
        matches = (len([num for num in firstArray if num in secondArray]))
        cards.append(copies.pop(0) if len(copies) > 0 else 1)
        copies.extend(1 for i in (range(matches - len(copies))))
        copies = [i + (1 * cards[-1]) for i in copies[0:matches]] + copies[matches:]
print(sum(cards))