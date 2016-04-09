''' How many houses receive at least one present from Santa and Robo-Santa? '''
def santa_present_directions(directions):
    # Add starting location house
    delivered = [(0,0)]

    santa_directions = directions[::2]
    robo_directions = directions[1::2]

    add_delivered_locations(santa_directions, delivered)
    add_delivered_locations(robo_directions, delivered)

    return len(delivered)

''' Counts unique houses visited and adds location to delivered '''
def add_delivered_locations(directions, delivered):
    x = 0
    y = 0
    for direction in directions:
        # Calculate new position
        if direction == "^":
            x += 1
        elif direction == "v":
            x -= 1
        elif direction == "<":
            y -= 1
        else:
            y += 1

        if (x,y) not in delivered:
            delivered.append((x,y))
