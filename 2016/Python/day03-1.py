''' How many houses receive at least one present from Santa? '''
def santa_present_directions(santa_directions):
    x = 0
    y = 0

    # Add starting location house
    delivered = [(x,y)]

    for direction in santa_directions:
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

    return len(delivered)
