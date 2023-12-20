import re
with open ("day4part2.txt") as data:
    copies, cards = [], []
    for line in data.readlines():
        cards.append(copies.pop(0) if len(copies) > 0 else 1)
        copies.extend(1 for i in (range((len([num for num in (line.split("|")[0][8:-1]).split(" ") if num in re.split(r'\s+', (line.split("|")[1][1:len(line.split("|")[1])-1]))])) - len(copies))))
        copies = [i + (1 * cards[-1]) for i in copies[0:(len([num for num in re.split(r'\s+', (line.split("|")[0][8:-1])) if num in re.split(r'\s+', (line.split("|")[1][1:len(line.split("|")[1])-1]))]))]] + copies[(len([num for num in re.split(r'\s+', (line.split("|")[0][8:-1])) if num in re.split(r'\s+', (line.split("|")[1][1:len(line.split("|")[1])-1]))])):]
print(sum(cards)) #part2
print(sum((2**(len([number for number in re.split(r'\s+', (line.split("|")[0][8:-1])) if number in re.split(r'\s+', (line.split("|")[1][1:len(line.split("|")[1])-1]))]) - 1) if len([number for number in re.split(r'\s+', (line.split("|")[0][8:-1])) if number in re.split(r'\s+', (line.split("|")[1][1:len(line.split("|")[1])-1]))]) >= 1 else 0) for line in open("day4part1.txt").readlines())) # part one