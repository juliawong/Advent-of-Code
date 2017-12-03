''' What is the total brightness of all lights? '''

def get_lights():
    DIMENSION = 1000
    lights = []
    for i in range(DIMENSION):
        lights.append([0] * DIMENSION)
    return lights

def turn_on(x1, x2, y1, y2, lights):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            lights[y][x] += 1

def turn_off(x1, x2, y1, y2, lights):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            lights[y][x] = max(0, lights[y][x] - 1)

def toggle(x1, x2, y1, y2, lights):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            lights[y][x] += 2

def count_total_brightness(instructions):
    # create lights
    lights = get_lights()

    # parse instructions
    instructions = instructions.replace("turn on", "on")
    instructions = instructions.replace("turn off", "off")
    instructions = instructions.split("\n")
    for instruction in instructions:
        action, from_coord, x, to_coord = instruction.split()
        x1, y1 = map(int, from_coord.split(","))
        x2, y2 = map(int, to_coord.split(","))

        if action == "on":
            turn_on(x1, x2, y1, y2, lights)
        elif action == "off":
            turn_off(x1, x2, y1, y2, lights)
        else:
            toggle(x1, x2, y1, y2, lights)


    return sum(map(sum, lights))
