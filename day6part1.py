import re
from math import prod
time, distance = open("day6part1.txt").read().split("\n")

time = list(map(int, re.findall(r'\d+', time.split(":")[1])))
records = list(map(int, re.findall(r'\d+', distance.split(":")[1])))

products = []
for i in range(len(time)):
    ways = 0
    for s in range(1, time[i] + 1):
        distance = s * (time[i] - s)
        ways = ways + 1 if distance > records[i] else ways
        print(ways)
    products.append(ways)
print(prod(products))

