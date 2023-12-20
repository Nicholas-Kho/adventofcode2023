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

    colours = {"g": 13,
               "r": 12,
               "b": 14}


    s_list = s[8:len(s)]
    n = len(s_list)
    for i in range(n):
        for key in colours.keys():
            if str(s_list[i]) == str(key):
                value = 0
                if s_list[i - 3].isnumeric():
                    second_digit = int(s_list[i - 3]) * 10
                    value += second_digit
                value += (int(s_list[i - 2]))
                if value > colours[key]:
                    return 0
    return game_id

print(isPossible("Game 99: 9 blue, 12 red; 9 blue, 11 red, 13 green; 9 blue, 1 red, 13 green; 4 blue, 12 green; 10 blue, 17 red, 8 green"))

total = 0
with open("advent.txt") as data:
    for line in data.readlines():
        total += int(isPossible(line))
        print(total, "total")
print(total)