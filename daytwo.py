import re

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

def get_game_rgb(reveal_string):
    # In "3 blue, 4 red" -> (4,0,3)
    red = green = blue = 0
    components = reveal_string.split(", ")
    for comp in components:
        if comp.endswith("red"):
            red = re.match("[0-9]+ ", comp).group(0).rstrip()
        if comp.endswith("green"):
            green = re.match("[0-9]+ ", comp).group(0).rstrip()
        if comp.endswith("blue"):
            blue = re.match("[0-9]+ ", comp).group(0).rstrip()
    return (int(red), int(green), int(blue))

def check_valid_game(game_string):
    reveals = game_string.split("; ")
    for reveal in reveals:
        rgb = get_game_rgb(reveal.strip())
        if (
                rgb[0] > RED_LIMIT or
                rgb[1] > GREEN_LIMIT or
                rgb[2] > BLUE_LIMIT
        ):
            return False
    return True

def count_ids(filename):
    # Part One
    file = open(filename, 'r')
    total = 0
    for line in file.readlines():
        game, string = line.split(":")
        game_id = game[5:]
        if check_valid_game(string.strip()):
            print(game_id)
            total += int(game_id)
    return total

def find_min_rgb(game_string):
    red = green = blue = 0
    reveals = game_string.split("; ")
    for reveal in reveals:
        rgb = get_game_rgb(reveal.strip())
        red = max(red, rgb[0])
        green = max(green, rgb[1])
        blue = max(blue, rgb[2])
    return (red, green, blue)



def count_sum_of_powers(filename):
    # Part Two
    file = open(filename, 'r')
    total = 0
    for line in file.readlines():
        _, string = line.split(":")
        min_rgb = find_min_rgb(string)
        rgb_power = min_rgb[0] * min_rgb[1] * min_rgb[2]
        total += rgb_power

    return total

print(count_sum_of_powers("day2.txt"))