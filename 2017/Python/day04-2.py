def passphrase(lines):
    total = 0
    for i in lines:
        passphrase = map("".join, map(sorted, i.split()))
        if len(passphrase) == len(set(passphrase)):
            total += 1
    return total

