def parseline(line):
    # "Card 1: 2 3 | 2 4 5" -> (1,{2,3}, {2,4,5})
    colon_index = line.find(':')
    card_prefix = line[:colon_index]
    card_number_str = card_prefix.split()[1]
    winning_numbers_str, own_numbers_str = line[colon_index+1:].split("|")
    winning_numbers = [int(num) for num in winning_numbers_str.split()]
    own_numbers = [int(num) for num in own_numbers_str.split()]
    return int(card_number_str), set(winning_numbers), set(own_numbers)

def parttwo(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    card_to_winning_count = {}
    card_counts = {}
    for line in lines:
        card_num, winning_numbers, my_numbers = parseline(line.strip())
        num_winning = len(winning_numbers.intersection(my_numbers))
        card_to_winning_count[card_num] = num_winning
        card_counts[card_num] = 1
    for card_number, number_of_cards in card_counts.items():
        for i in range(1, card_to_winning_count[card_number]+1):
            card_counts[card_number+i] = card_counts[card_number+i] + number_of_cards
    print(card_counts)
    return sum(card_counts.values())

def partone(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    points = 0
    for line in lines:
        _card_num, winning_numbers, my_numbers = parseline(line.strip())
        num_winning = len(winning_numbers.intersection(my_numbers))
        if num_winning:
            points += (2 ** (num_winning-1))
    return points

# print(partone("day4.txt"))
print(parttwo("day4.txt"))
