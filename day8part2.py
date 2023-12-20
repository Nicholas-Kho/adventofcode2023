import math
instructions, nodes = open("day8part2.txt").read().split("\n\n")
nodes = nodes.split("\n")
nodesMap = {}
def getRid(s):
    return s.replace(",", "")
for node in nodes:
    nodesMap[node.split()[0]] = list(map(getRid, node[7:-1].split()))
current_nodes = []
for node in nodesMap.keys():
    if node[-1] == "A":
        current_nodes.append(node)

nodesandexit = {}
for node in current_nodes:
    destination = []
    steps = 0
    next_node = node
    while next_node[-1] != "Z":
        steps += 1
        if len(destination) == 0:
            for di in instructions:
                destination.append(di)
        currentDirection = destination.pop(0)
        if currentDirection == "L":
            next_node = nodesMap[next_node][0]
        else:
            next_node = nodesMap[next_node][1]
        print(next_node)
    nodesandexit[node] = steps

print(nodesandexit)
values = nodesandexit.values()
print(math.lcm(*[int(v) for v in values]))