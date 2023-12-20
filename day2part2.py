def isPossible(s):

    game_id = s[5]
    print(s[5], s[6])
    if s[6].isnumeric():
        game_id = int(game_id)
        game_id *= 10
        game_id += int(s[6])
        print(game_id)
    s = s.replace("green", "g")
    s = s.replace("blue", "b")
    s = s.replace("red", "r")
    print(s)
    s_list = s[8:len(s)]

    colours = {"g":0,
               "r":0,
               "b": 0}
    n = len(s_list)
    # print(s)
    # print(s_list)
    for i in range(n):
        for key in colours.keys():
            # print(s_list[i], key)
            if str(s_list[i]) == str(key):
                # print("hey")
                value = 0
                if s_list[i - 3].isnumeric():
                    second_digit = int(s_list[i - 3]) * 10
                    value += second_digit
                value += (int(s_list[i - 2]))
                if value > colours[key]:
                    colours[key] = value
    # print(colours)
    # print(game_id)

    possible_colours = {"g":14,
                        "r":14,
                        "b":12}
    # print(s, colours)
    testvalue = 0
    print(colours)
    for value in colours.values():
        if testvalue == 0:
            testvalue += value
        else:
            testvalue *= value
    print(testvalue)
    return testvalue

# print(isPossible("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"))
total = 0
with open("advent.txt") as data:
    for line in data.readlines():
        total += isPossible(line)
        print(total, "total")
print(total)
# 9 blue 4 green 5 red