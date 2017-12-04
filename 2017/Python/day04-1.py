def passphrase(lines):
    total = 0
    for i in lines:
        passphrase = i.split()
        if len(passphrase) == len(set(passphrase)):
            total += 1
    return total

