with open("day7part1.txt") as data:
    camel_cards: dict[str, int] = {}
    for line in data.readlines():
        camel_cards[line.split()[0]] = line.split()[1]

    collection = {"one pair": [],
                  "two pair:": [],
                  "three of a kind": [],
                  "five of a kind": [],
                  "full house": [],
                  "high card": []}

    for key in camel_cards.keys():
        used_chars = {}
        unique_chars = 0

        test = 1
        for char in key:
            if char in used_chars:
                used_chars[char] += 1
                test += 1
            else:
                used_chars[char] = 1
                test = 1
        labels = 6-test
        print(used_chars, labels)

        single_dupe = 0
        two_dupes = 0
        three_dupes = 0
