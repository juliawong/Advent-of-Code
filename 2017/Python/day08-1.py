from collections import defaultdict

def register(instructions):
    registers = defaultdict(int)
    for i in instructions:
        instruction, condition = i.strip().split(" if ")
        cond_var, op, cond_val = condition.split()
        if eval("registers[\"" + cond_var + "\"]" + " " + op + " int(" + cond_val + ")"):
            ins_var, ins_op, ins_val = instruction.split()
            if ins_op == "inc":
                registers[ins_var] += int(ins_val)
            else:
                registers[ins_var] -= int(ins_val)
    return max(registers.values())


