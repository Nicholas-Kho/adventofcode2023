import re

total = 0
replace = {"\sgreen": "g","\sblue": "b","\sred":"r",";":",",":":"",",":""}
with open("advent.txt") as data:
    for string in data.readlines():
        for colour in replace:
            string = re.sub((colour), replace[colour], string)
        game_id = (string.split(" "))[1]
        colours = {"r":0,"g":0,"b":0}
        string = string[0:len(string)-1].split(" ")
        for i in range(len(string)-1, 1, -1):
            colours[string[i][-1]] = string[i][0:len(string[i])-1] if int(colours[string[i][-1]]) < int(string[i][0:len(string[i])-1]) else colours[string[i][-1]]
        num = 0
        for val in colours.values():
            num = int(val) if num == 0 else num * int(val)
        total += num
    print(total)