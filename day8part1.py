instructions, nodes = open("day8part1.txt").read().split("\n\n")
nodes = nodes.split("\n")
nodesMap = {}
import time
def getRid(s):
    return s.replace(",", "")
for node in nodes:
    nodesMap[node.split()[0]] = list(map(getRid, node[7:-1].split()))

destination = []
current_node = "AAA"
steps = 0
while current_node != "ZZZ":
    steps += 1
    if len(destination) == 0:
        for d in instructions:
            destination.append(d)
    direction = destination.pop(0)
    if direction == "R":
        current_node = nodesMap[current_node][1]
    if direction == "L":
        current_node = nodesMap[current_node][0]

print(steps, current_node)