def tower(programs, base):
    structure = {}
    weights = {}
    rebalance = []
    for i in programs:
        i = i.strip()
        if "->" in i:
            program, weight, data = i.replace(", ", ",").split(" ", 2)
            structure[program] = data[3:].split(",")
        else:
            program, weight = i.split(" ")
        weight = int(weight[1:-1])
        weights[program] = weight
    calc_weight(base, structure, weights, rebalance)

def calc_weight(program, structure, weights, rebalance):
    if program not in structure:
        return weights[program]

    total = weights[program]
    seen = []
    for i in structure[program]:
        total += calc_weight(i, structure, weights, rebalance)
        seen.append(calc_weight(i, structure, weights, rebalance))
    weights[program] = total
    if len(set(seen)) != 1:
        rebalance.append(program)
    return total

