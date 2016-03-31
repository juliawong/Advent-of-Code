''' What is the position of the first character that causes Santa to enter the basement (floor -1)? '''
def santaBasementFloor(floor_data):
    count = 1
    level = 0
    for floor in floor_data:
        if floor == "(":
            level += 1
        else:
            level -= 1
            if level == -1:
                break
        count += 1
    return count
