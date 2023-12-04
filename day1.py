STRING_DIGITS = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

LONGEST_DIGIT_STRING = max([len(a) for a in STRING_DIGITS.keys()])

def getdigit(string):
    # Returns either the digit (e.g. 3) or None
    if string[0].isnumeric():
        return int(string[0])
    for letters, digit in STRING_DIGITS.items():
        if string.startswith(letters):
            return digit
    return None
def finddigitv2(string, forward=True):
    index = 0 if forward else len(string)-1
    increment = 1 if forward else -1
    while True:
        end_index = min(index + LONGEST_DIGIT_STRING, len(string))
        digit_or_none = getdigit(string[index:end_index])
        if digit_or_none:
            return digit_or_none
        index += increment

def finddigitv1(string, forward=True):
    index = 0 if forward else len(string)-1
    increment = 1 if forward else -1
    while True:
        if string[index].isnumeric():
            return string[index]
        index += increment

def partone(filename):
    file = open(filename, 'r')
    total = 0
    for line in file.readlines():
        first = finddigitv1(line)
        last = finddigitv1(line, forward=False)
        num = int(first + last)
        total = total + num
    return total


def parttwo(filename):
    file = open(filename, 'r')
    total = 0
    for line in file.readlines():
        first = finddigitv2(line)
        last = finddigitv2(line, forward=False)
        num = int(str(first) + str(last))
        total = total + num
    return total

print(parttwo("day1.txt"))