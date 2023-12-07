def get_part_locations(line_num, line, part_dict):
    in_prog_number = ""
    line_dict = {}
    for col_num, char in enumerate(line):
        if char.isdigit():
            in_prog_number += char
        elif in_prog_number != "":
            line_dict[col_num-len(in_prog_number)] = in_prog_number
            in_prog_number = ""
    part_dict[line_num] = line_dict

def get_neighbours(row,col,length,height,width):
    neighbours = set()
    if row != 0:
        # Top Left
        if col != 0:
            neighbours.add((row-1, col-1))
        # Row above
        for i in range(length):
            neighbours.add((row-1,col+i))
        # Top Right
        if col + length < width:
            neighbours.add((row-1,col+length))
    if row != height-1:
        # Bottom Left
        if col != 0:
            neighbours.add((row+1, col-1))
        # Row below
        for i in range(length):
            neighbours.add((row+1,col+i))
        # Bottom Right
        if col + length < width:
            neighbours.add((row+1,col+length))
    if col != 0:
        neighbours.add((row,col-1))
    if col + length < width:
        neighbours.add((row,col+length))
    return neighbours

def check_neighbour_p1(row,col,length, lines):
    neighbours = get_neighbours(row,col,length,len(lines), len(lines[0].strip()))
    for check_row, check_col in neighbours:
        check_cell = lines[check_row][check_col]
        if  check_cell != "." and not check_cell.isdigit():
            return True
    return False

def get_parts_sum(lines, part_locations):
    count = 0
    for row, parts in part_locations.items():
        for col, part_value in parts.items():
            has_symbol_neighbour = check_neighbour_p1(row,col,len(part_value), lines)
            if has_symbol_neighbour:
                count += int(part_value)
    return count
def partone(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    part_locations = {}
    for i, line in enumerate(lines):
        get_part_locations(i, line, part_locations)
    count = get_parts_sum(lines, part_locations)
    print(count)

def get_part_cog_neighbours(part_locations, lines, part_cog_neighbours):
    # Map from location of cogs (*) to (row,col,value) of parts
    for row, parts in part_locations.items():
        for col, part_value in parts.items():
            neighbours = get_neighbours(row,col,len(part_value),len(lines), len(lines[0].strip()))
            for check_row, check_col in neighbours:
                if lines[check_row][check_col] == '*':
                    part_cog_neighbours[(check_row,check_col)] = part_cog_neighbours.get((check_row,check_col), set()).union({(row,col,part_value)})



def parttwo(filename):
    file = open(filename, 'r')
    lines = file.readlines()

    part_locations = {}
    for i, line in enumerate(lines):
        get_part_locations(i, line, part_locations)
    part_cog_neighbours = {}
    get_part_cog_neighbours(part_locations, lines, part_cog_neighbours)
    total_ratios = 0
    for cogs, parts in part_cog_neighbours.items():
        if len(parts) == 2:
            part1 = parts.pop()
            part2 = parts.pop()
            total_ratios += (int(part1[2]) * int(part2[2]))

# partone("day3.txt")
# parttwo("day3.txt")
