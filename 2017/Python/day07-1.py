def tower(programs):
    supported = []
    for i in programs:
        program = i.split()
        if len(program) > 2:
            supported.extend("".join(program[3:]).split(","))
    for i in programs:
        if i.split()[0] not in supported:
            return i
    return None

