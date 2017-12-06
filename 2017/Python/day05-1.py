def count_steps(instructions):
    instructions = map(int, instructions)
    steps = 0
    curr_ind = 0

    while curr_ind in range(0, len(instructions)):
        new_ind = curr_ind + instructions[curr_ind]
        instructions[curr_ind] += 1
        curr_ind = new_ind
        steps += 1

    return steps

