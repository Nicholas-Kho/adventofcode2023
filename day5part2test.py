seeds, *therest = open("day5part2.txt").read().split("\n\n")


seeds = list(map(int, seeds.split(":")[1].split()))
print(seeds)

uSeeds = []