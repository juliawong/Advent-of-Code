def memory_reallocation(memory_banks):
    memory_banks = map(int, memory_banks)
    seen = []
    steps = 0
    curr = ""
    while curr not in seen:
        seen.append(curr)
        min_ind = memory_banks.index(max(memory_banks))
        count = memory_banks[min_ind]
        memory_banks[min_ind] = 0
        for i in range(count):
            memory_banks[(min_ind + 1 + i) % len(memory_banks)] += 1

        curr = "".join(map(str, memory_banks))
        steps += 1

    return steps

